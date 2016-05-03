"""
Copied from https://github.com/EnricoMingo/iit-coman-ros-pkg
"""


from odio_urdf import *

no_forearms = Group(
 Xacroproperty(
  name= "Wrj1_to_FT",
  value= "0.0568"
 ),
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
 Link(
  Inertial(
   Origin(
    xyz= "0 0 -0.085",
    rpy= "0 0 0"
   ),
   Mass(
    value= "0.263"
   ),
   Inertia
    ixx= "6.913E-4",
    ixy= "0.0",
    iyy= "6.913E-4",
    ixz= "0.0",
    izz= "4.0425E-5",
    iyz= "0.0"
   )
  ),
  Visual(
   Origin(
    xyz= "-0.0055 -0.1558 -0.6175",
    rpy= "0 0 ${PI}"
   ),
   Material(
    name= "dark_grey"
   ),
   Geometry(
    Mesh(
     scale= "${SF} ${SF} ${SF}",
     filename= "package://coman_urdf/meshes/ForearmOld.STL"
    ),
    name= "LForearm_visual"
   )
  ),
  Collision(
   Origin(
    xyz= "-0.0055 -0.1558 -0.6175",
    rpy= "0 0 ${PI}"
   ),
   Geometry(
    Mesh(
     scale= "${SF} ${SF} ${SF}",
     filename= "package://coman_urdf/meshes/simple/ForearmOld.STL"
    ),
    name= "LForearm_collision"
   )
  ),
  name= "LForearm"
 ),
 Link(
  Inertial(
   Origin(
    xyz= "0 0 -0.085",
    rpy= "0 0 0"
   ),
   Mass(
    value= "0.263"
   ),
   Inertia
    ixx= "6.913E-4",
    ixy= "0.0",
    iyy= "6.913E-4",
    ixz= "0.0",
    izz= "4.0425E-5",
    iyz= "0.0"
   )
  ),
  Visual(
   Origin(
    xyz= "-0.0055 -0.1558 -0.6175",
    rpy= "0 0 ${PI}"
   ),
   Material(
    name= "dark_grey"
   ),
   Geometry(
    Mesh(
     scale= "${SF} ${SF} ${SF}",
     filename= "package://coman_urdf/meshes/ForearmOld.STL"
    ),
    name= "RForearm_visual"
   )
  ),
  Collision(
   Origin(
    xyz= "-0.0055 -0.1558 -0.6175",
    rpy= "0 0 ${PI}"
   ),
   Geometry(
    Mesh(
     scale= "${SF} ${SF} ${SF}",
     filename= "package://coman_urdf/meshes/simple/ForearmOld.STL"
    ),
    name= "RForearm_collision"
   )
  ),
  name= "RForearm"
 ),
 Joint(
  Parent(
   link= "LElb"
  ),
  Child(
   link= "LForearm"
  ),
  Origin(
   xyz= "-0.015 0.0 -0.05",
   rpy= "0 0 0"
  ),
  name= "LForearmPlate",
  type= "fixed"
 ),
 Joint(
  Parent(
   link= "LElb"
  ),
  Child(
   link= "l_wrist"
  ),
  Origin(
   xyz= "-0.015 0 -0.22",
   rpy= "0 0 0"
  ),
  name= "l_wrist_joint",
  type= "fixed"
 ),
 Joint(
  Parent(
   link= "RElb"
  ),
  Child(
   link= "RForearm"
  ),
  Origin(
   xyz= "-0.015 0.0 -0.05",
   rpy= "0 0 0"
  ),
  name= "RForearmPlate",
  type= "fixed"
 ),
 Joint(
  Parent(
   link= "RElb"
  ),
  Child(
   link= "r_wrist"
  ),
  Origin(
   xyz= "-0.015 0 -0.22",
   rpy= "0 0 0"
  ),
  name= "r_wrist_joint",
  type= "fixed"
 )
)
