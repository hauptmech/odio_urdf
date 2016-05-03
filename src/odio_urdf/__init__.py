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

    Parent(link="bla") -> Parent("bla")

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

        callers_local_vars = inspect.currentframe().f_back.f_back.f_locals.items()
 
        
        for arg in args:
            
            if type(arg) is str:
                setattr(self,'name',arg)
                self.attributes.add('name')
                
            elif type(arg) is Group:
                for elt in arg:
                    self.append(elt)
            else:
                if (type(arg) is type):
                    name = arg.__name__
                else:
                    name = type(arg).__name__
                    
                    
                if name in type(self).allowed_elements:
                    new_child = instantiate(arg)
                    self.append(new_child)
                    instantiated.append(name)
                    new_child.parent = self
                    
                    #If name is required and not there already, add it using the variable name
                    if 'name' in type(new_child).required_attributes and not 'name' in new_child.attributes:
                        #If we were a named variable, use it
                        name_val_list = [(var_name,var_val) for var_name, var_val in callers_local_vars if var_val is arg]
                        if len(name_val_list)>0:
                            name_val = name_val_list[0][0]
                            new_child.name = name_val
                            new_child.attributes.add('name')

                elif name in Element.xacro_tags:
                    pass
                   
                else:
                    raise Exception("Illegal element ["+name+']')
        
        for item in type(self).required_elements:
            if item not in instantiated:
                new_child = instantiate(globals()[item])
                self.append(new_child)
                new_child.parent = self
     
        for key,value in kwargs.items():
            if (key in type(self).allowed_attributes):
                setattr(self,key,value)
                self.attributes.add(key)
            else:
                raise Exception("Unknown attribute ["+key+']')


        

    def __call__(self,*args,**kwargs):
        
        callers_local_vars = inspect.currentframe().f_back.f_locals.items()

        name = ""
        for arg in args:
            if type(arg) is str:
                setattr(self,'name',arg)
                self.attributes.add('name')  
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
                
                    #If name is required and not there already, add it using the variable name
                    if 'name' in type(new_child).required_attributes and not 'name' in new_child.attributes:
                        #If we were a named variable, use it
                        name_val_list = [(var_name,var_val) for var_name, var_val in callers_local_vars if var_val is arg]
                        if len(name_val_list)>0:
                            name_val = name_val_list[-1][0]
                            new_child.name = name_val
                            new_child.attributes.add('name')

                elif name in Element.xacro_tags:
                    pass
                        
                else:
                    raise Exception("Illegal element ["+name+']')
            
            
        for key,value in kwargs.items():
            if (key in attributes):
                setattr(self,key,value)
                self.attributes.add(key)
            else:
                raise Exception("Unknown attribute ["+key+']')

        
        return self
                
    def __str__(self):
        return self.urdf(0)
        
    def __repr__(self):
        return self.urdf(0)

    def urdf(self,depth=0):
        s = " "*depth + "<" + type(self).__name__.lower() + " "
        if hasattr(self,'attributes'):
            for attr in self.attributes:
                to_insert = getattr(self,attr)
                if isinstance(to_insert,tuple):
                    to_insert = str(to_insert).strip('(').strip(')').replace(',','')
               
                s+= ' '+str(attr)+'="'+eval_macros(to_insert,Element.string_macros)+'" '
            #Flag required but unnamed attributes
            for attr in set(type(self).required_attributes).difference(self.attributes):
                s+= ' '+str(attr)+'="'+"UNNAMED_"+str(Element.element_counter)+'" '
                Element.element_counter += 1
        if len(self) == 0:
            s+= "/>\n"
        else:
            s+= ">\n"
                    
            for elt in self:
                s += elt.urdf(depth+1)
            
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
    allowed_elements = ['Joint','Link']
    required_attributes = []
    allowed_attributes = ['name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)	
		
class Robot(Element):
    counter = 0
    required_elements = []
    allowed_elements = ['Joint','Link','Material']
    required_attributes = ['name']
    allowed_attributes = ['name']
    
    def __init__(self, *args, **kwargs):
#        if not 'name' in kwargs:
#            kwargs['name'] = 'Robot'+str(Robot.counter)
#            Robot.counter += 1

        super().__init__(*args,**kwargs)

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

        super().__init__(*args,**kwargs)

     
class Link(Element):
    counter = 0
    required_elements = []
    allowed_elements = ['Inertial','Visual','Collision']
    required_attributes = ['name']
    allowed_attributes = ['name'] 
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

class Parent(Element):
    counter = 0
    required_elements = []
    allowed_elements = []
    required_attributes = ['link']
    allowed_attributes = ['link']  
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

class Child(Element):
    
    required_elements = []
    allowed_elements = []
    required_attributes = ['link']
    allowed_attributes = ['link'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

class Inertia(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['ixx','ixy','ixz','iyy','iyz','izz']  
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
      
class Visual(Element):
    required_elements = []
    allowed_elements = ['Origin','Geometry','Material']
    required_attributes = []
    allowed_attributes = []       
    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)

class Geometry(Element):
    required_elements = []
    allowed_elements = ['Box','Cylinder','Sphere','Mesh']
    required_attributes = []
    allowed_attributes = ['name']     
    
    def __init__(self, *args, **kwargs):
        if (len(args) != 1):
            raise Exception("Can only have one shape!")
        super().__init__(*args,**kwargs)
        
class Box(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['size']  
     
    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)
        
class Cylinder(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['radius','length']  
     
    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)
        
class Sphere(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['radius'] 
      
    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)
        
class Mesh(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['filename','scale'] 
      
    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)  

class Material(Element):
    required_elements = []
    allowed_elements = ['Color','Texture']
    required_attributes = ['name']
    allowed_attributes = ['name']       
    
    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)  
        
class Color(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['rgba']  
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs) 
		
class Texture(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['filename']  
    
    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)  
        
class Collision(Element):
    required_elements = []
    allowed_elements = ['Origin','Geometry']
    required_attributes = []
    allowed_attributes = ['name']  
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
class Mass(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['value'] 
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
     
class Origin(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xyz','rpy']       
    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)
        
class Axis(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['xyz']       
    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)
        
class Calibration(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['rising','falling']       
    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)
        
class Safety_controller(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['soft_lower_limit','soft_upper_limit','k_position','k_velocity']       
    def __init__(self, *args, **kwargs):

        super().__init__(*args,**kwargs)

class Limit(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = ['effort','velocity']
    allowed_attributes = ['lower','upper','effort','velocity']      
    def __init__(self, *args, **kwargs):
        
            
        super().__init__(*args,**kwargs)
        
class Dynamics(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['damping','friction']      
    def __init__(self, *args, **kwargs):
            
        super().__init__(*args,**kwargs)
                
class Mimic(Element):
    required_elements = []
    allowed_elements = []
    required_attributes = []
    allowed_attributes = ['joint','multiplier','offset']      
    def __init__(self, *args, **kwargs):
        if 'joint' not in kwargs:
            raise Exception('Mimic must have "joint" attribute')
            
        super().__init__(*args,**kwargs)
        
class Inertial(Element):
    required_elements = []
    allowed_elements = ['Origin','Mass','Inertia']
    required_attributes = []
    allowed_attributes = []  
     
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args,**kwargs)
    
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
    s = ""

    name = root.tag    
    if (root.tag[0] == '{'):
        name = 'xacro'+root.tag[root.tag.find('}')+1:]
    
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
    print(myRobot)
        




















