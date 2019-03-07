#!/usr/bin/env python3
import numpy as np
import cv2 as cv

img = cv.imread('sphere.png')
lower_red = np.array([110, 50, 50])
upper_red = np.array([121,255, 255])

hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)
mask = cv.inRange(hsv, lower_red, upper_red)
red = cv.bitwise_and(img, img, mask = mask)
edges = cv.Canny(red, 10, 100)

cv.imshow('canny', edges)
cv.imshow('image', img)
cv.imshow('red', red)
cv.waitKey(0)
cv.destroyAllWindows