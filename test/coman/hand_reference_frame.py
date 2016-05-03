"""
Copied from https://github.com/EnricoMingo/iit-coman-ros-pkg
"""


from odio_urdf import *

frame_x = 0.04
frame_z = 0.03

def reference_frame_hand(parent_name,name,x,z):
    ret = Group()
    
    ret(Link(name+"_link"))
    ret(Joint(
            name+"_joint",
            Origin(xyz="{x} 0 {z}".format(x=x,z=z), rpy="0 0 0"),
            Parent(link=parent_name),
            Child(link=name+"_link"),
            type="fixed"))
    return ret
    
def references_frame_hand(parent_name, name):
    return Group(
        reference_frame_hand(parent_name, name+"_upper_right", frame_x, -frame_z),
        reference_frame_hand(parent_name, name+"_upper_left", frame_x, frame_z),
        reference_frame_hand(parent_name, name+"_lower_right", -frame_x, -frame_z),
        reference_frame_hand(parent_name, name+"_lower_left", -frame_x, frame_z),
    )

hand_reference_frame = Group(references_frame_hand("LSoftHand","l_hand"),
                             references_frame_hand("RSoftHand","r_hand"),)
