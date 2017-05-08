#!/usr/bin/env python

import rospy
import math
import numpy as np
from std_msgs.msg import Float64
from ros_pololu_servo.srv import MotorRange
from ros_pololu_servo.msg import MotorCommand
from ros_pololu_servo.msg import MotorState
from ros_pololu_servo.msg import MotorStateList
from sensor_msgs.msg import Imu
from scipy.signal import kaiserord, lfilter, firwin, freqz
from scipy.signal import lfilter, lfilter_zi, filtfilt, butter
from scipy.linalg import block_diag
from filterpy.common import Q_discrete_white_noise
from filterpy.kalman import KalmanFilter
#TODO create a v to x function

class IMU_reader():
    def __init__(self):
        #Publisher for sending the state_turning to the PID controller
        self.state_driving_pub = rospy.Publisher('/throttle/effort', Float64, queue_size=1)
        self.state_driving = Float64()
        self.state_filter_pub = rospy.Publisher('/imu/data_filter', Float64, queue_size=1)
        self.state_filter = Float64()
        self.sub_imu = rospy.Subscriber('/imu/data_raw', Imu, self.imuCallBack, queue_size=1)

        # intial parameters
        self.n_iter = 1000000
        self.sz = (self.n_iter,) # size of array
        # z = np.random.normal(x,0.1,size=sz) # observations (normal about x, sigma=0.1)

        self.Q = .2 # process variance

        # allocate space for arrays
        self.xhat=np.zeros(self.sz)      # a posteri estimate of x
        self.P=np.zeros(self.sz)         # a posteri error estimate
        self.xhatminus=np.zeros(self.sz) # a priori estimate of x
        self.Pminus=np.zeros(self.sz)    # a priori error estimate
        self.K=np.zeros(self.sz)         # gain or blending factor

        self.R = 0.4 # estimate of measurement variance, change to see effect

        # intial guesses
        self.xhat[0] = 0.0
        self.P[0] = 0.0
        self.iterator = 1

        self.lastTime = 0
        dt = .004
        self.rk = KalmanFilter(dim_x = 2, dim_z = 2)
        self.rk.x = [0,0]
        self.rk.F = np.array([[1,0],[0,1]])
        self.rk.H = np.array([[dt/2,0],[0,dt/2]])
        self.rk.R = np.array([[.1,0],[0,.1]])
        q = Q_discrete_white_noise(dim=2, dt=.004, var=.1)
        self.rk.Q = block_diag(q, q)
        self.rk.P *= 1
        self.xs = []
    def imuCallBack(self,msg):
        k = self.iterator
        # self.iterator+=1
        y = msg.linear_acceleration.y
        if(y<.5 and y>-.5):
            y = 0
        x = msg.linear_acceleration.x
        # # time update
        # self.xhatminus[k] = self.xhat[k-1]
        # self.Pminus[k] = self.P[k-1]+self.Q
        # time = msg.header.stamp.nsecs+msg.header.stamp.secs*1e9
        #
        # # measurement update
        # self.K[k] = self.Pminus[k]/( self.Pminus[k]+self.R )
        # self.xhat[k] = self.xhatminus[k]+self.K[k]*(z-self.xhatminus[k])
        # self.P[k] = (1-self.K[k])*self.Pminus[k]
        # self.state_filter = self.xhat[k]
        # if(self.xhat[k] < .1 and self.xhat[k]>-.1):
        #     self.xhat[k] = 0
        # if(self.lastTime ==0):
        #     self.lastTime = time
        #     return
        # v = ((time-self.lastTime)/2)*(self.xhat[k]+self.xhat[k+1])/1e9
        # print self.xhat[k]
        # self.state_filter_pub.publish(self.state_filter)

        self.rk.update(np.array([x,y]))
        self.xs.append(self.rk.x)
        # print len(self.xs)
        print self.xs[k][1]
        self.state_filter = self.xs[k][1]
        self.state_filter_pub.publish(self.state_filter)
        pub = 0
        if(self.xs[k][1]<10):
            pub = 1
        self.state_driving = pub
        self.state_driving_pub.publish(self.state_driving)
        # rk.predict()


        self.iterator+=1


if __name__ == "__main__":
    rospy.init_node('IMU_reader')
    imu = IMU_reader()
    rospy.spin()
