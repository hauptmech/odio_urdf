"""
Copied from https://github.com/EnricoMingo/iit-coman-ros-pkg
"""

from odio_urdf import *
imu = Group(
 Xacroproperty(
  value= "3.14159265359",
  name= "PI"
 ),
 Link(
  Inertial(
   Mass(
    value= "0.01"
   ),
   Origin(
    xyz= "0 0 0"
   ),
   Inertia
    izz= "1.0E-6",
    ixy= "0",
    ixz= "0",
    ixx= "1.0E-6",
    iyy= "1.0E-6",
    iyz= "0"
   )
  ),
  Visual(
   Origin(
    xyz= "0 0 0",
    rpy= "0 0 0"
   ),
   Geometry(
    Box(
     size= "0.01 0.01 0.01"
    )
   )
  ),
  name= "imu_link"
 ),
 Joint(
  Parent(
   link= "Waist"
  ),
  Child(
   link= "imu_link"
  ),
  Origin(
   xyz= "-0.072 -0.0068 0.044",
   rpy= "0 0 0"
  ),
  type= "fixed",
  name= "imu_joint"
 )
)
