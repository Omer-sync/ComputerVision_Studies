import cv2 as cv
import numpy as np
# Reading in an image
img = cv.imread("D:/Programming/Python_Projects/Computer_Vision/Resources/Image/messi.png")

cv.imshow('Messi',img)

# Translation on x-y axis

def translate(img,x,y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return  cv.warpAffine(img,transmat,dimensions)

translated = translate(img,100,100)

cv.imshow('Translated',translated)

# Rotation

def rotate(img,angle,rotpoint=None):
    (height,width) = img.shape[:2]

    if rotpoint is None:
        rotpoint = (width//2,height//2)

    rotmat = cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotmat,dimensions)

rotated = rotate(img,90)

cv.imshow('Rotated',rotated)

# Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_LINEAR)

cv.imshow('Resized',resized)

# Flip
flipped = cv.flip(img,1)
cv.imshow('Flipped',flipped)


cv.waitKey(0)

