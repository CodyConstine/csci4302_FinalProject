#! /usr/bin/env python
import numpy as np
import cv2

print cv2.__version__

img = cv2.imread('3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,0)
im2,contours,h = cv2.findContours(thresh.copy(),1,2)

for cnt in contours:
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt,True)
    epsilon = 0.01*perimeter
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    x,y,w,h = cv2.boundingRect(cnt)
    if len(approx) == 8 and w >= 40 and h >= 40:
        #print area
        cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.drawContours(gray,[cnt],0,(255,55,55),3)

cv2.imshow('gray',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
