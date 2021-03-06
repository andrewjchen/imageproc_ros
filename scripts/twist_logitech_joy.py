#!/usr/bin/env python
import roslib; roslib.load_manifest('imageproc_ros')

import rospy
import serial

from std_msgs.msg import *
from geometry_msgs.msg import *
from sensor_msgs.msg import *

'''
twist_logitech_joy.py sends Twist commands from a joystick.
'''

def main():
    global pub
    rospy.loginfo("starting Twist Publishing via Joystick...")
    rospy.init_node('twist_logitech_joy')

    # TODO(andrew.chen) configureable topic
    pub = rospy.Publisher('safe_cmd_vel', Twist)
    rospy.Subscriber("joy", Joy, joystickChanged)
    rospy.spin()

def joystickChanged(data):
    #print str(data.axes[1]) + ","+ str(data.axes[4])

    #TODO(andrew.chen) configurable axes, constants?
    msg = Twist()
    msg.linear.x =  data.axes[1] + data.axes[4]
    msg.angular.z = data.axes[4] - data.axes[1]
    pub.publish(msg)

if __name__ == "__main__":
    main()
