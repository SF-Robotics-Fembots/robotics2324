#finding the red coordinates on a screen using cv2 and giving the coordinates
import time
import numpy as np
import cv2


capture = cv2.VideoCapture(0)

#define the color you want to find, BGR for cv2
lower1 = np.array([0, 5, 20])
upper1 = np.array([10, 255, 255])

# upper boundary RED color range values; Hue (160 - 180)
lower2 = np.array([160, 5, 20])
upper2 = np.array([179, 255, 255])

#

while capture.isOpened():
    ret, frame = capture.read()
    if ret == True:
        #cv2.imshow('frame!', frame)
        # lower boundary RED color range values; Hue (0 - 10)


        #lower_mask = cv2.inRange(frame, lower1, upper1)
        #upper_mask = cv2.inRange(frame, lower2, upper2)

        #full_mask = lower_mask + upper_mask
        redpx = np.argwhere(cv2.inRange(frame, (0,0,250), (0,0,255)))
        
        cv2.imshow("frame", frame)

        for px, py in redpx:
            cv2.circle(frame, (py, px), 5, (0, 255, 255), 1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
