"""
Copied from https://github.com/EnricoMingo/iit-coman-ros-pkg
"""

from odio_urdf import *

torso = Group(
 Xacroproperty(
  name= "PI",
  value= "3.14159265359"
 ),
 Xacroproperty(
  name= "PI_2",
  value= "1.57079632679"
 ),
 Xacroproperty(
  name= "SF",
  value= "0.03937"
 ),
 Xacroproperty(
  name= "cos_20",
  value= "0.93969262078"
 ),
 Xacroproperty(
  name= "sin_20",
  value= "0.34202014332"
 ),
 Link(
  name= "torso"
 ),
 Link(
  Inertial(
   Origin(
    rpy= "0 0 0",
    xyz= "4.2999707E-4 -0.0097650317 0.033011157"
   ),
   Mass(
    value= "0.54588774"
   ),
   Inertia(
    iyy= "7.4686706E-4",
    iyz= "-1.7450917E-4",
    ixy= "-7.2101244E-7",
    ixz= "1.1440119E-6",
    izz= "6.2196235E-4",
    ixx= "9.7126578E-4"
   )
  ),
  Visual(
   Origin(
    rpy= "0 0 ${PI}",
    xyz= "-0.020281504 0 -0.63912053"
   ),
   Material(
    name= "dark_grey"
   ),
   Geometry(
    Mesh(
     scale= "${SF} ${SF} ${SF}",
     filename= "package://coman_urdf/meshes/Torso1.STL"
    ),
    name= "DWL_visual"
   )
  ),
  Collision(
   Origin(
    rpy= "0 0 ${PI}",
    xyz= "-0.020281504 0 -0.63912053"
   ),
   Geometry(
    Mesh(
     scale= "${SF} ${SF} ${SF}",
     filename= "package://coman_urdf/meshes/simple/Torso1.STL"
    ),
    name= "DWL_collision"
   )
  ),
  name= "DWL"
 ),
 Link(
  Inertial(
   Origin(
    rpy= "0 0 0",
    xyz= "-0.0021273416 0.0033575235 -0.0010076896"
   ),
   Mass(
    value= "0.75398402"
   ),
   Inertia(
    iyy= "3.9581916E-4",
    iyz= "1.443019E-6",
    ixy= "-6.2120042E-6",
    ixz= "-1.3863473E-6",
    izz= "3.7449753E-4",
    ixx= "3.4093348E-4"
   )
  ),
  Visual(
   Origin(
    rpy= "0 0 ${PI}",
    xyz= "-0.020281504 0 -0.63912053"
   ),
   Material(
    name= "dark_grey"
   ),
   Geometry(
    Mesh(
     scale= "${SF} ${SF} ${SF}",
     filename= "package://coman_urdf/meshes/Torso2.STL"
    ),
    name= "DWS_visual"
   )
  ),
  Collision(
   Origin(
    rpy= "0 0 ${PI}",
    xyz= "-0.020281504 0 -0.63912053"
   ),
   Geometry(
    Mesh(
     scale= "${SF} ${SF} ${SF}",
     filename= "package://coman_urdf/meshes/simple/Torso2.STL"
    ),
    name= "DWS_collision"
   )
  ),
  name= "DWS"
 ),
 Link(
  Inertial(
   Origin(
    rpy= "0 0 0",
    xyz= "-0.0358501 1.8286043E-5 0.117557148"
   ),
   Mass(
    value= "6.3617175"
   ),
   Inertia(
    iyy= "0.030117357",
    iyz= "6.2443771E-6",
    ixy= "-9.8308572E-6",
    ixz= "-7.5649290E-4",
    izz= "0.025296582",
    ixx= "0.034089342"
   )
  ),
  Visual(
   Origin(
    rpy= "0 0 ${PI}",
    xyz= "-0.020281504 0.0 -0.68662053"
   ),
   Material(
    name= "red"
   ),
   Geometry(
    Mesh(
     scale= "${SF} ${SF} ${SF}",
     filename= "package://coman_urdf/meshes/Torso3.STL"
    ),
    name= "DWYTorso_visual"
   )
  ),
  Collision(
   Origin(
    rpy= "0 0 ${PI}",
    xyz= "-0.020281504 0.0 -0.68662053"
   ),
   Geometry(
    Mesh(
     scale= "${SF} ${SF} ${SF}",
     filename= "package://coman_urdf/meshes/simple/Torso3.STL"
    ),
    name= "DWYTorso_collision"
   )
  ),
  name= "DWYTorso"
 ),
 Joint(
  Parent(
   link= "DWYTorso"
  ),
  Child(
   link= "torso"
  ),
  Origin(
   rpy= "0 0 0",
   xyz= "-0.014976503999999998 0 0.15770847"
  ),
  name= "torso_joint",
  type= "fixed"
 ),
 Joint(
  Parent(
   link= "Waist"
  ),
  Child(
   link= "DWL"
  ),
  Origin(
   rpy= "0 0 0",
   xyz= "0.020281504 0 0.11912053"
  ),
  Axis(
   xyz= "${cos_20} 0 ${sin_20}"
  ),
  Limit(
   effort= "50",
   velocity= "4.0",
   lower= "-0.5236",
   upper= "0.5235"
  ),
  Dynamics(
   damping= "3.0",
   friction= "0"
  ),
  name= "WaistLat",
  type= "revolute"
 ),
 Joint(
  Parent(
   link= "DWL"
  ),
  Child(
   link= "DWS"
  ),
  Origin(
   rpy= "0 0 0",
   xyz= "0 0 0"
  ),
  Axis(
   xyz= "0 1 0"
  ),
  Limit(
   effort= "50",
   velocity= "4.0",
   lower= "-0.3491",
   upper= "0.8727"
  ),
  Dynamics(
   damping= "3.0",
   friction= "0"
  ),
  name= "WaistSag",
  type= "revolute"
 ),
 Joint(
  Parent(
   link= "DWS"
  ),
  Child(
   link= "DWYTorso"
  ),
  Origin(
   rpy= "0 0 0",
   xyz= "0 0 0.04749999"
  ),
  Axis(
   xyz= "0 0 1"
  ),
  Limit(
   effort= "50",
   velocity= "4.0",
   lower= "-1.3963",
   upper= "1.3962"
  ),
  Dynamics(
   damping= "3.0",
   friction= "0"
  ),
  name= "WaistYaw",
  type= "revolute"
 )
)
 
