#https://laury.dev/snippets/manually-control-webcam-using-command-line-linux/
import cv2

video1 = 0

while video1.isOpened():
    ret, frame = video1.read()
    if ret == True:
        #cv2.imshow('frame!', frame)git s
        cam = cv2.rotate(frame, cv2.ROTATE_180)
        cv2.imshow("back gripper", cam)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break