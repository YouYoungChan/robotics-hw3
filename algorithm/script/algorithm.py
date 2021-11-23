#!/usr/bin/env python
import rospy
from common_msgs.msg import Common

def callback(msg):
    print "subscribe:", msg.num.data, msg.vec.x, msg.vec.y, msg.vec.z

rospy.init_node('algorithm')
sub = rospy.Subscriber('algorithm_msg', Common, callback)
rospy.spin()
