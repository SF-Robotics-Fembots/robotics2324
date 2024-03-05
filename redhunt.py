#importing packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils #why do we do this twice?
import time

#argparse moment
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
                help="path to the optional video file?")
ap.add_argument("-b", "--buffer", type=int, default=64, 
                help="max buffer size")
args = vars(ap.parse_args())

#masking, defining the lower and upper boundaries
#using hsv color space, then initialize tracked points
red_lower = (0, 0, 38)
red_upper = (36, 19,255)

pts = deque(maxlen=args["buffer"])
#this uses argparse to look for the argument
#"buffer" and sets maxlen to that value (64 in this case)

#if a video path was not supplied, grab webcam
#in theory, you should be able to change
#the path of src="whatever the video link is"
if not args.get("video", False):
    vs = VideoStream(src=0).start()

#otherwise, grab a reference to video file
else:
    vs = cv2.VideoCapture(args["video"])

#allow the cam / video file to warm up
time.sleep(2)

#time for the while true lol
while True:
    #grab current frame
    frame = vs.read()

    #handle frame from VideoCapture / VideoStream
    frame = frame[1] if args.get("video", False) else frame
    #that's a strange if/else statement lol

    #end of video to exit loop
    if frame is None:
        break
    print("before frame")
    #resize frame, blur, & convert to hsv
    frame = imutils.resize(frame, width=600, height=600)
    print("before blur")
    blur = cv2.GaussianBlur(frame, (11, 11), 0)
    print("before hsv")
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    print("after hsv")
    time.sleep(2)

    #construct mask for red (I KNEW IT)
    #dilate & erode to remove holes
    mask = cv2.inRange(hsv, red_lower, red_upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    print("after mask")
    time.sleep(2)

    #contour time!
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    center = None
    print("after contours")

    if len(contours) > 0: #do this if they exist
        #find largest in mask then use to compute
        #minimum enclosing circle and centroid (?)
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        moment = cv2.moments(c) 
        center = (int(moment["m10"] / moment["m00"]), 
                  int(moment["m01"] / moment["m00"]))
        
        #only proceed if radius meets minimum size
        if radius > 10:
            #draw circle & centroid on frame
            #then update list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius),
                       (255, 255, 0), 2)
            cv2.circle(frame, center, 5, (255, 0, 0), -1)

        #update points queue
        pts.appendleft(center)

        #loop over the set of tracked points
        for i in range(1, len(pts)):
            #ignore if tracked pts are None
            if pts[i-1] is None or pts[i] is None:
                continue

            #otherwise draw line thickness +
            #connecting lines
            thickness = int(np.sqrt(args["buffer"] / float(i+1)) * 2.5)
            cv2.line(frame, pts[i-1], pts[i], (255, 0, 0), thickness)
        
        print("showing frame")
        time.sleep(2)
        #show frame to screen
        
        print("frame up")
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1) & 0xFF

        #if 'q' pressed, stop loop
        if key == ord('q'):
            break

    #if not video file, stop cam stream
    #if not args.get("video", False):
     #   vs.stop()
    
    #otherwise, release camera
    else:
        vs.release()

    #close all the windows!
    cv2.destroyAllWindows()

