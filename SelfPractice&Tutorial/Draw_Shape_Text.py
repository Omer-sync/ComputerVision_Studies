import cv2 as cv
import numpy as np

# Creating a palette
# blank = np.zeros((500,500,3),dtype='uint8')
#
# cv.imshow('Black',blank)
#
# blank[200:300,10:80] = 0,255,0
# cv.imshow('Green_part',blank)
#
# blank[:] = 0,255,0
# cv.imshow('Green',blank)

# 1.Drawing Rectangle

blank = np.zeros((500,500,3),dtype='uint8')

# cv.rectangle(blank,(0,0),(255,255),(0,0,255),thickness=1)
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=-1)
cv.rectangle(blank,(0,0),(255,255),(0,0,255),thickness=cv.FILLED)

cv.imshow('Rectangle',blank)

# 2.Drawing Circle

cv.circle(blank,(250,250),50,color = (120,150,20),thickness=1)
cv.imshow('Circle',blank)

# 3. Drawing Line

cv.line(blank,(0,250),(500,250),(120,160,20),thickness=4)

cv.imshow('Line',blank)

# 4. Put Text

cv.putText(blank,'Hello World',(250,400),cv.FONT_ITALIC,1.2,(240,0,0),thickness=3)
cv.imshow('Text',blank)
cv.waitKey(0)