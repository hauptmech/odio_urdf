"""
    An example of how to easily add new elements or monkey patch the existing ones.
    (Thanks to The-Ripp3r for the example of what people might want to add)


    1: Add a new element:
        a) subclass Element
        b) required_elements, allowed_elements, required_attributes, and allowed_attributes are pre-defined as empty list so only fill in the ones you need.
            allowed_elements: The xml sub-elements (tags) that are allowed
            required_elements: The xml sub-elements that MUST be present
            allowed_attributes: The xml attributes that are allowed
            required_attributes: The xml attributes that are required
    2: Allow a new element to be added to an existing element.
    3: Set the element name to be different than the class name


    Please submit pull requests for new elements added to odio_urdf/__init__.py so that all can benefit.

"""

from odio_urdf import *

# 1: Add a new element
class Deformable(Element): 
    required_elements = ['Inertial', 'Visual2'] 
    allowed_elements = ['Collision_margin', 'Repulsion_Stiffness', 'Friction', 'Neohookean']
    required_attributes = ['name']

# 2: Allow our new element to be added to existing elements
Group.allowed_elements += [ 'Deformable' ]
Robot.allowed_elements += [ 'Deformable' ]

class Visual2(Element):
    required_attributes = ['filename']
    element_name = "visual"              # 3: Set the element name to be different than the class name

class Collision_margin(Element):
    allowed_attributes = ['value']

class Repulsion_Stiffness(Element):
    allowed_attributes = ['value']

class Friction(Element):
    allowed_attributes = ['value']  

class Neohookean(Element):
    allowed_attributes = ['mu','lam','damping']  

myRobot2 = Robot(
            Deformable(
                Inertial(
                    Origin((0,0,0.5), rpy=(0,0,0)),
                    #Origin("0 0 0.5", rpy=(0,0,0)),
                    Mass(value=1),
                    Inertia(0,1,2,3,4,5,6),
                ),
                Visual2(filename="torus.vtk"),
                Collision_margin(value = 0.006),
                Repulsion_Stiffness(value = 800.0),
                Friction(value = 0.5),
                Neohookean(200.0, 200.0, 0.01), # mu, lam, and damping populated in attribute order
                name="practice"
            )
        )

print(myRobot2)
