import cv2 as cv

# Read in an image

img = cv.imread("D:/Programming/Python_Projects/Computer_Vision/ROV/FishSize/Source/" + "all_fish.PNG")
cv.imshow('Normal',img)


# Grayscaled

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Blurred

blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Edge Cascade

canny  = cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)

# Dilating the image

dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)