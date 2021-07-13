"""
Copied from https://github.com/EnricoMingo/iit-coman-ros-pkg
"""

from odio_urdf import *
def legs(GAZEBO_COMAN_USES_ROUND_FEET):
    accumulator = Group(
             Xacroproperty(name= "PI",value= "3.14159265359"),
             Xacroproperty(name= "PI_2",value= "1.57079632679"),
             Xacroproperty(name= "SF",value= "0.03937"),
             Link(
              Inertial(
               Origin(rpy= "0 0 0",xyz= "-3.269678E-4 -0.023587321 -2.6496509E-4"),
               Mass(value= "0.89258227"),
               Inertia(
                ixz= "-2.4802574E-6",
                ixy= "-3.9936567E-6",
                ixx= "4.7672294E-4",
                iyy= "5.458038E-4",
                iyz= "-3.3389575E-6",
                izz= "5.126859E-4"
                ),
               ),
              Visual(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 0.023 -0.52"),
               Material(name= "dark_grey"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/Leg0.STL",scale= "${SF} ${SF} ${SF}"),
                name= "RHipMot_visual"),
               ),
              Collision(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 0.023 -0.52"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/simple/Leg0.STL",scale= "${SF} ${SF} ${SF}"),
                name= "RHipMot_collision"),
               ),
              name= "RHipMot"),
             Link(
              Inertial(
               Origin(rpy= "0 0 0",xyz= "0.0012591632 -0.016896372 -0.058903336"),
               Mass(value= "1.0246101"),
               Inertia(
                ixz= "-1.6685011E-5",
                ixy= "-1.4449904E-6",
                ixx= "9.165719E-4",
                iyy= "0.00104849584",
                iyz= "2.5492874E-5",
                izz= "6.8637197E-4"
                ),
               ),
              Visual(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 0.0726 -0.52"),
               Material(name= "dark_grey"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/Leg1.STL",scale= "${SF} ${SF} ${SF}"),
                name= "RThighUpLeg_visual"),
               ),
              Collision(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 0.0726 -0.52"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/simple/Leg1.STL",scale= "${SF} ${SF} ${SF}"),
                name= "RThighUpLeg_collision"),
               ),
              name= "RThighUpLeg"),
             Link(
              Inertial(
               Origin(rpy= "0 0 0",xyz= "9.8720058E-4 6.7037262E-4 -0.075716843"),
               Mass(value= "1.7001134"),
               Inertia(
                ixz= "2.6403262E-5",
                ixy= "1.7802399E-6",
                ixx= "0.0038979546",
                iyy= "0.0039360845",
                iyz= "4.522711E-5",
                izz= "9.0218711E-4"
                ),
               ),
              Visual(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 0.0726 -0.4176"),
               Material(name= "dark_grey"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/Leg2.STL",scale= "${SF} ${SF} ${SF}"),
                name= "RThighLowLeg_visual"),
               ),
              Collision(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 0.0726 -0.4176"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/simple/Leg2.STL",scale= "${SF} ${SF} ${SF}"),
                name= "RThighLowLeg_collision"),
               ),
              name= "RThighLowLeg"),
             Link(
              Inertial(
               Origin(rpy= "0 0 0",xyz= "0.0024612666 -0.0053099614 -0.08598948"),
               Mass(value= "1.4098179"),
               Inertia(
                ixz= "1.2260973E-5",
                ixy= "1.1227206E-5",
                ixx= "0.0040604004",
                iyy= "0.004005652855",
                iyz= "5.1899176E-4",
                izz= "0.0012414054"
                ),
               ),
              Visual(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 0.0726 -0.2942"),
               Material(name= "dark_grey"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/Leg3.STL",scale= "${SF} ${SF} ${SF}"),
                name= "RLowLeg_visual"),
               ),
              Collision(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 0.0726 -0.2942"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/simple/Leg3.STL",scale= "${SF} ${SF} ${SF}"),
                name= "RLowLeg_collision"),
               ),
              name= "RLowLeg"),
             Link(
              Inertial(
               Origin(rpy= "0 0 0",xyz= "8.8067281E-4 -9.2224881E-4 2.3038476E-4"),
               Mass(value= "0.72992131"),
               Inertia(
                ixz= "2.5430158E-7",
                ixy= "7.6346303E-6",
                ixx= "3.2034425E-4",
                iyy= "3.6584358E-4",
                iyz= "-3.6889276E-6",
                izz= "3.6065156E-4"
                ),
               ),
              Visual(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 0.0726 -0.0932"),
               Material(name= "dark_grey"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/Leg4.STL",scale= "${SF} ${SF} ${SF}"),
                name= "RFootmot_visual"),
               ),
              Collision(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 0.0726 -0.0932"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/simple/Leg4.STL",scale= "${SF} ${SF} ${SF}"),
                name= "RFootmot_collision"),
               ),
              name= "RFootmot"))
    if(GAZEBO_COMAN_USES_ROUND_FEET):
       accumulator(Link(
               Inertial(
                Origin(rpy= "0 0 0",xyz= "0.00969210464 -0.0090460227 -0.043062308"),
                Mass(value= "0.66646684"),
                Inertia(
                 ixz= "2.0080105E-4",
                 ixy= "-9.2387693E-5",
                 ixx= "0.0012944808",
                 iyy= "0.0015851846",
                 iyz= "2.7599327E-4",
                 izz= "0.0013326766"
                 ),
                ),
               Visual(
                Origin(rpy= "0 0 -3.14159265359",xyz= "0.0 0.0726 -0.0932"),
                Material(name= "dark_grey"),
                Geometry(
                 Mesh(filename= "package://coman_urdf/meshes/RoundFoot.STL",scale= "0.03937 0.03937 0.03937"),
                 name= "RFoot_visual"),
                ),
               Collision(
                Origin(rpy= "0 0 -3.14159265359",xyz= "0.0 0.0726 -0.0932"),
                Geometry(
                 Mesh(filename= "package://coman_urdf/meshes/simple/RoundFoot.STL",scale= "0.03937 0.03937 0.03937"),
                 name= "RFoot_collision"),
                ),
               name= "RFoot"))
    else:
        accumulator(Link(
               Inertial(
                Origin(rpy= "0 0 0",xyz= "0.00969210464 -0.0090460227 -0.043062308"),
                Mass(value= "0.66646684"),
                Inertia(
                 ixz= "2.0080105E-4",
                 ixy= "-9.2387693E-5",
                 ixx= "0.0012944808",
                 iyy= "0.0015851846",
                 iyz= "2.7599327E-4",
                 izz= "0.0013326766"
                 ),
                ),
               Visual(
                Origin(rpy= "0 0 0",xyz= "0.03 0 -0.07"),
                Geometry(
                 Box(size= "0.2 0.1 0.04"),
                 ),
                Material(name= "dark_gray"),
                ),
               Collision(
                Origin(rpy= "0 0 0",xyz= "0.03 0 -0.07"),
                Geometry(
                 Box(size= "0.2 0.1 0.04"),
                 ),
                ),
               name= "RFoot"))
    
    accumulator(Link(
              Inertial(
               Origin(rpy= "0 0 0",xyz= "-3.269678E-4 0.023587321 -2.6496509E-4"),
               Mass(value= "0.89258227"),
               Inertia(
                ixz= "-2.4802574E-6",
                ixy= "3.9936567E-6",
                ixx= "4.7672294E-4",
                iyy= "5.458038E-4",
                iyz= "3.3389575E-6",
                izz= "5.126859E-4"
                ),
               ),
              Visual(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 -0.023 -0.52"),
               Material(name= "dark_grey"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/Leg0.STL",scale= "${SF} -${SF} ${SF}"),
                name= "RHipMot_visual"),
               ),
              Collision(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 -0.023 -0.52"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/simple/Leg0.STL",scale= "${SF} -${SF} ${SF}"),
                name= "RHipMot_collision"),
               ),
              name= "LHipMot"),
             Link(
              Inertial(
               Origin(rpy= "0 0 0",xyz= "0.0012591632 0.016896372 -0.058903336"),
               Mass(value= "1.0246101"),
               Inertia(
                ixz= "-1.6685011E-5",
                ixy= "1.4449904E-6",
                ixx= "9.165719E-4",
                iyy= "0.00104849584",
                iyz= "-2.5492874E-5",
                izz= "6.8637197E-4"
                ),
               ),
              Visual(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 -0.0726 -0.52"),
               Material(name= "dark_grey"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/Leg1.STL",scale= "${SF} -${SF} ${SF}"),
                name= "LThighUpLeg_visual"),
               ),
              Collision(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 -0.0726 -0.52"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/simple/Leg1.STL",scale= "${SF} -${SF} ${SF}"),
                name= "LThighUpLeg_collision"),
               ),
              name= "LThighUpLeg"),
             Link(
              Inertial(
               Origin(rpy= "0 0 0",xyz= "9.8720058E-4 -6.7037262E-4 -0.075716843"),
               Mass(value= "1.7001134"),
               Inertia(
                ixz= "2.6403262E-5",
                ixy= "-1.7802399E-6",
                ixx= "0.0038979546",
                iyy= "0.0039360845",
                iyz= "-4.5227110E-5",
                izz= "9.0218711E-4"
                ),
               ),
              Visual(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 -0.0726 -0.4176"),
               Material(name= "dark_grey"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/Leg2.STL",scale= "${SF} -${SF} ${SF}"),
                name= "LThighLowLeg_visual"),
               ),
              Collision(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 -0.0726 -0.4176"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/simple/Leg2.STL",scale= "${SF} -${SF} ${SF}"),
                name= "LThighLowLeg_collision"),
               ),
              name= "LThighLowLeg"),
             Link(
              Inertial(
               Origin(rpy= "0 0 0",xyz= "0.0024612666 0.0053099614 -0.085989484"),
               Mass(value= "1.4098179"),
               Inertia(
                ixz= "1.2260973E-5",
                ixy= "-1.1227206E-5",
                ixx= "0.0040604004",
                iyy= "0.004005652855",
                iyz= "-5.1899176E-4",
                izz= "0.0012414054"
                ),
               ),
              Visual(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 -0.0726 -0.2942"),
               Material(name= "dark_grey"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/Leg3.STL",scale= "${SF} -${SF} ${SF}"),
                name= "LLowLeg_visual"),
               ),
              Collision(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 -0.0726 -0.2942"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/simple/Leg3.STL",scale= "${SF} -${SF} ${SF}"),
                name= "LLowLeg_collision"),
               ),
              name= "LLowLeg"),
             Link(
              Inertial(
               Origin(rpy= "0 0 0",xyz= "8.8067281E-4 9.2224881E-4 2.3038476E-4"),
               Mass(value= "0.72992131"),
               Inertia(
                ixz= "2.5430158E-7",
                ixy= "-7.6346303E-6",
                ixx= "3.2034425E-4",
                iyy= "3.6584358E-4",
                iyz= "3.6889276E-6",
                izz= "3.6065156E-4"
                ),
               ),
              Visual(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 -0.0726 -0.0932"),
               Material(name= "dark_grey"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/Leg4.STL",scale= "${SF} -${SF} ${SF}"),
                name= "LFootmot_visual"),
               ),
              Collision(
               Origin(rpy= "0 0 ${PI}",xyz= "0.0 -0.0726 -0.0932"),
               Geometry(
                Mesh(filename= "package://coman_urdf/meshes/simple/Leg4.STL",scale= "${SF} -${SF} ${SF}"),
                name= "LFootmot_collision"),
               ),
              name= "LFootmot"))
    if GAZEBO_COMAN_USES_ROUND_FEET:
       accumulator(Link(
               Inertial(
                Origin(rpy= "0 0 0",xyz= "0.0096921046 0.0090460227 -0.043062308"),
                Mass(value= "0.66646684"),
                Inertia(
                 ixz= "2.0080105E-4",
                 ixy= "9.2387693E-5",
                 ixx= "0.0012944808",
                 iyy= "0.0015851846",
                 iyz= "-2.7599327E-4",
                 izz= "0.0013326766"
                 ),
                ),
               Visual(
                Origin(rpy= "0 0 -3.14159265359",xyz= "0.0 -0.0726 -0.0932"),
                Material(name= "dark_grey"),
                Geometry(
                 Mesh(filename= "package://coman_urdf/meshes/RoundFoot.STL",scale= "0.03937 -0.03937 0.03937"),
                 name= "LFoot_visual"),
                ),
               Collision(
                Origin(rpy= "0 0 -3.14159265359",xyz= "0.0 -0.0726 -0.0932"),
                Geometry(
                 Mesh(filename= "package://coman_urdf/meshes/simple/RoundFoot.STL",scale= "0.03937 -0.03937 0.03937"),
                 name= "LFoot_collision"),
                ),
               name= "LFoot"))
    else:
        accumulator(Link(
               Inertial(
                Origin(rpy= "0 0 0",xyz= "0.0096921046 0.0090460227 -0.043062308"),
                Mass(value= "0.66646684"),
                Inertia(
                 ixz= "2.0080105E-4",
                 ixy= "9.2387693E-5",
                 ixx= "0.0012944808",
                 iyy= "0.0015851846",
                 iyz= "-2.7599327E-4",
                 izz= "0.0013326766"
                 ),
                ),
               Visual(
                Origin(rpy= "0 0 0",xyz= "0.03 0 -0.07"),
                Geometry(
                 Box(size= "0.2 0.1 0.04"),
                 ),
                Material(name= "dark_gray"),
                ),
               Collision(
                Origin(rpy= "0 0 0",xyz= "0.03 0 -0.07"),
                Geometry(
                 Box(size= "0.2 0.1 0.04"),
                 ),
                ),
               name= "LFoot"))
    
    accumulator(
             Joint(
              Parent(link= "Waist"),
              Child(link= "RHipMot"),
              Origin(rpy= "0 0 0",xyz= "0.0 -0.023 0.0"),
              Axis(xyz= "0 1 0"),
              Limit(
               effort= "50",
               velocity= "4.0",
               lower= "-1.9199",
               upper= "0.7854"
               ),
              Dynamics(damping= "3.0",friction= "0"),
              type= "revolute",name= "RHipSag"),
             Joint(
              Parent(link= "RHipMot"),
              Child(link= "RThighUpLeg"),
              Origin(rpy= "0 0 0",xyz= "0.0 -0.0496 0.0"),
              Axis(xyz= "1 0 0"),
              Limit(
               effort= "50",
               velocity= "4.0",
               lower= "-1.0472",
               upper= "0.4363"
               ),
              Dynamics(damping= "3.0",friction= "0"),
              type= "revolute",name= "RHipLat"),
             Joint(
              Parent(link= "RThighUpLeg"),
              Child(link= "RThighLowLeg"),
              Origin(rpy= "0 0 0",xyz= "0.0 0.0 -0.1024"),
              Axis(xyz= "0 0 1"),
              Limit(
               effort= "50",
               velocity= "4.0",
               lower= "-0.8727",
               upper= "0.8727"
               ),
              Dynamics(damping= "3.0",friction= "0"),
              type= "revolute",name= "RHipYaw"),
             Joint(
              Parent(link= "RThighLowLeg"),
              Child(link= "RLowLeg"),
              Origin(rpy= "0 0 0",xyz= "0.0 0.0 -0.1234"),
              Axis(xyz= "0 1 0"),
              Limit(
               effort= "50",
               velocity= "4.0",
               lower= "-0.1745",
               upper= "1.9199"
               ),
              Dynamics(damping= "3.0",friction= "0"),
              type= "revolute",name= "RKneeSag"),
             Joint(
              Parent(link= "RLowLeg"),
              Child(link= "RFootmot"),
              Origin(rpy= "0 0 0",xyz= "0.0 0.0 -0.201"),
              Axis(xyz= "1 0 0"),
              Limit(
               effort= "50",
               velocity= "4.0",
               lower= "-0.6109",
               upper= "0.6109"
               ),
              Dynamics(damping= "3.0",friction= "0"),
              type= "revolute",name= "RAnkLat"),
             Joint(
              Parent(link= "RFootmot"),
              Child(link= "RFoot"),
              Origin(rpy= "0 0 0",xyz= "0.0 0.0 0.0"),
              Axis(xyz= "0 1 0"),
              Limit(
               effort= "50",
               velocity= "4.0",
               lower= "-1.2217",
               upper= "1.2217"
               ),
              Dynamics(damping= "3.0",friction= "0"),
              type= "revolute",name= "RAnkSag"),
             Joint(
              Parent(link= "Waist"),
              Child(link= "LHipMot"),
              Origin(rpy= "0 0 0",xyz= "0.0 0.023 0.0"),
              Axis(xyz= "0 1 0"),
              Limit(
               effort= "50",
               velocity= "4.0",
               lower= "-1.9199",
               upper= "0.7854"
               ),
              Dynamics(damping= "3.0",friction= "0"),
              type= "revolute",name= "LHipSag"),
             Joint(
              Parent(link= "LHipMot"),
              Child(link= "LThighUpLeg"),
              Origin(rpy= "0 0 0",xyz= "0.0 0.0496 0.0"),
              Axis(xyz= "1 0 0"),
              Limit(
               effort= "50",
               velocity= "4.0",
               lower= "-0.4363",
               upper= "1.0472"
               ),
              Dynamics(damping= "3.0",friction= "0"),
              type= "revolute",name= "LHipLat"),
             Joint(
              Parent(link= "LThighUpLeg"),
              Child(link= "LThighLowLeg"),
              Origin(rpy= "0 0 0",xyz= "0.0 0.0 -0.1024"),
              Axis(xyz= "0 0 1"),
              Limit(
               effort= "50",
               velocity= "4.0",
               lower= "-0.8727",
               upper= "0.8727"
               ),
              Dynamics(damping= "3.0",friction= "0"),
              type= "revolute",name= "LHipYaw"),
             Joint(
              Parent(link= "LThighLowLeg"),
              Child(link= "LLowLeg"),
              Origin(rpy= "0 0 0",xyz= "0.0 0.0 -0.1234"),
              Axis(xyz= "0 1 0"),
              Limit(
               effort= "50",
               velocity= "4.0",
               lower= "-0.1745",
               upper= "1.9199"
               ),
              Dynamics(damping= "3.0",friction= "0"),
              type= "revolute",name= "LKneeSag"),
             Joint(
              Parent(link= "LLowLeg"),
              Child(link= "LFootmot"),
              Origin(rpy= "0 0 0",xyz= "0.0 0.0 -0.201"),
              Axis(xyz= "1 0 0"),
              Limit(
               effort= "50",
               velocity= "4.0",
               lower= "-0.6109",
               upper= "0.6109"
               ),
              Dynamics(damping= "3.0",friction= "0"),
              type= "revolute",name= "LAnkLat"),
             Joint(
              Parent(link= "LFootmot"),
              Child(link= "LFoot"),
              Origin(rpy= "0 0 0",xyz= "0.0 0.0 0.0"),
              Axis(xyz= "0 1 0"),
              Limit(
               effort= "50",
               velocity= "4.0",
               lower= "-1.2217",
               upper= "1.2217"
               ),
              Dynamics(damping= "3.0",friction= "0"),
              type= "revolute",name= "LAnkSag"),
             )
    return accumulator
