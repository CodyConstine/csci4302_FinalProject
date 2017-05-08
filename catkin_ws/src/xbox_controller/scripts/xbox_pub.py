#!/usr/bin/env python

import rospy
import xbox
from std_msgs.msg import Float64

def talker():
    turning_pub = rospy.Publisher('/turning_PID/control_effort', Float64, queue_size=10)
    turning = Float64
    driving_pub = rospy.Publisher('/driving_PID/control_effort', Float64, queue_size=10)
    driving = Float64
    throttle_pub = rospy.Publisher('/throttle/effort', Float64, queue_size=10)
    throttle = Float64
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        throttle = 0
        if(joy.rightTrigger()):
            throttle = 1.0
        if(joy.rightTrigger() == False):
            throttle = 0

        turning = joy.leftX()*100
        # rospy.loginfo(a)
        turning_pub.publish(turning)
        rate.sleep()
    joy.close()


if __name__ == '__main__':
    try:
        joy = xbox.Joystick()
        talker()
    except rospy.ROSInterruptException:
        pass
