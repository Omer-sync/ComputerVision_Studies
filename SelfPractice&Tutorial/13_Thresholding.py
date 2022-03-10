import cv2 as cv
import numpy as np

# img = cv.imread("D:/Programming/Python_Projects/Computer_Vision/Resources/Image/park.jfif")
img = cv.imread("D:/Programming/Python_Projects/Computer_Vision/ROV/FishSize/Source/" + "samplefromvideo_1.png")
cv.imshow('Park',img)

B,G,R = cv.split(img)
zeros = np.zeros(img.shape[:2], dtype="uint8")

img = cv.merge([zeros,G,R])
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY )
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV )
cv.imshow('Simple Thresholded Inverse', thresh_inv)
# cv.imwrite('D:/Programming/Python_Projects/Computer_Vision/ROV/FishSize/Source/one_fish.png',thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)