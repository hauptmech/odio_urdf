"""
Copied from https://github.com/EnricoMingo/iit-coman-ros-pkg
"""

from odio_urdf import *

arms = Group(
 Xacroproperty(value= "3.14159265359",name= "PI"),
 Xacroproperty(value= "0.03937",name= "SF"),
 Link(
  Inertial(
   Origin(xyz= "0.0099500565 -0.038682024 1.6446924E-4",rpy= "0 0 0"),
   Mass(value= "0.56782202"),
   Inertia(
    ixz= "-3.0037676E-6",
    ixy= "1.9035768E-4",
    iyy= "6.3399921E-4",
    ixx= "7.8337456E-4",
    iyz= "4.3840774E-6",
    izz= "0.001008054"
    ),
   ),
  Visual(
   Origin(xyz= "-0.005305 0.0825 -0.844329",rpy= "0 0 ${PI}"),
   Material(name= "dark_grey"),
   Geometry(
    Mesh(filename= "package://coman_urdf/meshes/Arm0.STL",scale= "${SF} ${SF} ${SF}"),
    name= "RShp_visual"),
   ),
  Collision(
   Origin(xyz= "-0.005305 0.0825 -0.844329",rpy= "0 0 ${PI}"),
   Geometry(
    Mesh(filename= "package://coman_urdf/meshes/simple/Arm0.STL",scale= "${SF} ${SF} ${SF}"),
    name= "RShp_collision"),
   ),
  name= "RShp"),
 Link(
  Inertial(
   Origin(xyz= "-0.0038936743 2.2022151E-6 -0.0048616005",rpy= "0 0 0"),
   Mass(value= "0.77683752"),
   Inertia(
    ixz= "9.2521185E-6",
    ixy= "-2.4111086E-7",
    iyy= "4.3089204E-4",
    ixx= "4.5812904E-4",
    iyz= "-4.7216950E-7",
    izz= "3.4174855E-4"
    ),
   ),
  Visual(
   Origin(xyz= "-0.005305 0.1558 -0.844329",rpy= "0 0 ${PI}"),
   Material(name= "dark_grey"),
   Geometry(
    Mesh(filename= "package://coman_urdf/meshes/Arm1.STL",scale= "${SF} ${SF} ${SF}"),
    name= "RShr_visual"),
   ),
  Collision(
   Origin(xyz= "-0.005305 0.1558 -0.844329",rpy= "0 0 ${PI}"),
   Geometry(
    Mesh(filename= "package://coman_urdf/meshes/simple/Arm1.STL",scale= "${SF} ${SF} ${SF}"),
    name= "RShr_collision"),
   ),
  name= "RShr"),
 Link(
  Inertial(
   Origin(xyz= "0.0022714213 -0.0071091517 -0.057455221",rpy= "0 0 0"),
   Mass(value= "1.0462304"),
   Inertia(
    ixz= "3.0222291E-4",
    ixy= "6.6702837E-5",
    iyy= "0.0029181573",
    ixx= "0.0030934574",
    iyz= "-5.2663661E-4",
    izz= "8.0830389E-4"
    ),
   ),
  Visual(
   Origin(xyz= "-0.005305 0.1558 -0.79952053",rpy= "0 0 ${PI}"),
   Material(name= "dark_grey"),
   Geometry(
    Mesh(filename= "package://coman_urdf/meshes/Arm2.STL",scale= "${SF} ${SF} ${SF}"),
    name= "RShy_visual"),
   ),
  Collision(
   Origin(xyz= "-0.005305 0.1558 -0.79952053",rpy= "0 0 ${PI}"),
   Geometry(
    Mesh(filename= "package://coman_urdf/meshes/simple/Arm2.STL",scale= "${SF} ${SF} ${SF}"),
    name= "RShy_collision"),
   ),
  name= "RShy"),
 Link(
  Inertial(
   Origin(xyz= "-6.5553403E-4 -9.3464748E-4 -9.3101289E-4",rpy= "0 0 0"),
   Mass(value= "0.63306933"),
   Inertia(
    ixz= "-9.8007285E-6",
    ixy= "-2.6376470E-7",
    iyy= "2.7781302E-4",
    ixx= "2.2599075E-4",
    iyz= "-2.0435288E-6",
    izz= "2.1878992E-4"
    ),
   ),
  Visual(
   Origin(xyz= "0 0 0",rpy= "-1.570796326795 1.570796326795 0"),
   Material(name= "dark_grey"),
   Geometry(
    Mesh(filename= "package://coman_urdf/meshes/Elbow.STL",scale= "1.0 1.0 1.0"),
    name= "RElb_visual"),
   ),
  Collision(
   Origin(xyz= "0 0 0",rpy= "-1.570796326795 1.570796326795 0"),
   Geometry(
    Mesh(filename= "package://coman_urdf/meshes/simple/Elbow.STL",scale= "1.0 1.0 1.0"),
    name= "RElb_collision"),
   ),
  name= "RElb"),
 Link(
  Inertial(
   Origin(xyz= "0.0099500565 0.038682024 1.6446924E-4",rpy= "0 0 0"),
   Mass(value= "0.56782202"),
   Inertia(
    ixz= "-3.0037676E-6",
    ixy= "-1.9035768E-4",
    iyy= "6.3399921E-4",
    ixx= "7.8337456E-4",
    iyz= "-4.3840774E-6",
    izz= "0.001008054"
    ),
   ),
  Visual(
   Origin(xyz= "-0.005305 -0.0825 -0.844329",rpy= "0 0 ${PI}"),
   Material(name= "dark_grey"),
   Geometry(
    Mesh(filename= "package://coman_urdf/meshes/Arm0.STL",scale= "${SF} -${SF} ${SF}"),
    name= "LShp_visual"),
   ),
  Collision(
   Origin(xyz= "-0.005305 -0.0825 -0.844329",rpy= "0 0 ${PI}"),
   Geometry(
    Mesh(filename= "package://coman_urdf/meshes/simple/Arm0.STL",scale= "${SF} -${SF} ${SF}"),
    name= "LShp_collision"),
   ),
  name= "LShp"),
 Link(
  Inertial(
   Origin(xyz= "-0.0038936743 -2.2022151E-6 -0.0048616005",rpy= "0 0 0"),
   Mass(value= "0.77683752"),
   Inertia(
    ixz= "9.2521185E-6",
    ixy= "2.4111086E-7",
    iyy= "4.3089204E-4",
    ixx= "4.5812904E-4",
    iyz= "4.721695E-7",
    izz= "3.4174855E-4"
    ),
   ),
  Visual(
   Origin(xyz= "-0.005305 -0.1558 -0.844329",rpy= "0 0 ${PI}"),
   Material(name= "dark_grey"),
   Geometry(
    Mesh(filename= "package://coman_urdf/meshes/Arm1.STL",scale= "${SF} -${SF} ${SF}"),
    name= "LShr_visual"),
   ),
  Collision(
   Origin(xyz= "-0.005305 -0.1558 -0.844329",rpy= "0 0 ${PI}"),
   Geometry(
    Mesh(filename= "package://coman_urdf/meshes/simple/Arm1.STL",scale= "${SF} -${SF} ${SF}"),
    name= "LShr_collision"),
   ),
  name= "LShr"),
 Link(
  Inertial(
   Origin(xyz= "0.0022714213 0.0071091517 -0.057455221",rpy= "0 0 0"),
   Mass(value= "1.0462304"),
   Inertia(
    ixz= "3.0222291E-4",
    ixy= "-6.6702837E-5",
    iyy= "0.0029181573",
    ixx= "0.0030934574",
    iyz= "5.2663661E-4",
    izz= "8.0830389E-4"
    ),
   ),
  Visual(
   Origin(xyz= "-0.005305 -0.1558 -0.79952053",rpy= "0 0 ${PI}"),
   Material(name= "dark_grey"),
   Geometry(
    Mesh(filename= "package://coman_urdf/meshes/Arm2.STL",scale= "${SF} -${SF} ${SF}"),
    name= "LShy_visual"),
   ),
  Collision(
   Origin(xyz= "-0.005305 -0.1558 -0.79952053",rpy= "0 0 ${PI}"),
   Geometry(
    Mesh(filename= "package://coman_urdf/meshes/simple/Arm2.STL",scale= "${SF} -${SF} ${SF}"),
    name= "LShy_collision"),
   ),
  name= "LShy"),
 Link(
  Inertial(
   Origin(xyz= "-6.5553403E-4 9.3464748E-4 -9.3101289E-4",rpy= "0 0 0"),
   Mass(value= "0.63306933"),
   Inertia(
    ixz= "-9.8007285E-6",
    ixy= "2.6376470E-7",
    iyy= "2.7781302E-4",
    ixx= "2.2599075E-4",
    iyz= "2.0435288E-6",
    izz= "2.1878992E-4"
    ),
   ),
  Visual(
   Origin(xyz= "0 0 0",rpy= "-1.570796326795 1.570796326795 0"),
   Material(name= "dark_grey"),
   Geometry(
    Mesh(filename= "package://coman_urdf/meshes/Elbow.STL",scale= "1.0 1.0 1.0"),
    name= "LElb_visual"),
   ),
  Collision(
   Origin(xyz= "0 0 0",rpy= "-1.570796326795 1.570796326795 0"),
   Geometry(
    Mesh(filename= "package://coman_urdf/meshes/simple/Elbow.STL",scale= "1.0 1.0 1.0"),
    name= "LElb_collision"),
   ),
  name= "LElb"),
 Joint(
  Parent(link= "DWYTorso"),
  Child(link= "RShp"),
  Origin(xyz= "-0.014976503999999998 -0.0825 0.15770847",rpy= "0 0 0"),
  Axis(xyz= "0 1 0"),
  Limit(
   effort= "50",
   upper= "1.6581",
   velocity= "4.0",
   lower= "-3.4034"
   ),
  Dynamics(friction= "0",damping= "3.0"),
  type= "revolute",name= "RShSag"),
 Joint(
  Parent(link= "RShp"),
  Child(link= "RShr"),
  Origin(xyz= "0.0 -0.07329999999999999 0.0",rpy= "0 0 0"),
  Axis(xyz= "1 0 0"),
  Limit(
   effort= "50",
   upper= "0.31415",
   velocity= "4.0",
   lower= "-2.094"
   ),
  Dynamics(friction= "0",damping= "3.0"),
  type= "revolute",name= "RShLat"),
 Joint(
  Parent(link= "RShr"),
  Child(link= "RShy"),
  Origin(xyz= "0.0 0.0 -0.04480846999999999",rpy= "0 0 0"),
  Axis(xyz= "0 0 1"),
  Limit(
   effort= "50",
   upper= "1.5708",
   velocity= "4.0",
   lower= "-1.5708"
   ),
  Dynamics(friction= "0",damping= "3.0"),
  type= "revolute",name= "RShYaw"),
 Joint(
  Parent(link= "RShy"),
  Child(link= "RElb"),
  Origin(xyz= "0.015 0.0 -0.13519152999999998",rpy= "0 0 0"),
  Axis(xyz= "0 1 0"),
  Limit(
   effort= "50",
   upper= "0.0",
   velocity= "4.0",
   lower= "-2.3562"
   ),
  Dynamics(friction= "0",damping= "3.0"),
  type= "revolute",name= "RElbj"),
 Joint(
  Parent(link= "DWYTorso"),
  Child(link= "LShp"),
  Origin(xyz= "-0.014976503999999998 0.0825 0.15770847",rpy= "0 0 0"),
  Axis(xyz= "0 1 0"),
  Limit(
   effort= "50",
   upper= "1.6581",
   velocity= "4.0",
   lower= "-3.4034"
   ),
  Dynamics(friction= "0",damping= "3.0"),
  type= "revolute",name= "LShSag"),
 Joint(
  Parent(link= "LShp"),
  Child(link= "LShr"),
  Origin(xyz= "0.0 0.07329999999999999 0.0",rpy= "0 0 0"),
  Axis(xyz= "1 0 0"),
  Limit(
   effort= "50",
   upper= "2.094",
   velocity= "4.0",
   lower= "-0.31415"
   ),
  Dynamics(friction= "0",damping= "3.0"),
  type= "revolute",name= "LShLat"),
 Joint(
  Parent(link= "LShr"),
  Child(link= "LShy"),
  Origin(xyz= "0.0 0.0 -0.04480846999999999",rpy= "0 0 0"),
  Axis(xyz= "0 0 1"),
  Limit(
   effort= "50",
   upper= "1.5708",
   velocity= "4.0",
   lower= "-1.5708"
   ),
  Dynamics(friction= "0",damping= "3.0"),
  type= "revolute",name= "LShYaw"),
 Joint(
  Parent(link= "LShy"),
  Child(link= "LElb"),
  Origin(xyz= "0.015 0.0 -0.13519152999999998",rpy= "0 0 0"),
  Axis(xyz= "0 1 0"),
  Limit(
   effort= "50",
   upper= "0.0",
   velocity= "4.0",
   lower= "-2.3562"
   ),
  Dynamics(friction= "0",damping= "3.0"),
  type= "revolute",name= "LElbj"),
 )
