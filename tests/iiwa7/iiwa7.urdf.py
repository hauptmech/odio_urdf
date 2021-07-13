#!/bin/env python
#
# odio_urdf definition of iiwa7
# Copyright 2016, hauptmech <hauptmech@gmail.com>
#
# Data copied from iiwa_description by Salvo Virga <salvo.virga@tum.de>
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are permit
# ted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of cond
# itions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of c
# onditions and the following disclaimer in the documentation and/or other materials provided
#  with the distribution.
# 
# 3. Neither the name of the copyright holder nor the names of its contributors may be used t
# o endorse or promote products derived from this software without specific prior written per
# mission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
#  OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTAB
# ILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT 
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, 
# OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON A
# NY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENC
# E OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import sys
import math
from odio_urdf import *
import iiwa_materials
import iiwa_gazebo
import iiwa_transmission

PI = math.pi
safety_controller_k_pos = 100
safety_controller_k_vel = 2
joint_damping = 0.5
max_effort = 300
max_velocity = 10
filepath = "package://iiwa_description/meshes/iiwa7/"

def link(N,robot_name,origin,mass,I,material,geom_origin):
    """
        Most of the links are the same except for the passed in info.
        This function just allows grouping the important numbers better. 
    """
    N = str(N)
    ret = Link(
        Inertial(
            Origin(origin),
            Mass(value=mass),
            Inertia(I)),
        Visual(
            Origin(geom_origin),
            Geometry(Mesh(filename = filepath+"visual/link_"+N+".stl")),
            Material(material)),
        Collision(
            Origin(geom_origin),
            Geometry(Mesh(filename = filepath+"collision/link_"+N+".stl")),
            Material(material)),
       name = robot_name+"_link_"+N)
    return ret

def joint(N,robot_name,origin,limit,safe):
    """
        Most of the joints are the same except for the passed in info.
        This function just allows grouping the important numbers better. 
    """
    N = int(N)
    ret = Joint(
        Parent(link=robot_name+"_link_"+str(N-1)),
        Child(link=robot_name+"_link_"+str(N)),
        Origin(origin),
        Axis(xyz="0 0 1"),
        Limit(lower=limit[0]*PI/180, upper=limit[1]*PI/180, effort=max_effort, velocity=max_velocity),
        Safety_controller(soft_lower_limit=safe[0]*PI/180,soft_upper_limit=safe[1]*PI/180,
            k_position=safety_controller_k_pos, k_velocity=safety_controller_k_vel),
        Dynamics(damping=joint_damping),
        type="revolute",
        name= robot_name+"_joint_"+str(N))
    return ret

def iiwa7_main(parent, hardware_interface, robot_name):
    """
        Main definition of the iiwa7. 
    """
    ret = Group(
        Joint(parent+"_"+robot_name+"_joint", Origin(xyz="0 0 0", rpy="0 0 0"),
            Parent(link=parent), Child(link=robot_name+"_link_0"), type="fixed"),
        link(0, robot_name,[-0.1,0.0   ,0.07  ,0,0,0],5,[0.5,0,0,0.06,0,0.03], "Grey",[0,0,0]),
        joint(1,robot_name,[0.0 ,0.0   ,0.15  ,0,0,0],[-170,170],[-168,168]),
        link(1, robot_name,[0.0 ,-0.03 ,0.12  ,0,0,0],4,[1,0,0,0.09,0,0.02], "Orange",[0,0,0.0075]),
        joint(2,robot_name,[0.0 ,0.0   ,0.19  ,PI/2,0,PI],[-120,120],[-118,118]),
        link(2, robot_name,[3e-4,0.059 ,0.042 ,0,0,0],4,[0.05,0,0,0.18,0,0.044], "Orange",[0,0,-0.006]),
        joint(3,robot_name,[0.0 ,0.21  ,0.0   ,PI/2,0,PI],[-170,170],[-168,168]),
        link(3, robot_name,[0.0 ,0.03  ,0.13  ,0,0,0],3,[0.08,0,0,0.075,0,0.01], "Orange",[0,-0.005,-0.06]),
        joint(4,robot_name,[0.0 ,0.0   ,0.19  ,PI/2,0,0],[-120,120],[-118,118]),
        link(4, robot_name,[0.0 ,0.067 ,0.34  ,0,0,0],2.7,[0.03,0,0,0.01,0,0.029], "Orange",[0,0,0]),
        joint(5,robot_name,[0.0 ,0.21  ,0.0   ,-PI/2,PI,0],[-175,175],[-173,173]),
        link(5, robot_name,[1e-4,0.021 ,0.076 ,0,0,0],1.7,[0.02,0,0,0.018,0,0.005], "Orange",[0,0,-0.026]),
        joint(6,robot_name,[0.0 ,0.0607,0.19  ,PI/2,0,0],[-120,120],[-118,118]),
        link(6, robot_name,[0.0 ,6e-4  ,4e-4  ,0,0,0],1.8,[0.005,0,0,0.0036,0,0.0047], "Orange",[0,0,0]),
        joint(7,robot_name,[0.0 ,0.081 ,0.0607,-PI/2,PI,0],[-175,175],[-173,173]),
        link(7, robot_name,[0.0 ,0.0   ,0.02  ,0,0,0],0.3,[0.001,0,0,0.001,0,0.001], "Grey",[0,0,-0.0005]),
        Joint(  
            Parent(link=robot_name+"_link_7"),
            Child(link=robot_name+"_joint_ee_kuka"),
            Origin([0,0,0.045,PI,PI,PI]), 
            Axis(xyz="0 0 1"),
            name = robot_name+"_joint_ee",
            type = "fixed"),
        Link(robot_name+"_link_ee_kuka"),
        Joint("tool0_joint",
            Parent(link=robot_name+"_link_7"),
            Child(robot_name+"_link_ee"),
            Origin([0,0,0.04,0,-PI/2,0]),
            type="fixed"),
        Link(robot_name+"_link_ee"))

    ret(iiwa_gazebo.iiwa_gazebo(robot_name),iiwa_transmission.transmissions(hardware_interface))

    #Link 0 has some unique collision checking
    ret[1](Self_collision_checking(
            Origin(xyz = "0 0 0", rpy = "0 0 0"),
            Geometry(Capsule(radius = 0.15, length = 0.25))))
 
    return ret


if __name__ == "__main__":
    
    # Default command line parameters 
    defaults = {"hardware_interface": "PositionJointInterface", "robot_name": "iiwa"}

    # Extract all 'name:=value' arguments from the command line and add them
    # to kwargs
    kwargs = {}
    for a in sys.argv:
        vals = a.split(":=")
        if len(vals) == 2:
            kwargs[vals[0]]=vals[1]

    # Make sure that parameters not passed in on commandline are set to their
    # default value.
    for k,v in defaults.items():
        if not k in kwargs:
            kwargs[k]=v

    # Build the robot structure
    iiwa7 = Robot(
        iiwa_materials.materials,
        Link("world"),
        iiwa7_main(parent="world",**kwargs),
        name = kwargs["robot_name"]
    )    

    # Dump the robot to stdout
    print(iiwa7)
