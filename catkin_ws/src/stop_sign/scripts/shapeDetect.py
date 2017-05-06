#! /usr/bin/env python
import numpy as np
import cv2

print cv2.__version__

img = cv2.imread('3.jpg')
#gray = cv2.imread('shapes.png',0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,0)
im2,contours,h = cv2.findContours(thresh.copy(),1,2)

for cnt in contours:
    M = cv2.moments(cnt)
    #print M
    #cx = int(M['m10']/M['m00'])
    #cy = int(M['m01']/M['m00'])
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt,True)
    epsilon = 0.01*perimeter
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    hull = cv2.convexHull(cnt)
    k = cv2.isContourConvex(cnt)
    #print len(approx)
    if len(approx) == 8:
        #print "octagon"
        cv2.drawContours(img,[cnt],0,(255,55,55),3)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
