"""
Copied from https://github.com/EnricoMingo/iit-coman-ros-pkg
"""


from odio_urdf import *

import torso
import legs
import foot_reference_frame
import arms

def coman_base(GAZEBO_COMAN_USES_FOREARMS):
    return Group(
             Xacroproperty(
              value= "3.14159265359",
              name= "PI"
             ),
             Link(
              name= "base_link"
             ),
             Link(
              Inertial(
               Origin(
                rpy= "0.0 0.0 0.0",
                xyz= "-0.026391145 -5.8216364E-4 0.052632312"
               ),
               Mass(
                value= "1.8008695"
               ),
               Inertia(
                iyy= "0.006241636",
                iyz= "1.7225949E-5",
                ixz= "0.0016920543",
                ixx= "0.0051032982",
                izz= "0.0024517762",
                ixy= "-5.7170981E-5"
               )
              ),
              Visual(
               Origin(
                rpy= "0 0 ${PI}",
                xyz= "0 0 -0.52"
               ),
               Material(
                name= "dark_grey"
               ),
               Geometry(
                Mesh(
                 scale= "0.03937 0.03937 0.03937",
                 filename= "package://coman_urdf/meshes/Waist.STL"
                ),
                name= "Waist_visual"
               )
              ),
              Collision(
               Origin(
                rpy= "0 0 ${PI}",
                xyz= "0 0 -0.52"
               ),
               Geometry(
                Mesh(
                 scale= "0.03937 0.03937 0.03937",
                 filename= "package://coman_urdf/meshes/simple/Waist.STL"
                ),
                name= "Waist_collision"
               )
              ),
              name= "Waist"
             ),
             Joint(
              Parent(
               link= "base_link"
              ),
              Child(
               link= "Waist"
              ),
              Origin(
               rpy= "0 0 0",
               xyz= "0 0 0"
              ),
              name= "base_joint",
              type= "fixed"
             ),
             Xacroinclude(
              filename= "$(find coman_urdf)/urdf/parts/torso.urdf.xacro"
             ),
             #Include torso
             torso.torso,
             
             Link(
              name= "l_ankle"
             ),
             Link(
              name= "r_ankle"
             ),
             Link(
              name= "l_sole"
             ),
             Link(
              name= "r_sole"
             ),
             Link(
              name= "l_toe"
             ),
             Link(
              name= "r_toe"
             ),
             Xacroinclude(
              filename= "$(find coman_urdf)/urdf/parts/legs.urdf.xacro"
             ),
             legs.legs(GAZEBO_COMAN_USES_FOREARMS),
             Joint(
              Parent(
               link= "LFoot"
              ),
              Child(
               link= "l_ankle"
              ),
              Origin(
               rpy= "0 0 0",
               xyz= "0 0 0"
              ),
              name= "l_ankle_joint",
              type= "fixed"
             ),
             Joint(
              Parent(
               link= "RFoot"
              ),
              Child(
               link= "r_ankle"
              ),
              Origin(
               rpy= "0 0 0",
               xyz= "0 0 0"
              ),
              name= "r_ankle_joint",
              type= "fixed"
             ),
             Joint(
              Parent(
               link= "LFoot"
              ),
              Child(
               link= "l_sole"
              ),
              Origin(
               rpy= "0 0 0",
               xyz= "0 0 -0.09"
              ),
              name= "l_sole_joint",
              type= "fixed"
             ),
             Joint(
              Parent(
               link= "RFoot"
              ),
              Child(
               link= "r_sole"
              ),
              Origin(
               rpy= "0 0 0",
               xyz= "0 0 -0.09"
              ),
              name= "r_sole_joint",
              type= "fixed"
             ),
             Joint(
              Parent(
               link= "l_sole"
              ),
              Child(
               link= "l_toe"
              ),
              Origin(
               rpy= "0 0 0",
               xyz= "0.13 0 0"
              ),
              name= "l_toe_joint",
              type= "fixed"
             ),
             Joint(
              Parent(
               link= "r_sole"
              ),
              Child(
               link= "r_toe"
              ),
              Origin(
               rpy= "0 0 0",
               xyz= "0.13 0 0"
              ),
              name= "r_toe_joint",
              type= "fixed"
             ),
             Xacroinclude(
              filename= "$(find coman_urdf)/urdf/parts/foot_reference_frame.urdf.xacro"
             ),
             foot_reference_frame.foot_reference_frame,
             Xacroinclude(
              filename= "$(find coman_urdf)/urdf/parts/arms.urdf.xacro"
             ),
             arms.arms
             
            )
