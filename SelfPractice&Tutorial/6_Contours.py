import cv2 as cv
import numpy as np

# Reading in an image
img = cv.imread("D:/Programming/Python_Projects/Computer_Vision/Resources/Image/messi.png")

cv.imshow('Messi',img)

blank = np.zeros(img.shape,dtype='uint8')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Messi_Gray',gray)


canny = cv.Canny(img,125,175)
cv.imshow('Messi_Canny',canny)

ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresholded',thresh)

contours,hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours are found')

cv.drawContours(blank,contours,-1,(0,0,255),thickness=1)
cv.imshow('Counters Drawn',blank)
cv.waitKey(0)
