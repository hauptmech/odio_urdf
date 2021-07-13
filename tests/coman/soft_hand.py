"""
Copied from https://github.com/EnricoMingo/iit-coman-ros-pkg
"""

from odio_urdf import *

coman_uses_soft_hand = Group(
           Link(
           Inertial(
            Origin(
             rpy= "0 0 0",
             xyz= "0 0 0"
            ),
            Mass(
             value= "0.3"
            ),
            Inertia(
             iyz= "0",
             ixx= "0.001",
             izz= "0.001",
             ixy= "0",
             iyy= "0.001",
             ixz= "0"
            )
           ),
           Visual(
            Origin(
             rpy= "${-3.14159265359/2} 0 ${3.14159265359}",
             xyz= "0.007 0.01 -0.04"
            ),
            Material(
             name= "dark_grey"
            ),
            Geometry(
             Mesh(
              scale= "0.1 0.1 0.1",
              filename= "package://coman_urdf/meshes/SoftHandOpen.STL"
             ),
             name= "RSoftHand_visual"
            )
           ),
           Collision(
            Origin(
             rpy= "0 0 3.14159265359",
             xyz= "0 0.01 -0.04"
            ),
            Geometry(
             Mesh(
              scale= "1E-3 1E-3 1E-3",
              filename= "package://coman_urdf/meshes/simple/SoftHandOpen.STL"
             ),
             name= "RSoftHand_collision"
            )
           ),
           name= "RSoftHand"
          ),
          Link(
           Inertial(
            Origin(
             rpy= "0 0 0",
             xyz= "0 0 0"
            ),
            Mass(
             value= "0.3"
            ),
            Inertia(
             iyz= "0",
             ixx= "0.001",
             izz= "0.001",
             ixy= "0",
             iyy= "0.001",
             ixz= "0"
            )
           ),
           Visual(
            Origin(
             rpy= "${-3.14159265359/2} 0 0",
             xyz= "0.007 -0.01 -0.04"
            ),
            Material(
             name= "dark_grey"
            ),
            Geometry(
             Mesh(
              scale= "-0.1 0.1 0.1",
              filename= "package://coman_urdf/meshes/SoftHandOpen.STL"
             ),
             name= "LSoftHand_visual"
            )
           ),
           Collision(
            Origin(
             rpy= "0 0 0",
             xyz= "0.007 -0.01 -0.04"
            ),
            Geometry(
             Mesh(
              scale= "-1E-3 1E-3 1E-3",
              filename= "package://coman_urdf/meshes/simple/SoftHandOpen.STL"
             ),
             name= "LSoftHand_collision"
            )
           ),
           name= "LSoftHand"
          ),
          Joint(
           Parent(
            link= "RWrMot3"
           ),
           Child(
            link= "RSoftHand"
           ),
           Origin(
            rpy= "0 0 0",
            xyz= "0 0 -0.07"
           ),
           name= "r_handj",
           type= "fixed"
          ),
          Joint(
           Parent(
            link= "LWrMot3"
           ),
           Child(
            link= "LSoftHand"
           ),
           Origin(
            rpy= "0 0 0",
            xyz= "0 0 -0.07"
           ),
           name= "l_handj",
           type= "fixed"
          ),
          
        )

coman_does_not_use_soft_hand = Group(
              Link(
               Inertial(
            Origin(
             rpy= "0 0 0",
             xyz= "0 0 0"
            ),
            Mass(
             value= "0.3"
            ),
            Inertia(
             iyz= "0",
             ixx= "0.001",
             izz= "0.001",
             ixy= "0",
             iyy= "0.001",
             ixz= "0"
            )
               ),
               Visual(
            Origin(
             rpy= "0 0 0",
             xyz= "0 0 0"
            ),
            Geometry(
             Box(
              size= "0.07 0.07 0.07"
             )
            ),
            Material(
             Color(
              rgba= "0 1.0 1.0 1.0"
             ),
             name= "Cyan"
            )
               ),
               Collision(
            Origin(
             rpy= "0 0 0",
             xyz= "0 0 0"
            ),
            Geometry(
             Box(
              size= "0.07 0.07 0.07"
             )
            )
               ),
               name= "RSoftHand"
              ),
              Link(
               Inertial(
            Origin(
             rpy= "0 0 0",
             xyz= "0 0 0"
            ),
            Mass(
             value= "0.3"
            ),
            Inertia(
             iyz= "0",
             ixx= "0.001",
             izz= "0.001",
             ixy= "0",
             iyy= "0.001",
             ixz= "0"
            )
               ),
               Visual(
            Origin(
             rpy= "0 0 0",
             xyz= "0 0 0"
            ),
            Geometry(
             Box(
              size= "0.07 0.07 0.07"
             )
            ),
            Material(
             Color(
              rgba= "0 1.0 1.0 1.0"
             ),
             name= "Cyan"
            )
               ),
               Collision(
            Origin(
             rpy= "0 0 0",
             xyz= "0 0 0"
            ),
            Geometry(
             Box(
              size= "0.07 0.07 0.07"
             )
            )
               ),
               name= "LSoftHand"
              ),
              Joint(
               Parent(
            link= "RWrMot3"
               ),
               Child(
            link= "RSoftHand"
               ),
               Origin(
            rpy= "0 0 0",
            xyz= "0 0 -0.04"
               ),
               Axis(
            xyz= "1 0 0"
               ),
               Limit(
            effort= "5",
            lower= "0.0",
            velocity= "4.0",
            upper= "1.57075"
               ),
               Dynamics(
            damping= "3.0",
            friction= "0"
               ),
               name= "r_handj",
               type= "revolute"
              ),
              Joint(
               Parent(
            link= "LWrMot3"
               ),
               Child(
            link= "LSoftHand"
               ),
               Origin(
            rpy= "0 0 0",
            xyz= "0 0 -0.04"
               ),
               Axis(
            xyz= "-1 0 0"
               ),
               Limit(
            effort= "5",
            lower= "0.0",
            velocity= "4.0",
            upper= "1.57075"
               ),
               Dynamics(
            damping= "3.0",
            friction= "0"
               ),
               name= "l_handj",
               type= "revolute"
              ),
     )

