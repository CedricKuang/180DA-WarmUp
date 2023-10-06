'''
The following code snippet is from the OpenCV official tutorial:
https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html

'''


import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    # define range of blue color in HSV
    # lower_blue = np.array([110,50,50])
    # upper_blue = np.array([130,255,255])

    lower_blue = np.array([0,0,150])
    upper_blue = np.array([120,120,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)

    # These codes are added by myself
    # draw the localization box of white object using contor
    gray_frame = cv.cvtColor(hsv, cv.COLOR_RGB2GRAY)
    ret,thresh = cv.threshold(gray_frame,127,255,0)
    contours,hierarchy = cv.findContours(thresh, 1, 2)
    
    try:
        cnt = contours[0]
    except:
        pass
    else:
        x,y,w,h = cv.boundingRect(cnt)
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    # These codes are added by myself

    
    cv.imshow('frame',frame)
    # cv.imshow('mask',mask)
    # cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()