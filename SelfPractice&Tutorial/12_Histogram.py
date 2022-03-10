import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("D:/Programming/Python_Projects/Computer_Vision/ROV/FishSize/Source/" + "samplefromvideo_1.png")

cv.imshow('Park',img)

# Grayscale Histogram

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# Masked Grayscale Histogram

# blank = np.zeros(img.shape[0:2],dtype='uint8')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)
#
# mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
#
# masked = cv.bitwise_and(gray,gray,mask=mask)
# cv.imshow('Mask', masked)
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256] )
# plt.figure()
# plt.title("GrayScale Histogram")
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Colorful Histogram

blank = np.zeros(img.shape[0:2],dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Mask', masked)

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)