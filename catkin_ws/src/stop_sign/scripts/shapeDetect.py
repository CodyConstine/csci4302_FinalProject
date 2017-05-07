#! /usr/bin/env python
from std_msgs.msg import String
import numpy as np
import roslib
roslib.load_manifest('my_package')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

from __future__ import print_function

class image_converter:
	def __init__(self):
		self.image_pub = rospy.Publisher("stop_sign",Image)
		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber("camera/image_raw",Image,self.callback)

	def callback(self,data):
		try:
			cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
		except CvBridgeError as e:
			print(e)
		(rows,cols,channels) = cv_image.shape
		
		ret,thresh = cv2.threshold(cv_image,127,255,0)
		im2,contours,h = cv2.findContours(thresh.copy(),1,2)
		
		for cnt in contours:
			area = cv2.contourArea(cnt)
			perimeter = cv2.arcLength(cnt,True)
			epsilon = 0.01*perimeter
			approx = cv2.approxPolyDP(cnt,epsilon,True)
			x,y,w,h = cv2.boundingRect(cnt)
			if len(approx) == 8 and w >= 40 and h >= 40:
				cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),2)
				cv2.drawContours(gray,[cnt],0,(255,55,55),3)
		
		if cols > 60 and rows > 60 :
			cv2.circle(cv_image, (50,50), 10, 255)
		cv2.imshow("Image window", cv_image)
		cv2.waitKey(3)

		try:
			self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
		except CvBridgeError as e:
			print(e)
	
	def main(args):
		ic = image_converter()
		rospy.init_node('image_converter', anonymous=True)
		try:
			rospy.spin()
		except KeyboardInterrupt:
			print("Shutting down")
		cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
