import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
	_, frame = cap.read()
	blur = cv2.gaussianblur
	thresh = cv2.threshold(blur,100,200,cv2.THRESH_BINARY)
	canned = cv2.Canny(thresh, 100, 200)
	cv2.imshow('live', cv2.flip(canned,1))
	if(cv2.waitKey(1) & 0xFF == ord('q')):
		break

cv2.destroyAllWindows()
cap.release()