#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import Float32
from ros_pololu_servo.srv import MotorRange
from ros_pololu_servo.msg import MotorCommand
from ros_pololu_servo.msg import MotorState
from ros_pololu_servo.msg import MotorStateList


class wall_avoid():

    def __init__(self):
        self.middle_dist = 120;
        self.motor_pub = rospy.Publisher('pololu/command', MotorCommand, queue_size=1)
        self.cmd = MotorCommand()
        self.cmd.joint_name = 'front_turning'
        self.cmd.speed = 0
        self.cmd.acceleration = 0

        self.sub = rospy.Subscriber('/pololu/motor_states', MotorStateList, self.subCallback, queue_size=1)

    def subCallback(self, msg):
        for x in msg.motor_states:
            # print x.motor_id
            if x.motor_id == 6:
                dist = x.pulse
                turn_ratio = float((float(self.middle_dist) - float(dist))/float(dist))*math.pi/2
                print turn_ratio
                if(turn_ratio>.5):
                    turn_ratio = .5
                if(turn_ratio<-.5):
                    turn_ratio = -.5
                self.cmd.position = turn_ratio
                self.motor_pub.publish(self.cmd)

if __name__ == "__main__":
    rospy.init_node('wall_avoid')
    wall = wall_avoid()
    rospy.spin()
