#!/usr/bin/env python3
import cv2
import numpy as np

cam0 = cv2.VideoCapture(0)
lower_red = np.array([115,60,50])
upper_red = np.array([155,100, 255])
lower_green = np.array([40,40,70])
upper_green = np.array([80,120,255])
lower_yellow = np.array([23, 41, 70])
upper_yellow = np.array([45, 150, 255])

while True:
	ret, frame = cam0.read()
	frame = cv2.flip(frame, 1)

	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

	#get red
	mask = cv2.inRange(hsv_frame, lower_red, upper_red)
	red = cv2.bitwise_and(frame, frame, mask = mask)

	#get green
	mask = cv2.inRange(hsv_frame, lower_green, upper_green)
	green = cv2.bitwise_and(frame, frame, mask = mask)

	#get yellow
	mask = cv2.inRange(hsv_frame, lower_yellow, upper_yellow)
	yellow = cv2.bitwise_and(frame, frame, mask = mask)

	cv2.imshow('live', frame)
	cv2.imshow('red', red)
	cv2.imshow('yellow', yellow)
	cv2.imshow('green', green)

	if(cv2.waitKey(1) & 0xFF == ord('q')):
		break
cv2.destroyAllWindows()
cam0.release()