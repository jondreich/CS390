import cv2 as cv
import numpy as np

img = cv.imread('img/ugly.jpg')
height, width, depth = img.shape
img = cv.resize(img, int(height/2), int(width/2))
hsv = cv.cvtColor(img, cv.COLOR_BGR2HLS)
hsv[:,:,0] = hsv[:,:,0]
blur = cv.GaussianBlur(hsv,(5,5),0)
smooth = cv.addWeighted(blur,1.5,img,-0.5,0)

cv.imshow('image', img)
cv.imshow('image', smooth)
cv.waitKey(0)
cv.destroyAllWindows