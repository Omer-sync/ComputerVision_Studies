import cv2 as cv
import numpy as np

img = cv.imread("D:/Programming/Python_Projects/Computer_Vision/Resources/Image/messi_crowd.jpg")
img2 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
template = cv.imread("D:/Programming/Python_Projects/Computer_Vision/Resources/Image/partofmessi.jpg",0)
cv.imshow('Coin',template)
w,h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

# Single Detection
# for meth in methods:
#     img = img2.copy()
#     method = eval(meth)
#
#
#     # Apply template Matching
#     res = cv.matchTemplate(img,template,method)
#     min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
#
#     # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#     if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
#         top_left = min_loc
#     else:
#         top_left = max_loc
#
#     bottom_right = (top_left[0] + w, top_left[1] + h)
#     cv.rectangle(img,top_left, bottom_right, 255, 2)
#
#     cv.imshow(f'Matching Result {meth}',res)
#
#     cv.imshow(f'Detected Point{meth}', img)

# Multiple Detection

res = cv.matchTemplate(img2,template,cv.TM_CCOEFF_NORMED)
cv.imshow('points',res)
threshold = 0.9
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv.imshow('Matched',img)
cv.waitKey(0)


# [220 221 222 223 220 221 222 223 220 221 295 296 297 298 595 596 597 598
#  295 296 297 298 594 595 596 597 521 522 519 520 521 522 523 519 520 521
#  522 523 595 596 597 598 446 447 594 595 596 597 598 446 593 594 595 596
#  597 598 520 521 522 523 519 520 521 522 523 519 520 521 522  52  53  54
#   52 445 446 447 448 594 595 596 597 598 444 445 446 447 448 594 595 596
#  597 598 444 445 446 447 593 594 595 596 597] [ 35  35  35  35  36  36  36  36  37  37  71  71  71  71  71  71  71  71
#   72  72  72  72  72  72  72  72 106 106 107 107 107 107 107 108 108 108
#  108 108 142 142 142 142 143 143 143 143 143 143 143 144 144 144 144 144
#  144 144 178 178 178 178 179 179 179 179 179 180 180 180 180 188 188 188
#  189 214 214 214 214 214 214 214 214 214 215 215 215 215 215 215 215 215
#  215 215 216 216 216 216 216 216 216 216 216]