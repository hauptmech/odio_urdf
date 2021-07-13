"""
Copied from https://github.com/EnricoMingo/iit-coman-ros-pkg
"""


from odio_urdf import *

xtion = Group(
 Xacroproperty(
  value= "3.14159265359",
  name= "PI"
 ),
 Link(
  Inertial(
   Origin(
    rpy= "0 0 0",
    xyz= "0.047 0.0 0.40"
   ),
   Mass(
    value= "0.39"
   ),
   Inertia(
    ixx= "0.01",
    ixy= "3.34E-7",
    ixz= "-2.66E-4",
    iyz= "1.97E-6",
    iyy= "0.009",
    izz= "5.1E-4"
   )
  ),
  Visual(
   Origin(
    rpy= "0 0 ${PI}",
    xyz= "-0.020281504 0.0 -0.68662053"
   ),
   Geometry(
    Mesh(
     scale= "0.03937 0.03937 0.03937",
     filename= "package://coman_urdf/meshes/XtionBase.STL"
    ),
    name= "Xtion_body_visual"
   )
  ),
  Collision(
   Origin(
    rpy= "0 0 ${PI}",
    xyz= "-0.020281504 0.0 -0.68662053"
   ),
   Geometry(
    Mesh(
     scale= "0.03937 0.03937 0.03937",
     filename= "package://coman_urdf/meshes/simple/XtionBase.STL"
    ),
    name= "Xtion_body_collision"
   )
  ),
  name= "Xtion_body"
 ),
 Link(
  Inertial(
   Origin(
    rpy= "0 0 0",
    xyz= "0.0 0.0 0.0225"
   ),
   Mass(
    value= "0.2"
   ),
   Inertia(
    ixx= "0.00053",
    ixy= "0.0",
    ixz= "0.0",
    iyz= "0.0",
    iyy= "0.00008",
    izz= "0.00053"
   )
  ),
  Visual(
   Origin(
    rpy= "0 0 ${PI}",
    xyz= "-0.0915 0.0 -1.2778"
   ),
   Geometry(
    Mesh(
     scale= "0.001 0.001 0.001",
     filename= "package://coman_urdf/meshes/XtionCamBody.STL"
    ),
    name= "Xtion_cam_body_visual"
   )
  ),
  Collision(
   Origin(
    rpy= "0 0 ${PI}",
    xyz= "-0.0915 0.0 -1.2778"
   ),
   Geometry(
    Mesh(
     scale= "0.001 0.001 0.001",
     filename= "package://coman_urdf/meshes/simple/XtionCamBody.STL"
    ),
    name= "Xtion_cam_body_collision"
   )
  ),
  name= "Xtion_cam_body"
 ),
 Joint(
  Parent(
   link= "DWYTorso"
  ),
  Child(
   link= "Xtion_body"
  ),
  Origin(
   rpy= "0 0 0",
   xyz= "0 0 0"
  ),
  type= "fixed",
  name= "Xtion_body_joint"
 ),
 Joint(
  Parent(
   link= "Xtion_body"
  ),
  Child(
   link= "Xtion_cam_body"
  ),
  Origin(
   rpy= "0 0 0",
   xyz= "0.071 0 0.591"
  ),
  type= "fixed",
  name= "Xtion_cam_body_joint"
 ),
 Joint(
  Parent(
   link= "Xtion_cam_body"
  ),
  Child(
   link= "gaze"
  ),
  Origin(
   rpy= "0 0 0",
   xyz= "0.015 0 0.022"
  ),
  type= "fixed",
  name= "gaze_joint"
 )
)
 
