"""
Author: hauptmech <hauptmech@gmail.com> 

Copyright (c) 2016
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

-------------------------------------------------

Please see README.md for an overview.

"""
import xml.etree.ElementTree as ET
import copy
import inspect

def instantiate(subject):
    if (type(subject) is type):
        ret = globals()[subject.__name__]()
    else:
        ret = subject
    return ret
  
"""
ToDo:
    Process tuples into string
    Default values for attributes
    
    Origin() -> Origin(xyz= "0 0 0",rpy= "0 0 0")
    Mesh(scale=10, filename="bla")-> Mesh(scale="10 10 10", filename="bla")
    Inertia(i="a b c") -> 
    Inertia(
        izz= "c",
        iyy= "b",
        ixx= "a",
        iyz= "0.0",
        ixy= "0.0",
        ixz= "0.0"
        ),

"""
 
def eval_macros(string, env):
    to_eval_start = string.find('${')
    if to_eval_start == -1:
        return string
    to_eval_end = string.find('}',to_eval_start)
    if (to_eval_start != to_eval_end):
        res = eval(string[to_eval_start+2:to_eval_end],env)
        string = string[:to_eval_start]+str(res)+string[to_eval_end+1:]
    return eval_macros(string, env)

    
class Element(list):
    element_counter = 0
    string_macros = {}
    xacro_tags = ['Xacroproperty','Xacroinclude','Xacroif','Xacrounless']
    
    def __init__(self,*args,**kwargs):
        
        self.attributes = set()
        instantiated = []
        self.xmltext = "" 

        callers_local_vars = inspect.currentframe().f_back.f_back.f_locals.items()
               
        # __call__() adds and sets all our attributes and elements
        self(*args, **kwargs)

        # Create defaults for any required elements that have not been created yet.
        for arg in args:
            if type(arg) is not str and type(arg) is not Group:
                if (type(arg) is type):
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
        
        if 'xmltext' in kwargs:
            self.xmltext = kwargs['xmltext']
            del kwargs['xmltext'] 

        callers_local_vars = inspect.currentframe().f_back.f_locals.items()

        name = ""
        unlabeled = 0 # Count of unlabeled strings we have encountered so far
        for arg in args:
            # myjoint("myname","mytype")
            if type(arg) is str:
                if unlabeled in range(len(type(self).allowed_attributes)):
                    setattr(self,type(self).allowed_attributes[unlabeled],arg)
                    self.attributes.add(type(self).allowed_attributes[unlabeled])
                    unlabeled += 1
            elif type(arg) is Group:
                for elt in arg:
                    self.append(elt)
            else:
                if (type(arg) is type):
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
            if (key in type(self).allowed_attributes):
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
        return self.urdf(0)
        
    def __repr__(self):
        return self.urdf(0)

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
        
############# elements #############

class Xacroproperty(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = [] 
    def __init__(self, **kwargs):
        if ('name' in kwargs and 'value' in kwargs):
            Element.string_macros[kwargs['name']] = float(kwargs['value'])
            
class Xacroinclude(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = [] 
    
    def __init__(self, **kwargs):
        pass
            
class Xacrounless(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = [] 
    
    def __init__(self, **kwargs):
        pass
            
class Xacroif(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = [] 
    
    def __init__(self, **kwargs):
        pass

class Group(Element):
    counter = 0
    required_elements = []
    allowed_elements = ['Joint','Link','Material','Transmission','Gazebo']
    required_attributes = []
    allowed_attributes = ['name']
    
    def __init__(self, *args, **kwargs):
        super(Group, self).__init__(*args,**kwargs)	
		
class Robot(Element):
    counter = 0
    required_elements = []
    allowed_elements = ['Joint','Link','Material','Transmission','Gazebo']
    required_attributes = ['name']
    allowed_attributes = ['name']
    
    def __init__(self, *args, **kwargs):
#        if not 'name' in kwargs:
#            kwargs['name'] = 'Robot'+str(Robot.counter)
#            Robot.counter += 1

        super(Robot, self).__init__(*args,**kwargs)

    def __str__(self):
        return '<?xml version="1.0"?>\n'+self.urdf(0)
        
class Joint(Element):
    counter = 0     
    required_elements = ['Parent','Child']
    allowed_elements = ['Parent','Child','Origin','Inertial','Visual','Collision','Axis','Calibration','Dynamics','Limit','Mimic','Safety_controller']
    required_attributes = ['name','type']
    allowed_attributes = ['name','type']
    
    def __init__(self, *args, **kwargs):

#        if not 'name' in kwargs:
#            kwargs['name'] = 'JOINT'+str(Joint.counter)
#            Joint.counter += 1
        
        if not 'type' in kwargs:
            kwargs['type'] = 'revolute'
            
        Joint_types = ['revolute','continuous','prismatic','fixed','floating','planar']
        if kwargs['type'] not in Joint_types:
            raise Exception('Joint type not correct')

        super(Joint, self).__init__(*args,**kwargs)

     
class Link(Element):
    counter = 0
    required_elements = []
    allowed_elements = ['Inertial','Visual','Collision','Self_collision_checking', 'Contact']
    required_attributes = ['name']
    allowed_attributes = ['name'] 
    def __init__(self, *args, **kwargs):
        super(Link, self).__init__(*args,**kwargs)

class Transmission(Element):
    counter = 0
    required_elements = []
    allowed_elements = ['Type','Transjoint','Actuator']
    required_attributes = ['name']
    allowed_attributes = ['name']  
    
    def __init__(self, *args, **kwargs):
        super(Transmission, self).__init__(*args,**kwargs)


class Type(Element):
    counter = 0
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xmltext']  
    
    def __init__(self, *args, **kwargs):
        super(Type, self).__init__(*args,**kwargs)

class Transjoint(Element):
    counter = 0
    required_elements = []
    allowed_elements = ['Hardwareinterface']
    required_attributes = ['name']
    allowed_attributes = ['name']  
    
    def __init__(self, *args, **kwargs):
        super(Transjoint, self).__init__(*args,**kwargs)

class Hardwareinterface(Element):
    counter = 0
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xmltext']  
    
    def __init__(self, *args, **kwargs):
        super(Hardwareinterface, self).__init__(*args,**kwargs)

class Mechanicalreduction(Element):
    counter = 0
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xmltext']  
    
    def __init__(self, *args, **kwargs):
        super(Mechanicalreduction, self).__init__(*args,**kwargs)




class Actuator(Element):
    counter = 0
    required_elements = []
    allowed_elements = ['Mechanicalreduction','Hardwareinterface']
    required_attributes = ['name']
    allowed_attributes = ['name']  
    
    def __init__(self, *args, **kwargs):
        super(Actuator, self).__init__(*args,**kwargs)






class Parent(Element):
    counter = 0
    required_elements = []
    allowed_elements = []
    required_attributes = ['link']
    allowed_attributes = ['link']  
    
    def __init__(self, *args, **kwargs):
        super(Parent, self).__init__(*args,**kwargs)

class Child(Element):
    
    required_elements = []
    allowed_elements = []
    required_attributes = ['link']
    allowed_attributes = ['link'] 

    def __init__(self, *args, **kwargs):
        super(Child, self).__init__(*args,**kwargs)

class Inertia(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['ixx','ixy','ixz','iyy','iyz','izz']  
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
    required_elements = []
    allowed_elements = ['Origin','Geometry','Material']
    required_attributes = []
    allowed_attributes = []       
    def __init__(self, *args, **kwargs):
        super(Visual, self).__init__(*args,**kwargs)

class Geometry(Element):
    required_elements = []
    allowed_elements = ['Box','Cylinder','Sphere','Mesh','Capsule']
    required_attributes = []
    allowed_attributes = ['name']     
    
    def __init__(self, *args, **kwargs):
        if (len(args) != 1):
            raise Exception("Can only have one shape!")
        super(Geometry, self).__init__(*args,**kwargs)
        
class Box(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['size']  
     
    def __init__(self, *args, **kwargs):

        super(Box, self).__init__(*args,**kwargs)
 
class Capsule(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['radius','length']  
     
    def __init__(self, *args, **kwargs):
        super(Capsule, self).__init__(*args,**kwargs)
        
class Cylinder(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['radius','length']  
     
    def __init__(self, *args, **kwargs):
        super(Cylinder, self).__init__(*args,**kwargs)
        
class Sphere(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['radius'] 
      
    def __init__(self, *args, **kwargs):

        super(Sphere, self).__init__(*args,**kwargs)
        
class Mesh(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['filename','scale'] 
      
    def __init__(self, *args, **kwargs):

        super(Mesh, self).__init__(*args,**kwargs)  

class Material(Element):
    required_elements = []
    allowed_elements = ['Color','Texture']
    required_attributes = []
    allowed_attributes = ['name']       
    
    def __init__(self, *args, **kwargs):
        super(Material, self).__init__(*args,**kwargs)  
        
class Color(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['rgba']  
     
    def __init__(self, *args, **kwargs):
        super(Color, self).__init__(*args,**kwargs) 
		
class Texture(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['filename']  
    
    def __init__(self, *args, **kwargs):

        super(Texture, self).__init__(*args,**kwargs)  
        
class Collision(Element):
    required_elements = []
    allowed_elements = ['Origin','Geometry','Material']
    required_attributes = []
    allowed_attributes = ['name']  
     
    def __init__(self, *args, **kwargs):
        super(Collision, self).__init__(*args,**kwargs)
         
class Self_collision_checking(Element):
    required_elements = []
    allowed_elements = ['Origin','Geometry']
    required_attributes = []
    allowed_attributes = ['name']  
     
    def __init__(self, *args, **kwargs):
        super(Self_collision_checking, self).__init__(*args,**kwargs)
        
class Mass(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['value'] 
     
    def __init__(self, *args, **kwargs):
        super(Mass, self).__init__(*args,**kwargs)
     
class Origin(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xyz','rpy']       
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0],list):
            if len(args[0]) == 6:
                kwargs["xyz"]=str(args[0][0])+' '+str(args[0][1])+' '+str(args[0][2])
                kwargs["rpy"]=str(args[0][3])+' '+str(args[0][4])+' '+str(args[0][5])
                
            if len(args[0]) == 3:
                kwargs["xyz"]=str(args[0][0])+' '+str(args[0][1])+' '+str(args[0][2])
            

        super(Origin, self).__init__(**kwargs)
        
class Axis(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xyz']       
    def __init__(self, *args, **kwargs):

        super(Axis, self).__init__(*args,**kwargs)
        
class Calibration(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['rising','falling']       
    def __init__(self, *args, **kwargs):

        super(Calibration, self).__init__(*args,**kwargs)
        
class Safety_controller(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['soft_lower_limit','soft_upper_limit','k_position','k_velocity']       
    def __init__(self, *args, **kwargs):

        super(Safety_controller, self).__init__(*args,**kwargs)

class Limit(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = ['effort','velocity']
    allowed_attributes = ['lower','upper','effort','velocity']      
    def __init__(self, *args, **kwargs):
        
            
        super(Limit, self).__init__(*args,**kwargs)
        
class Dynamics(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['damping','friction']      
    def __init__(self, *args, **kwargs):
            
        super(Dynamics, self).__init__(*args,**kwargs)
                
class Mimic(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['joint','multiplier','offset']      
    def __init__(self, *args, **kwargs):
        if 'joint' not in kwargs:
            raise Exception('Mimic must have "joint" attribute')
            
        super(Mimic, self).__init__(*args,**kwargs)
        
class Inertial(Element):
    required_elements = []
    allowed_elements = ['Origin','Mass','Inertia']
    required_attributes = []
    allowed_attributes = []  
     
    def __init__(self, *args, **kwargs):
        
        super(Inertial, self).__init__(*args,**kwargs)
 
class Gazebo(Element):
    counter = 0
    required_elements = []
    allowed_elements = ['Material','Gravity','Dampingfactor','Maxvel','Mindepth','Mu1','Mu2',
        'Fdir1','Kp','Kd','Selfcollide','Maxcontacts','Laserretro','Plugin']
    required_attributes = []
    allowed_attributes = ['reference','xmltext']  
    
    def __init__(self, *args, **kwargs):
        super(Gazebo, self).__init__(*args,**kwargs)
 
class Plugin(Element):
    counter = 0
    required_elements = []
    allowed_elements = ['Robotnamespace']
    required_attributes = []
    allowed_attributes = ['name','filename']  

 
class Robotnamespace(Element):
    counter = 0
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xmltext']  

class Gravity(Element):
    counter = 0
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xmltext']  
        
class Laserretro(Element):
    counter = 0
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xmltext']  
   

class Maxcontacts(Element):
    counter = 0
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xmltext']  
   

class Selfcollide(Element):
    counter = 0
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xmltext']  
   

class Kd(Element):
    counter = 0
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xmltext']  
   

class Kp(Element):
    counter = 0
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xmltext']  
   

class Fdir1(Element):
    counter = 0
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xmltext']  
   

class Mu2(Element):
    counter = 0
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xmltext']  
   
 
class Dampingfactor(Element):
    counter = 0
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xmltext']  
   
 
class Maxvel(Element):
    counter = 0
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xmltext']  
   
 
class Mindepth(Element):
    counter = 0
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xmltext']  
   
 
class Mu1(Element):
    counter = 0
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xmltext']  
   
class Contact(Element):
    """Bullet3 element.
    """
    required_elements = []
    allowed_elements = ['Stiffness', 'Damping', 'Lateral_Friction']
    required_attributes = []
    allowed_attributes = []

    def __init__(self, *args, **kwargs):
        super(Contact, self).__init__(*args, **kwargs)


class Stiffness(Element):
    """Bullet3 element.
    """
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['value']

    def __init__(self, *args, **kwargs):
        super(Stiffness, self).__init__(*args, **kwargs)


class Damping(Element):
    """Bullet3 element.
    """
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['value']

    def __init__(self, *args, **kwargs):
        super(Damping, self).__init__(*args, **kwargs)


class Lateral_Friction(Element):
    """Bullet3 element.
    """
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['value']

    def __init__(self, *args, **kwargs):
        super(Lateral_Friction, self).__init__(*args, **kwargs)
################## elements###########

def dump_urdf(urdf_string):
    root = ET.fromstring(urdf_string)

    s = dump(root)
    return s
    
def dump_urdf_contents(urdf_string):
    root = ET.fromstring(urdf_string)
    s = ""
    for elt in root:
        s += dump(elt)
    return s   
    
def dump(root,depth=0):
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
    
    myRobot = Link(
        Inertial(
            Origin(xyz=(0,0,0.5), rpy=(0,0,0)),
            Mass(value=1),
            Inertia(ixx=100, ixy=0),
        ),
        Visual,
        Collision,
        name="test"
        )
    
    print(Origin([2,3,4]))
    print(Origin([7,8,6,7,5,4]))
    print(Inertia([1,2,3,4,4,2]))
        




















