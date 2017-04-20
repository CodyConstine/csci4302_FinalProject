#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import Float64
from ros_pololu_servo.srv import MotorRange
from ros_pololu_servo.msg import MotorCommand
from ros_pololu_servo.msg import MotorState
from ros_pololu_servo.msg import MotorStateList


class wall_avoid():

    def __init__(self):
        #Publisher for sending commands to the pololu
        self.motor_pub = rospy.Publisher('pololu/command', MotorCommand, queue_size=1)
        self.cmd = MotorCommand()
        self.cmd.joint_name = 'front_turning'
        self.cmd.speed = 0
        self.cmd.acceleration = 0
        #Publisher for sending the state_turning to the PID controller
        self.state_turning_pub = rospy.Publisher('/state', Float64, queue_size=1)
        self.state_turning = Float64()
        #Publisher for sending a setpoint_turning to the PID controller
        self.setpoint_turning_pub = rospy.Publisher('/setpoint', Float64, queue_size=1)
        self.setpoint_turning = Float64()

        #Subscriber for the state of the pololu motors
        self.sub_pololu = rospy.Subscriber('/pololu/motor_states', MotorStateList, self.subCallback_Turning, queue_size=1)
        #Subscriber for the PID control msgs
        self.sub_control = rospy.Subscriber('/control_effort', Float64, self.subCallback_Control, queue_size=1)
        #this block is to send the desired setpoint
        self.setpoint_turning = 130
        self.setpoint_turning_pub.publish(self.setpoint_turning)
    #callback for the control_effort, will turn the control_effort data on -100 to 100 and scale our maximum radians of .6
    def subCallback_Control(self, msg):
        turn_ratio = .6/msg.data
        self.cmd.position = turn_ratio
        self.motor_pub.publish(self.cmd)
    #callback for the pololu motor states, will take the side ir pulse and feed it to the pid controller
    def subCallback_Turning(self, msg):
        for x in msg.motor_states:
            if x.motor_id == 6:
                dist = x.pulse
                self.state_turning = dist
                self.state_turning_pub.publish(self.state_turning)

                # turn_ratio = float((float(self.middle_dist) - float(dist))/float(dist))*math.pi/2
                # print turn_ratio
                # if(turn_ratio>.5):
                #     turn_ratio = .5
                # if(turn_ratio<-.5):
                #     turn_ratio = -.5
                # self.cmd.position = turn_ratio
                # self.motor_pub.publish(self.cmd)

if __name__ == "__main__":
    rospy.init_node('wall_avoid')
    wall = wall_avoid()
    rospy.spin()
