import cv2

video1 = cv2.VideoCapture("http://192.168.1.99:8084/stream")


while video1.isOpened():
    ret, frame = video1.read()
    if ret == True:
        #scv2.imshow('frame!', frame)
        #cam = \cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow("camera 3", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
