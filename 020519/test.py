import cv2 as cv
import numpy as np

img = cv.imread("img/minecraft.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
img[:][:][0] = img[:][:][0] + 100
#img = cv.cvtColor(img, cv.COLOR_HSV2BGR)

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows