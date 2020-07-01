#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import pygame
import rospy
from std_msgs.msg import String

# initializes Pygame
pygame.init()

# sets the window title
pygame.display.set_caption('Keyboard events')

# sets the window size
pygame.display.set_mode((400, 400))

def talker():
    lockStr  = "AP1"
    fanStr   = "AP2"
    lampStr  = "AP3"
    ledStr   = "AP4"
    radioStr = "AP5"

    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():

        # if the 'close' button of the window is pressed
        event = pygame.event.wait()

        # if the 'close' button of the window is pressed
        if event.type == pygame.QUIT:
            # stops the application
            break

        # captures the 'KEYDOWN' and 'KEYUP' events
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            # gets the key name
            key_name = pygame.key.name(event.key)

            # converts to uppercase the key name
            key_name = key_name.upper()

            # if any key is pressed
            if event.type == pygame.KEYDOWN:
                if key_name == 'A':
                    print("Detected A Press - Send Lock Signal")
                    rospy.loginfo(lockStr)
                    pub.publish(lockStr)
                    rate.sleep()
                elif key_name == 'S':
                    print("Detected S Press - Send Fan Signal")
                    rospy.loginfo(fanStr)
                    pub.publish(fanStr)
                    rate.sleep()
                elif key_name == 'D':
                    print("Detected D Press - Send Lamp Signal")
                    rospy.loginfo(lampStr)
                    pub.publish(lampStr)
                    rate.sleep()
                elif key_name == 'F':
                    print("Detected F Press - Send Led Signal")
                    rospy.loginfo(ledStr)
                    pub.publish(ledStr)
                    rate.sleep()
                elif key_name == 'G':
                    print("Detected G Press - Send Radio Signal")
                    rospy.loginfo(radioStr)
                    pub.publish(radioStr)
                    rate.sleep()

        # finalizes Pygame
    pygame.quit()

    #hello_str = "hello world %s" % rospy.get_time()
    #rospy.loginfo(hello_str)
    #pub.publish(hello_str)
    #rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass