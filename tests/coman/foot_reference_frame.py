"""
Copied from https://github.com/EnricoMingo/iit-coman-ros-pkg
"""

from odio_urdf import *

frame_x = 0.04
frame_y = 0.03

def reference_frame_foot(parent_name,name,x,y):
    ret = Group()
    
    ret(Link(name+"_link"))
    ret(Joint(
            name+"_joint",
            Origin(xyz="{x} {y} 0".format(x=x,y=y), rpy="0 0 0"),
            Parent(link=parent_name),
            Child(link=name+"_link"),
            type="fixed"))
    return ret
    
def references_frame_foot(parent_name, name):
    return Group(
        reference_frame_foot(parent_name, name+"_upper_right", 0.13, -0.05),
        reference_frame_foot(parent_name, name+"_upper_left", 0.13,   0.05),
        reference_frame_foot(parent_name, name+"_lower_right", -0.07, -0.05),
        reference_frame_foot(parent_name, name+"_lower_left", -0.07, 0.05),
    )

foot_reference_frame = Group(references_frame_foot("l_sole","l_foot"),
                             references_frame_foot("r_sole","r_foot"),)

