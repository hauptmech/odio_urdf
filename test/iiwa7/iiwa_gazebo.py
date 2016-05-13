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

from odio_urdf import *

def link(N, material):
    ret = Gazebo(Material(xmltext = material),
       Mu1(xmltext = "0.2"),
       Mu2(xmltext = "0.2"),
       reference= "iiwa_link_"+str(N))
    return ret

def iiwa_gazebo(robot_name):
    ret = Group(
        Gazebo(Plugin("gazebo_ros_control",
            Robotnamespace(xmltext = "/"+robot_name),
            filename="libgazebo_ros_control.so")),
        link(0,"Gazebo/Grey"),
        link(1,"Gazebo/Orange"),
        link(2,"Gazebo/Orange"),
        link(3,"Gazebo/Orange"),
        link(4,"Gazebo/Orange"),
        link(5,"Gazebo/Orange"),
        link(6,"Gazebo/Orange"),
        link(7,"Gazebo/Grey"))
    return ret

if __name__ == "__main__":
    print(iiwa_gazebo("test"))

