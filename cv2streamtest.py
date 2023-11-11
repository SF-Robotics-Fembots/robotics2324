import cv2

video1 = cv2.VideoCapture("http://192.168.1.99:8080/stream")

while video1.isOpened():
    ret, frame = video1.read()
    if ret == True:
        cv2.imshow('frame!', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
