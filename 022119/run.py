import cv2
import numpy as np

def detect_faces(f_cascade, colored_img, scaleFactor = 1.1):
	#just making a copy of image passed, so that passed image is not changed
	img_copy = colored_img.copy()
	#convert the test image to gray image as opencv face detector expects gray images
	gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)       
	#let's detect multiscale (some images may be closer to camera than others) images
	faces = f_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=5);   
	#go over list of faces and draw them as rectangles on original colored img
	for (x, y, w, h) in faces:
		cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)
	return img_copy

cap = cv2.VideoCapture(0)
haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')

while(True):
	_, frame = cap.read()

	drawn = detect_faces(haar_face_cascade, frame)
	cv2.imshow('live', cv2.flip(drawn,1))

	if(cv2.waitKey(1) & 0xFF == ord('q')):
		break
	
	cv2.destroyAllWindows()
	cap.release()