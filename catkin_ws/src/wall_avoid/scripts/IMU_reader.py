#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import Float64
from ros_pololu_servo.srv import MotorRange
from ros_pololu_servo.msg import MotorCommand
from ros_pololu_servo.msg import MotorState
from ros_pololu_servo.msg import MotorStateList
from sensor_msgs.msg import Imu
from scipy.signal import kaiserord, lfilter, firwin, freqz
from scipy.signal import lfilter, lfilter_zi, filtfilt, butter
#TODO create a v to x function

class IMU_reader():
    def __init__(self):
        #Publisher for sending the state_turning to the PID controller
        self.state_driving_pub = rospy.Publisher('/throttle/effort', Float64, queue_size=1)
        self.state_driving = Float64()
        self.state_filter_pub = rospy.Publisher('/imu/data_filter', Float64, queue_size=1)
        self.state_filter = Float64()
        self.sub_imu = rospy.Subscriber('/imu/data_raw', Imu, self.imuCallBack, queue_size=1)

        sample_rate = 235

        # The Nyquist rate of the signal.
        nyq_rate = sample_rate / 2.0

        # The desired width of the transition from pass to stop,
        # relative to the Nyquist rate.  We'll design the filter
        # with a 5 Hz transition width.
        width = 5.0/nyq_rate

        # The desired attenuation in the stop band, in dB.
        ripple_db = 60.0

        # Compute the order and Kaiser parameter for the FIR filter.
        N, beta = kaiserord(ripple_db, width)

        # The cutoff frequency of the filter.
        cutoff_hz = 5.0

        # Use firwin with a Kaiser window to create a lowpass FIR filter.
        self.taps = firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
        self.windowSize = len(self.taps)

        self.buffer = [0]*self.windowSize
        self.output = []
    #print self.windowSize

        self.lastTime  =0
        self.e = .3
    def imuCallBack(self,msg):
        out = self.lowPassFilter(msg.linear_acceleration.y)
        nowTime = msg.header.stamp.nsecs+msg.header.stamp.secs*1e9
        a = self.output[self.windowSize-1]
        b = self.output[self.windowSize-2]
        if(self.output[self.windowSize-1]<=self.e):
            a = 0
            b = 0
        if(self.lastTime == 0):
            self.lastTime = nowTime
            return
        out = (nowTime-self.lastTime)*(.5*(a+b))
        out = out/1e9
        pub = 0
        print out
        if(out < 30):
            pub =1
        self.state_driving = pub
        self.state_driving_pub.publish(self.state_driving)
        self.state_filter = out
        self.state_filter_pub.publish(self.state_filter)
        # print(out)
    def lowPassFilter(self,data):
        self.buffer.insert(0,data)
        self.buffer.pop()
        # Use firwin with a Kaiser window to create a lowpass FIR filter.
        #taps = firwin(self.windowSize, .25, window=('kaiser', 0))

        # Use lfilter to filter x with the FIR filter.
        self.output = lfilter(self.taps, 1.0, self.buffer)

        return self.output[self.windowSize-1]


if __name__ == "__main__":
    rospy.init_node('IMU_reader')
    imu = IMU_reader()
    rospy.spin()
