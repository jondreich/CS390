#!/usr/bin/env python3
import numpy as np
import cv2 as cv

img = cv.imread('piggo.jpg')
height, width, depth = img.shape

edges = cv.Canny(img, 100, 200)
lines = cv.HoughLines(edges, 1, np.pi/180, 200)

for line in lines:
    for rho, theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + width*(-b))
        y1 = int(y0 + height*(a))
        x2 = int(x0 - width*(-b))
        y2 = int(y0 - height*(a))
        cv.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows