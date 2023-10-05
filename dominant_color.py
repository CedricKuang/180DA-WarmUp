'''
The following code snippet is from the OpenCV official tutorial:
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html

And a tutorial for dominant color:
https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097

'''

import numpy as np
import cv2
from sklearn.cluster import KMeans

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame = frame.reshape((frame.shape[0] * frame.shape[1],3)) #represent as row*column,channel number
    clt = KMeans(n_clusters=3) #cluster number
    clt.fit(frame)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()