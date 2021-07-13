#!/usr/bin/python
"""
Copied from https://github.com/EnricoMingo/iit-coman-ros-pkg
"""

from odio_urdf import *


"""
  ROS urdf definition of the COMAN humanoid Robot by Istituto Italiano di Tecnologia
  
  Author: Enrico Mingo & Alessio Rocchi
  Inertial matrix has to be in CoM frame (URDF specs)
  Velocity and effort limits are fake!
"""


model_name = "IIT Coman w/ Softhand"
model_version = "0.1"
GAZEBO_COMAN_USES_ROUND_FEET = False
GAZEBO_COMAN_USES_FOREARMS = True
GAZEBO_COMAN_USES_SOFTHANDS = True


"""
1) COMAN classic without the staff to carry the sensor. 
      Torso frame is connected to gaze link through a gaze_joint "fixed"
2) COMAN with staff and xtion sensor. Torso frame is connected to a xtion_staff_link through
      a xtion_staff_joint "fixed". Xtion_staff_link is then connected to gaze_link through gaze_joint "fixed". 
"""
GAZEBO_COMAN_USES_XTION = False

grey =      Material(Color(rgba="0.5 0.5 0.5 1"))
dark_grey = Material(Color(rgba="0.3 0.3 0.3 1"))
red =       Material(Color(rgba="1.0 0.0 0.0 1"))


########### Robot definition ###############
coman = Robot("coman",grey,dark_grey,red)

coman(Link("gaze"))

if GAZEBO_COMAN_USES_XTION:
    import xtion
    coman(xtion.xtion)
else:
    gaze_joint = Joint(
            Parent(link="torso"),
            Child(link="gaze"),
            Origin(xyz="0 0 0.1", rpy="0 0 0"),
            type = "fixed")
    
    coman(gaze_joint)


import coman_base

coman(coman_base.coman_base(GAZEBO_COMAN_USES_FOREARMS))
    
"""   
************ FOREARMS ************
This links are defined in order to be compliant with http://www.ros.org/reps/rep-0120.html#coordinate-frames
and to define the end effectors of the Robot

position and orientation of the arm regardless of the tool (grasping device for instance) attached to it
"""

coman(Link("l_wrist"), Link("r_wrist"))

if GAZEBO_COMAN_USES_FOREARMS:
    import forearms
    coman(forearms.forearms)
    coman(
        Link("l_arm_ft"),
        Link("r_arm_ft"),
         Joint(
          Parent(link= "LForearm"),
          Child(link= "l_arm_ft"),
          Origin(rpy= "0 0 0",xyz= "0 0 0"),
          name= "l_arm_ft_joint",
          type= "fixed"
         ),
         Joint(
          Parent(link= "RForearm"),
          Child(link= "r_arm_ft"),
          Origin(rpy= "0 0 0",xyz= "0 0 0"),
          name= "r_arm_ft_joint",
          type= "fixed"))
else:
    import no_forearms
    coman(no_forearms.no_forearms)

coman(
    Link("l_leg_ft"),
     Link("r_leg_ft"),
     Joint(
      Parent(link= "LFoot"),
      Child(link= "l_leg_ft"),
      Origin(xyz= "0 0 -0.065", rpy= "0 0 0"),
      name= "l_leg_ft_joint",
      type= "fixed"),
     Joint(
      Parent(link= "RFoot"),
      Child(link= "r_leg_ft"),
      Origin(xyz= "0 0 -0.065", rpy= "0 0 0"),
      name= "r_leg_ft_joint",
      type= "fixed")
)

if GAZEBO_COMAN_USES_FOREARMS:
    import soft_hand
    if GAZEBO_COMAN_USES_SOFTHANDS:
        coman(soft_hand.coman_does_not_use_soft_hand)
    else:
        coman(soft_hand.coman_uses_soft_hand)
     
    import hand_reference_frame
    coman(hand_reference_frame.hand_reference_frame)

    
    
print(coman)

