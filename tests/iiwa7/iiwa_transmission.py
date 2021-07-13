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

def transmission(hw_interface,N):
    """ Definition of one transmission """
    N = str(N) # Make sure we can easily cat to a string
    ret = Transmission(
        "iiwa_tran_"+N,
        Type(xmltext="transmission_interface/SimpleTransmission"),
        Transjoint("iiwa_joint_"+N, Hardwareinterface(xmltext = hw_interface)),
        Actuator("iiwa_motor_"+N, 
            Hardwareinterface(xmltext = hw_interface),
            Mechanicalreduction(xmltext = "1")
        )
    )
    return ret


def transmissions(hardware_interface):
    """ Create a transmission for each joint thant needs one """
    ret = Group()
    for i in range(1,8):
       ret(transmission(hardware_interface,i))

    return ret 


if __name__ == "__main__":
    print(transmissions("hardware_interface"))
