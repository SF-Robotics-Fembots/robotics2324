#https://laury.dev/snippets/manually-control-webcam-using-command-line-linux/
import cv2

video1 = cv2.VideoCapture("http://192.168.1.99:8080/stream")


while video1.isOpened():
    ret, frame = video1.read()
    if ret == True:
        #cv2.imshow('frame!', frame)git s
        cam = cv2.rotate(frame, cv2.ROTATE_180)
        cv2.imshow("back gripper", cam)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
