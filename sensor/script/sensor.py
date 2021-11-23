#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Vector3
from common_msgs.msg import Common

rospy.init_node('sensor')
pub = rospy.Publisher('algorithm_msg', Common, queue_size=1)
msg = Common()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.num.data =1
    msg.vec = Vector3(x=100%4, y=100%7, z=100%5)
    pub.publish(msg)
    print "publish:",msg.num, msg.vec.x, msg.vec.y, msg.vec.z
    rate.sleep()
