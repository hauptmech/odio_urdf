"""
Copied from https://github.com/EnricoMingo/iit-coman-ros-pkg
"""

from odio_urdf import *
forearms = Group(
 Xacroproperty(name= "Wrj1_to_FT",value= "0.0568"),
 Link(
  Inertial(
   Origin(xyz= "0 0 ${-0.085 + Wrj1_to_FT}",rpy= "0 0 0"),
   Mass(value= "0.93351655"),
   Inertia(
    izz= "0.001",
    iyy= "0.001",
    ixx= "0.001",
    iyz= "0.0",
    ixy= "0.0",
    ixz= "0.0"
    ),
   ),
  Visual(
   Origin(xyz= "0 0 ${0.015 + Wrj1_to_FT}",rpy= "3.14159265359 0 1.570796326795"),
   Material(name= "dark_grey"),
   Geometry(
    Mesh(scale= "0.1 0.1 0.1",filename= "package://coman_urdf/meshes/Forearm0.STL"),
    name= "LForearm_visual"),
   ),
  Collision(
   Origin(xyz= "0 0 ${0.015 + Wrj1_to_FT}",rpy= "0 3.14159265359 1.570796326795"),
   Geometry(
    Mesh(scale= "1.0 1.0 1.0",filename= "package://coman_urdf/meshes/simple/Forearm0.STL"),
    name= "LForearm_collision"),
   ),
  name= "LForearm"),
 Link(
  Inertial(
   Origin(xyz= "0 0 0",rpy= "0 0 0"),
   Mass(value= "0.26070556"),
   Inertia(
    izz= "5.213E-5",
    iyy= "0.000132",
    ixx= "0.000132",
    iyz= "0",
    ixy= "0",
    ixz= "0"
    ),
   ),
  Visual(
   Origin(xyz= "0.025 0 0",rpy= "0 1.570796326795 3.14159265359"),
   Material(name= "grey"),
   Geometry(
    Mesh(scale= "0.001 0.001 0.001",filename= "package://coman_urdf/meshes/Forearm1.STL"),
    name= "LWrMot2_visual"),
   ),
  Collision(
   Origin(xyz= "0.025 0 0",rpy= "0 1.570796326795 3.14159265359"),
   Geometry(
    Mesh(scale= "0.001 0.001 0.001",filename= "package://coman_urdf/meshes/simple/Forearm1.STL"),
    name= "LWrMot2_collision"),
   ),
  name= "LWrMot2"),
 Link(
  Inertial(
   Origin(xyz= "0 0 0",rpy= "0 0 0"),
   Mass(value= "0.054007518"),
   Inertia(
    izz= "2.16E-5",
    iyy= "2.16E-5",
    ixx= "2.16E-5",
    iyz= "0",
    ixy= "0",
    ixz= "0"
    ),
   ),
  Visual(
   Origin(xyz= "0.025 -0.012 -0.02",rpy= "0 3.14159265359 1.570796326795"),
   Material(name= "grey"),
   Geometry(
    Mesh(scale= "0.001 0.001 0.001",filename= "package://coman_urdf/meshes/Forearm2.STL"),
    name= "LWrMot3_visual"),
   ),
  Collision(
   Origin(xyz= "0.025 -0.012 -0.02",rpy= "0 3.14159265359 1.570796326795"),
   Geometry(
    Mesh(scale= "0.001 0.001 0.001",filename= "package://coman_urdf/meshes/simple/Forearm2.STL"),
    name= "LWrMot3_collision"),
   ),
  name= "LWrMot3"),
 Link(
  Inertial(
   Origin(xyz= "0 0 ${-0.085 + Wrj1_to_FT}",rpy= "0 0 0"),
   Mass(value= "0.93351655"),
   Inertia(
    izz= "0.001",
    iyy= "0.001",
    ixx= "0.001",
    iyz= "0.0",
    ixy= "0.0",
    ixz= "0.0"
    ),
   ),
  Visual(
   Origin(xyz= "0 0 ${0.015 + Wrj1_to_FT}",rpy= "3.14159265359 0 1.570796326795"),
   Material(name= "dark_grey"),
   Geometry(
    Mesh(scale= "0.1 0.1 0.1",filename= "package://coman_urdf/meshes/Forearm0.STL"),
    name= "RForearm_visual"),
   ),
  Collision(
   Origin(xyz= "0 0 ${0.015 + Wrj1_to_FT}",rpy= "0 3.14159265359 1.570796326795"),
   Geometry(
    Mesh(scale= "1.0 1.0 1.0",filename= "package://coman_urdf/meshes/simple/Forearm0.STL"),
    name= "RForearm_collision"),
   ),
  name= "RForearm"),
 Link(
  Inertial(
   Origin(xyz= "0 0 0",rpy= "0 0 0"),
   Mass(value= "0.26070556"),
   Inertia(
    izz= "5.213E-5",
    iyy= "0.000132",
    ixx= "0.000132",
    iyz= "0",
    ixy= "0",
    ixz= "0"
    ),
   ),
  Visual(
   Origin(xyz= "0.025 0 0",rpy= "0 1.570796326795 3.14159265359"),
   Material(name= "grey"),
   Geometry(
    Mesh(scale= "0.001 0.001 0.001",filename= "package://coman_urdf/meshes/Forearm1.STL"),
    name= "RWrMot2_visual"),
   ),
  Collision(
   Origin(xyz= "0.025 0 0",rpy= "0 1.570796326795 3.14159265359"),
   Geometry(
    Mesh(scale= "0.001 0.001 0.001",filename= "package://coman_urdf/meshes/simple/Forearm1.STL"),
    name= "RWrMot2_collision"),
   ),
  name= "RWrMot2"),
 Link(
  Inertial(
   Origin(xyz= "0 0 0",rpy= "0 0 0"),
   Mass(value= "0.054007518"),
   Inertia(
    izz= "2.16E-5",
    iyy= "2.16E-5",
    ixx= "2.16E-5",
    iyz= "0",
    ixy= "0",
    ixz= "0"
    ),
   ),
  Visual(
   Origin(xyz= "0.025 -0.012 -0.02",rpy= "0 3.14159265359 1.570796326795"),
   Material(name= "grey"),
   Geometry(
    Mesh(scale= "0.001 0.001 0.001",filename= "package://coman_urdf/meshes/Forearm2.STL"),
    name= "RWrMot3_visual"),
   ),
  Collision(
   Origin(xyz= "0.025 -0.012 -0.02",rpy= "0 3.14159265359 1.570796326795"),
   Geometry(
    Mesh(scale= "0.001 0.001 0.001",filename= "package://coman_urdf/meshes/simple/Forearm2.STL"),
    name= "RWrMot3_collision"),
   ),
  name= "RWrMot3"),
 Joint(
  Parent(link= "LElb"),
  Child(link= "LForearm"),
  Origin(xyz= "-0.015 0.0 ${-0.051 - Wrj1_to_FT}",rpy= "0 0 0"),
  Axis(xyz= "0 0 1"),
  Limit(
   upper= "1.5708",
   lower= "-1.5708",
   effort= "5",
   velocity= "4.0"
   ),
  Dynamics(damping= "0.03",friction= "0"),
  name= "LForearmPlate",type= "revolute"),
 Joint(
  Parent(link= "LForearm"),
  Child(link= "LWrMot2"),
  Origin(xyz= "0 0 ${-0.14368 + Wrj1_to_FT}",rpy= "0 0 0"),
  Axis(xyz= "0 1 0"),
  Limit(
   upper= "0.524",
   lower= "-0.524",
   effort= "5",
   velocity= "4.0"
   ),
  Dynamics(damping= "0.03",friction= "0"),
  name= "LWrj1",type= "revolute"),
 Joint(
  Parent(link= "LWrMot2"),
  Child(link= "LWrMot3"),
  Origin(xyz= "0 0 0.0",rpy= "0 0 0"),
  Axis(xyz= "1 0 0"),
  Limit(
   upper= "1.395",
   lower= "-0.785375",
   effort= "5",
   velocity= "4.0"
   ),
  Dynamics(damping= "0.03",friction= "0"),
  name= "LWrj2",type= "revolute"),
 Joint(
  Parent(link= "LWrMot3"),
  Child(link= "l_wrist"),
  Origin(xyz= "0 0 0",rpy= "0 0 0"),
  name= "l_wrist_joint",type= "fixed"),
 Joint(
  Parent(link= "RElb"),
  Child(link= "RForearm"),
  Origin(xyz= "-0.015 0.0 ${-0.051 - Wrj1_to_FT}",rpy= "0 0 0"),
  Axis(xyz= "0 0 1"),
  Limit(
   upper= "1.5708",
   lower= "-1.5708",
   effort= "5",
   velocity= "4.0"
   ),
  Dynamics(damping= "0.03",friction= "0"),
  name= "RForearmPlate",type= "revolute"),
 Joint(
  Parent(link= "RForearm"),
  Child(link= "RWrMot2"),
  Origin(xyz= "0 0 ${-0.14368 + Wrj1_to_FT}",rpy= "0 0 0"),
  Axis(xyz= "0 1 0"),
  Limit(
   upper= "0.524",
   lower= "-0.524",
   effort= "5",
   velocity= "4.0"
   ),
  Dynamics(damping= "0.03",friction= "0"),
  name= "RWrj1",type= "revolute"),
 Joint(
  Parent(link= "RWrMot2"),
  Child(link= "RWrMot3"),
  Origin(xyz= "0 0 0.0",rpy= "0 0 0"),
  Axis(xyz= "1 0 0"),
  Limit(
   upper= "0.785375",
   lower= "-1.395",
   effort= "5",
   velocity= "4.0"
   ),
  Dynamics(damping= "0.03",friction= "0"),
  name= "RWrj2",type= "revolute"),
 Joint(
  Parent(link= "RWrMot3"),
  Child(link= "r_wrist"),
  Origin(xyz= "0 0 0",rpy= "0 0 0"),
  name= "r_wrist_joint",type= "fixed"),
 )
if __name__ == "__main__":
    #print(forearms)
    pass
