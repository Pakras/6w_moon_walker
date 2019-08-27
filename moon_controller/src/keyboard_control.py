#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
import sys
import select
import termios
import tty
import geometry_msgs.msg
import time
import std_msgs.msg

MANIPULATOR_STEPS = 500
SPEED_STEPS = 5


def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def parse_buttons(key):
    global msgForce1
    global fore, aft

    if key == 'r':
        msgForce1 += 0.1
        middle_pub.publish(msgForce1)
    if key == 'w':
        aftRightTire_pub.publish(-1)
        aftLeftTire_pub.publish(1)
        midRightTire_pub.publish(-1)
        foreRightTire_pub.publish(-1)
        foreLeftTire_pub.publish(1)
        midLeftTire_pub.publish(1)
    if key == 's':
        aftRightTire_pub.publish(0)
        aftLeftTire_pub.publish(0)
        midRightTire_pub.publish(0)
        foreRightTire_pub.publish(0)
        foreLeftTire_pub.publish(0)
        midLeftTire_pub.publish(0)
    if key == 'x':
        aftRightTire_pub.publish(1)
        aftLeftTire_pub.publish(-1)
        midRightTire_pub.publish(1)
        foreRightTire_pub.publish(1)
        foreLeftTire_pub.publish(-1)
        midLeftTire_pub.publish(-1)
    if key == 'd':
        aftRightTire_pub.publish(-2)
        aftLeftTire_pub.publish(-2)
        midRightTire_pub.publish(-2)
        foreRightTire_pub.publish(-2)
        foreLeftTire_pub.publish(-2)
        midLeftTire_pub.publish(-2)
    if key == 'a':
        aftRightTire_pub.publish(2)
        aftLeftTire_pub.publish(2)
        midRightTire_pub.publish(2)
        foreRightTire_pub.publish(2)
        foreLeftTire_pub.publish(2)
        midLeftTire_pub.publish(2)

    if key == 'f':
        msgForce1 -= 0.1
        middle_pub.publish(msgForce1)
    if key == 't':
        fore += 0.05
        fore_pub.publish(fore)
    if key == 'g':
        fore -= 0.05
        fore_pub.publish(fore)
    if key == 'y':
        aft -= 0.05
        aft_pub.publish(aft)
    if key == 'h':
        aft += 0.05
        aft_pub.publish(aft)

    return 0


if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    speed = 0
    force = 600
    torque = 300
    msgForce1 = 0
    msgForce2 = 0
    fore = 0
    aft = 0
    current_longt = 0

    rospy.init_node('rocad_teleop')

    middle_pub = \
        rospy.Publisher('/moon/LefttoRight/command',
                        std_msgs.msg.Float64, queue_size=1)
    fore_pub = \
        rospy.Publisher('/moon/fore/command',
                        std_msgs.msg.Float64, queue_size=1)
    aft_pub = rospy.Publisher('/moon/aft/command'
                              , std_msgs.msg.Float64, queue_size=1)
    aftRightTire_pub = \
        rospy.Publisher('/moon/aftRightWheel_j/command',
                        std_msgs.msg.Float64, queue_size=1)
    aftLeftTire_pub = \
        rospy.Publisher('/moon/aftLeftWheel_j/command',
                        std_msgs.msg.Float64, queue_size=1)
    midRightTire_pub = \
        rospy.Publisher('/moon/midRightWheel_j/command',
                        std_msgs.msg.Float64, queue_size=1)
    foreRightTire_pub = \
        rospy.Publisher('/moon/foreRightWheel_j/command',
                        std_msgs.msg.Float64, queue_size=1)
    foreLeftTire_pub = \
        rospy.Publisher('/moon/foreLeftWheel_j/command',
                        std_msgs.msg.Float64, queue_size=1)
    midLeftTire_pub = \
        rospy.Publisher('/moon/midLeftWheel_j/command',
                        std_msgs.msg.Float64, queue_size=1)

    try:
        while 1:
            key = getKey()
            parse_buttons(key)
            if key == '\x03':
                raise KeyboardInterrupt()
    except Exception, e:
        print e
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

