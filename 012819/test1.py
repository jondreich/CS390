#!/usr/bin/python3
import sys
import numpy as np
import cv2 as cv
import pytesseract as pt
from PIL import Image
from pytesseract import image_to_string

def getImagePath():
	return cv.imread('img/')

def readText(img_path):
	img = cv.imread(img_path)
	img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

	kernel = np.ones((1,1), np.uint8)
	img = cv.dilate(img, kernel, iterations=1)
	img = cv.erode(img, kernel, iterations=1)

	cv.imwrite(file_path + "noiseless.png", img)
	cv.imwrite(file_path + "thres.png", img)

	return pt.image_to_string(Image.open(file_path + "thres.png"))


file_path = 'img/'
print(readText(file_path + "graph1.PNG"))