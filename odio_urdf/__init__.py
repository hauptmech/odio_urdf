"""
Author: hauptmech <hauptmech@gmail.com>

Copyright (c) 2016, 2021
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

-------------------------------------------------

Please see README.md for an overview.

"""
import six
import xml.etree.ElementTree as ET
import copy
import inspect


def eval_macros(string, env):
    to_eval_start = string.find('${')
    if to_eval_start == -1:
        return string
    to_eval_end = string.find('}',to_eval_start)
    if (to_eval_start != to_eval_end):
        res = eval(string[to_eval_start+2:to_eval_end],env)
        string = string[:to_eval_start]+str(res)+string[to_eval_end+1:]
    return eval_macros(string, env)

class ElementMeta(type):
    """ Metaclass for URDF element subclasses """
    _defaults_ = dict(
            required_elements=[],
            allowed_elements=[],
            required_attributes=[],
            arg_attributes=[],
        )

    def __new__(cls, name, bases, clsdict):
        """
            Populate class attributes from _default_ if they are not explicitly defined
        """
        for k in cls._defaults_:
            if not k in clsdict:
                clsdict[k] = cls._defaults_[k]

        return super(ElementMeta, cls).__new__(cls, name, bases, clsdict)

class NamedElementMeta(ElementMeta):
    """ Many elements have 'name' as a required attribute """
    _defaults_ = dict(ElementMeta._defaults_, required_attributes=["name"], arg_attributes=["name"])


def instantiate(subject):
    """ If subject is a type instead of an instance, instantiate it"""
    if type(subject) in [type, ElementMeta, NamedElementMeta]:
        ret = globals()[subject.__name__]()
    else:
        ret = subject
    return ret

@six.add_metaclass(ElementMeta)
class Element(list):
    """
        Parent class for all URDF elements

        All element classes have class attributes that define what sub elements and xml attributes are
        allowed or required.

        required_elements: If any sub-element in this list is not present, it generates an error on xml output
        allowed_elements: If a sub-element NOT in this list is provided, it generates an error
        required_attributes: If any attribute in this list is not provided, it will be auto-generated
        arg_attributes: Unnamed args will be assigned to these attributes sequentially.
    """
    element_counter = 0
    string_macros = {}
    xacro_tags = ['Xacroproperty','Xacroinclude','Xacroif','Xacrounless']

    def __init__(self,*args,**kwargs):

        self.attributes = set()
        instantiated = []
        self.xmltext = ""

        up_frame = inspect.currentframe().f_back
        if up_frame.f_back:
            up_frame = up_frame.f_back
        callers_local_vars = up_frame.f_locals.items()

        # __call__() adds and sets all our attributes and elements
        self._populate_element_(*args, **kwargs)

        # Create defaults for any required elements that have not been created yet.
        for arg in args:
            if type(arg) is not str and type(arg) is not Group:
                if type(arg) in [type,ElementMeta,NamedElementMeta]:
                    name = arg.__name__
                else:
                    name = type(arg).__name__

                if name in type(self).allowed_elements:
                    instantiated.append(name)

        for item in type(self).required_elements:
            if item not in instantiated:
                new_child = instantiate(globals()[item])
                self.append(new_child)
                new_child.parent = self


    def __call__(self,*args,**kwargs):
        """
            For our DSL, allow existing instances to be populated with sub-elements the same way
            we allow during instantiation

            ```
            robot = Robot('my_robot_name', Link('my_link_name')) # populate with a link during object creation
            robot( Link('My_second_link') ) # Add a second link to the instance

            ```
        """
        self._populate_element_(*args, **kwargs)

    def _populate_element_(self,*args,**kwargs):
        """ Populate a URDF element with attributes and sub elements

            *args of type str and int will be assigned one-by-one to the attributes in Class.arm_attributes
            *args derrived from Element will be added to the sub-element list


            **kwargs will be assigned to the attribute implied by the keyword

            xmltext = "<somexml/>" will be directly injected into the output
        """

        if 'xmltext' in kwargs:
            self.xmltext = kwargs['xmltext']
            del kwargs['xmltext']

        if 'xacro_xml' in kwargs:
            xacroroot = ET.fromstring(kwargs['xacro_xml'])   # The root shoud be <Robot/>
            for child in xacroroot:
                self.xmltext += ET.tostring(child,encoding='unicode') # Add the xml to our <Robot>
            del kwargs['xacro_xml']

        callers_local_vars = inspect.currentframe().f_back.f_locals.items()

        name = ""
        unlabeled = 0 # Count of unlabeled strings we have encountered so far
        for arg in args:
            # myjoint("myname","mytype")
            if type(arg) is str:
                if unlabeled in range(len(type(self).arg_attributes)):
                    setattr(self,type(self).arg_attributes[unlabeled],arg)
                    self.attributes.add(type(self).arg_attributes[unlabeled])
                    unlabeled += 1
            elif type(arg) is Group:
                for elt in arg:
                    self.append(elt)
            else:
                if type(arg) in [type,ElementMeta,NamedElementMeta]:
                    name = arg.__name__
                else:
                    name = type(arg).__name__

                if name in self.allowed_elements:
                    new_child = instantiate(arg)
                    self.append(new_child)
                    new_child.parent = self

                    #If name is required and not there already, add it using the variable name
                    if 'name' in type(new_child).required_attributes and not 'name' in new_child.attributes:
                        #If we were a named variable, use it
                        name_val_list = [(var_name,var_val) for var_name, var_val in callers_local_vars if var_val is arg]
                        if len(name_val_list)>0:
                            name_val = name_val_list[-1][0] #Use most recent label
                            new_child.name = name_val
                            new_child.attributes.add('name')

                elif name in Element.xacro_tags:
                    pass

                else:
                    raise Exception("Illegal element ["+name+']')


        for key,value in kwargs.items():
            if (key in type(self).arg_attributes):
                #Convert raw numbers and number lists to strings
                if isinstance(value,int) or isinstance(value,float):
                    value = str(value)
                elif isinstance(value,tuple) or isinstance(value,list):
                    value = " ".join([str(x) for x in value])

                setattr(self,key,value)
                self.attributes.add(key)
            else:
                raise Exception("Unknown attribute ["+key+']')
        return self

    def __str__(self):
        return self.urdf()

    def __repr__(self):
        return self.urdf()

    special_names = {"transjoint": "joint"}
    def urdf(self,depth=0):
        name = type(self).__name__.lower()
        if name in self.special_names: name = self.special_names[name]
        s = " "*depth + "<" + name + " "
        if hasattr(self,'attributes'):
            for attr in self.attributes:
                to_insert = str(getattr(self,attr))
                if isinstance(to_insert,tuple):
                    to_insert = str(to_insert).strip('(').strip(')').replace(',','')

                s+= ' '+str(attr)+'="'+eval_macros(to_insert,Element.string_macros)+'" '
            #Flag required but unnamed attributes
            for attr in set(type(self).required_attributes).difference(self.attributes):
                s+= ' '+str(attr)+'="'+"UNNAMED_"+str(Element.element_counter)+'" '
                Element.element_counter += 1
        if len(self) == 0 and self.xmltext == "":
            s+= "/>\n"
        else:
            s+= ">\n"

            for elt in self:
                s += elt.urdf(depth+1)
            if self.xmltext != "":
                s +=" "*(depth+1) + self.xmltext + "\n"
            s +=" "*depth + "</" + type(self).__name__.lower() + ">\n"
        return s

@six.add_metaclass(NamedElementMeta)
class NamedElement(Element):
    pass
############# elements #############

class Xacroinclude(Element):pass
class Xacrounless(Element):pass
class Xacroif(Element):pass
class Xacroproperty(Element):
    def __init__(self, **kwargs):
        if ('name' in kwargs and 'value' in kwargs):
            Element.string_macros[kwargs['name']] = float(kwargs['value'])


class Group(Element):
    """ A group of <Robot> top level elements that will be appended to the Robot() that owns this group"""
    allowed_elements = ['Joint','Link','Material','Transmission','Gazebo']
    arg_attributes = ['name']


class Robot(NamedElement):
    """ Robot is the top level element in a URDF """
    allowed_elements = ['Joint','Link','Material','Transmission','Gazebo']

    def urdf(self, depth=0):
        return '<?xml version="1.0"?>\n'+super(Robot,self).urdf(0)

class Joint(NamedElement):
    required_elements = ['Parent','Child']
    allowed_elements = ['Parent','Child','Origin','Inertial','Visual','Collision','Axis','Calibration','Dynamics','Limit','Mimic','Safety_controller']
    required_attributes = ['type']
    arg_attributes = ['type']

    def __init__(self, *args, **kwargs):

        if not 'type' in kwargs:
            kwargs['type'] = 'revolute'

        Joint_types = ['revolute','continuous','prismatic','fixed','floating','planar']
        if kwargs['type'] not in Joint_types:
            raise Exception('Joint type not correct')

        super(Joint, self).__init__(*args,**kwargs)


class Link(NamedElement):
    allowed_elements = ['Inertial','Visual','Collision','Self_collision_checking', 'Contact']

class Transmission(NamedElement):
    allowed_elements = ['Type','Transjoint','Actuator']

class Type(Element): pass

class Transjoint(NamedElement):
    allowed_elements = ['Hardwareinterface']

class Hardwareinterface(Element): pass

class Mechanicalreduction(Element):pass

class Actuator(NamedElement):
    allowed_elements = ['Mechanicalreduction','Hardwareinterface']

class Parent(Element):
    required_attributes = ['link']
    arg_attributes = ['link']

class Child(Element):
    required_attributes = ['link']
    arg_attributes = ['link']

class Inertia(Element):
    arg_attributes = ['ixx','ixy','ixz','iyy','iyz','izz']
    def __init__(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0],list):
            if len(args[0]) == 6:
                kwargs["ixx"]=str(args[0][0])
                kwargs["ixy"]=str(args[0][1])
                kwargs["ixz"]=str(args[0][2])
                kwargs["iyy"]=str(args[0][3])
                kwargs["iyz"]=str(args[0][4])
                kwargs["izz"]=str(args[0][5])
        super(Inertia, self).__init__(**kwargs)

class Visual(Element):
    allowed_elements = ['Origin','Geometry','Material']

class Geometry(Element):
    allowed_elements = ['Box','Cylinder','Sphere','Mesh','Capsule']
    arg_attributes = ['name']

    def __init__(self, *args, **kwargs):
        if (len(args) != 1):
            raise Exception("Can only have one shape!")
        super(Geometry, self).__init__(*args,**kwargs)

class Box(Element):
    arg_attributes = ['size']

class Capsule(Element):
    arg_attributes = ['radius','length']

class Cylinder(Element):
    arg_attributes = ['radius','length']

class Sphere(Element):
    arg_attributes = ['radius']

class Mesh(Element):
    arg_attributes = ['filename','scale']

class Material(Element):
    allowed_elements = ['Color','Texture']
    arg_attributes = ['name']

class Color(Element):
    arg_attributes = ['rgba']

class Texture(Element):
    arg_attributes = ['filename']

class Collision(Element):
    allowed_elements = ['Origin','Geometry','Material']
    arg_attributes = ['name']

class Self_collision_checking(Element):
    allowed_elements = ['Origin','Geometry']
    arg_attributes = ['name']

class Mass(Element):
    arg_attributes = ['value']

class Origin(Element):
    arg_attributes = ['xyz','rpy']
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0],list):
            if len(args[0]) == 6:
                kwargs["xyz"]=str(args[0][0])+' '+str(args[0][1])+' '+str(args[0][2])
                kwargs["rpy"]=str(args[0][3])+' '+str(args[0][4])+' '+str(args[0][5])

            if len(args[0]) == 3:
                kwargs["xyz"]=str(args[0][0])+' '+str(args[0][1])+' '+str(args[0][2])

        super(Origin, self).__init__(**kwargs)

class Axis(Element):
    arg_attributes = ['xyz']

class Calibration(Element):
    arg_attributes = ['rising','falling']

class Safety_controller(Element):
    arg_attributes = ['soft_lower_limit','soft_upper_limit','k_position','k_velocity']

class Limit(Element):
    required_attributes = ['effort','velocity']
    arg_attributes = ['lower','upper','effort','velocity']

class Dynamics(Element):
    arg_attributes = ['damping','friction']

class Mimic(Element):
    arg_attributes = ['joint','multiplier','offset']
    def __init__(self, *args, **kwargs):
        if 'joint' not in kwargs:
            raise Exception('Mimic must have "joint" attribute')
        super(Mimic, self).__init__(*args,**kwargs)

class Inertial(Element):
    allowed_elements = ['Origin','Mass','Inertia']

class Gazebo(Element):
    allowed_elements = ['Material','Gravity','Dampingfactor','Maxvel','Mindepth','Mu1','Mu2',
        'Fdir1','Kp','Kd','Selfcollide','Maxcontacts','Laserretro','Plugin']
    arg_attributes = ['reference','xmltext']

class Plugin(Element):
    allowed_elements = ['Robotnamespace']
    arg_attributes = ['name','filename']

class Robotnamespace(Element): pass
class Gravity(Element): pass
class Laserretro(Element): pass
class Maxcontacts(Element): pass
class Selfcollide(Element): pass
class Kd(Element): pass
class Kp(Element): pass
class Fdir1(Element): pass
class Mu2(Element): pass
class Dampingfactor(Element): pass
class Maxvel(Element): pass
class Mindepth(Element): pass
class Mu1(Element): pass

class Contact(Element):
    """Bullet3 element."""
    allowed_elements = ['Stiffness', 'Damping', 'Lateral_Friction']

class Stiffness(Element):
    """Bullet3 element."""
    arg_attributes = ['value']

class Damping(Element):
    """Bullet3 element."""
    arg_attributes = ['value']

class Lateral_Friction(Element):
    """Bullet3 element."""
    arg_attributes = ['value']

################## elements###########

def urdf_to_odio(urdf_string):
    """
        Dump a URDF string to odio DSL representation
    """
    root = ET.fromstring(urdf_string)

    s = xml_to_odio(root)
    return s


def xml_to_odio(root,depth=0):
    """
        Dump an xml ElementTree to the odio DSL representation
    """
    special_names = {}
    s = ""

    name = root.tag
    if (root.tag[0] == '{'):
        name = 'xacro'+root.tag[root.tag.find('}')+1:]

    if name in special_names:
        name = special_names[name]

    s += "\n"+ ' '*depth + name.capitalize() + '('

    for tag in root:
        s+= dump(tag,depth+1) + ','

    if len(root.attrib.items()) < 3:
        space = ""
        if (len(root)>0):
            s+= '\n'+' '*(depth+1)
    else:
        space =  '\n'+' '*(depth+1)

    for key,value in root.attrib.items():
        s+= space + key + '= "'+value+'",'

    if root.text.strip() != "":
        s+= space + 'xmltext = "'+root.text+'",'

    if s[-1]==',':
        s = s[:-1]

    if len(root) < 0:
        s += ')'
    else:
        s+= space + ')'
        #s+= '\n'+' '*depth +')'
    return s

if __name__ == "__main__":
    pass
















