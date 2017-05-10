#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import Float64
from ros_pololu_servo.srv import MotorRange
from ros_pololu_servo.msg import MotorCommand
from ros_pololu_servo.msg import MotorState
from ros_pololu_servo.msg import MotorStateList
from sensor_msgs.msg import Imu

#TODO create a v to x function

class IR_reader():
    def __init__(self):
        #Publisher for sending the state_turning to the PID controller
        self.state_turning_pub = rospy.Publisher('/turning_PID/state', Float64, queue_size=1)
        self.state_turning = Float64()
        #Publisher for sending a setpoint_turning to the PID controller
        self.setpoint_turning_pub = rospy.Publisher('/turning_PID/setpoint', Float64, queue_size=1)
        self.setpoint_turning = Float64()

        #Publisher for sending the state_turning to the PID controller
        self.state_driving_pub = rospy.Publisher('/driving_PID/state', Float64, queue_size=1)
        self.state_driving = Float64()
        #Publisher for sending a setpoint_turning to the PID controller
        self.setpoint_driving_pub = rospy.Publisher('/driving_PID/setpoint', Float64, queue_size=1)
        self.setpoint_driving = Float64()

        #Subscriber for the state of the pololu motors
        self.sub_pololu = rospy.Subscriber('/pololu/motor_states', MotorStateList, self.subCallback_Turning, queue_size=1)
        #this block is to send the desired setpoint
        self.setpoint_turning = 130
        self.setpoint_driving = 120
    #callback for the pololu motor states, will take the side ir pulse and feed it to the pid controller
    def subCallback_Turning(self, msg):
#	print "Here"
	a = 0
	b = 0
        for x in msg.motor_states:
	    #a = 0
	    #b = 0
            if x.motor_id == 6:
#		print x.pulse
		a = x.pulse
#                self.state_turning = x.pulse
#                self.setpoint_turning_pub.publish(self.setpoint_turning)
#                self.state_turning_pub.publish(self.state_turning)
            if x.motor_id == 11:
		b = x.pulse
#                self.state_driving = x.pulse
#                self.setpoint_driving_pub.publish(self.setpoint_driving)
#                self.state_driving_pub.publish(self.state_driving)
#	print str(a-b)
	self.state_turning_pub.publish(a-b)
if __name__ == "__main__":
    rospy.init_node('IR_reader')
    ir = IR_reader()
    rospy.spin()
