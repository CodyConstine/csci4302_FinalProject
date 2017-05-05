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

class IMU_reader():
    def __init__(self):
        #Publisher for sending the state_turning to the PID controller
        self.state_driving_pub = rospy.Publisher('/throttle/effort', Float64, queue_size=1)
        self.state_driving = Float64()

        self.sub_imu = rospy.Subscriber('/imu/data_raw', Imu, self.imuCallBack, queue_size=1)

        self.input = []
        self.output = []
        self.ALPHA = 0.15
    def imuCallBack(self,msg):
        out = self.lowPassFilter(msg.linear_acceleration.y)
        pub = 1
        if(out>10):
            pub = 0
        self.state_driving = pub
        self.state_driving_pub.publish(self.state_driving)
        print(out)

    def lowPassFilter(self,data):
        n = len(self.input)
        self.input.append(data)
        if(len(self.output)== 0):
            self.output.append(self.input[0])
            return input[n-1]
        l = 0
        if(n>10):
            l = n-10
        for i in range(l,n):
            self.output.append(self.output[i-1] + self.ALPHA * (self.input[i]*self.output[i-1]))
        return self.output[n-1]

if __name__ == "__main__":
    rospy.init_node('IMU_reader')
    imu = IMU_reader()
    rospy.spin()
