#libraries
from PyQt5 import *
from PyQt5 import QtWidgets
import cv2
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import numpy as np
from tkinter import *
import tkinter as tk
import pyautogui as pg
import time
import pygetwindow
from PIL import Image
import numpy as np

video = cv2.VideoCapture(0)
#create main window object
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        title = "photogrammetry"
        # start_point = (0, 0)
        # end_point = (250, 250)
        # color = (0, 255, 0)
        # thickness = 9
        # image = cv2.line(video, start_point, end_point, color, thickness)
        # cv2.imshow(title, image)

        #self.setGeometry(0, 0, 500, 300)

        #create layout for q widget
        self.VBL = QVBoxLayout()
        self.setWindowTitle(title)

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.CancelBTN = QPushButton("Cancel")

        self.VBL.addWidget(self.CancelBTN)
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        #define worker1 thread in main program
        self.Worker1 = Worker1()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)

        self.ssBTN = QPushButton("Screenshot")
        self.VBL.addWidget(self.ssBTN)
        self.ssBTN.clicked.connect(self.screenshot)
       #self.VBL.addWidget(self.ssBTN)

        self.srBTN = QPushButton("Screenrecord")
        self.VBL.addWidget(self.srBTN)
        self.srBTN.clicked.connect(self.screenrecord)
        


    #change the pixmap displayed by feed label to value emmitted by worker1 (qthread)
    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker1.stop()
        time.sleep(0)
        cv2.destroyAllWindows()

    def screenshot(self):
            #titles = pygetwindow.getAllTitles() #prob dont need this
            random = int(time.time())
            file = "C:/Users/alyss/Downloads/" + str(random) + ".png"
            window = pygetwindow.getWindowsWithTitle('screenshot')[0]
            left, top = window.topleft
            right, bottom = window.bottomright
            pg.screenshot(file)
            im = Image.open(file)
            im = im.crop((left+19, top+42, right-19, bottom-106))
            im.save(file)
            im.show(file)

    def screenrecord(self):
            #cam = cv2.VideoCapture(0)
            width = int(video.get(3))
            height = int(video.get(4))
            fps = 20
            out = cv2.VideoWriter("C:/Users/alyss/Downloads/vid.avi", cv2.VideoWriter_fourcc('M','J', 'P', 'G'), fps, (width, height))

            while video.isOpened():
                ret, frame = video.read()
                if ret == True:
                    out.write(frame)
                    cv2.imshow('frame', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            
            #video.release()
            out.release()

            cv2.destroyWindow('frame')

#makes connection with camera and captures vid
class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    #define run function
    def run(self):
        self.ThreadActive = True
        #capture video
        #video = cv2.VideoCapture(0)
        # Read logo and resize
        # logo = cv2.imread(r'C:/Users/rosar/Downloads/redBar.png')
        # logo2 = cv2.imread(r'C:/Users/rosar/Downloads/redBar.png')
        # size = 150
        # logo = cv2.resize(logo, (size, 10), (600,600))
        # logo2 = cv2.resize(logo2, (size, 10), (500,500))
        # # Create a mask of logo
        # img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
        # img3gray = cv2.cvtColor(logo2, cv2.COLOR_BGR2GRAY)
        # ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
        # ret2, mask2 = cv2.threshold(img3gray, 1, 255, cv2.THRESH_BINARY) #probably dont need ret2
        
        while self.ThreadActive:
            if cv2.waitKey(1) == ord('q'):
                    break
            if video.isOpened() == False:
                 print("Failed to open video")
            # Region of Image (ROI), where we want to insert logo
            # roi = ((frame[200:150, 200:150]))
            # roi2 = ((frame[200:150, 200:150]))
            # roi = ((frame[-size-175:-175, -size-40:-40]))
            # roi2 = ((frame[-size-175:-175, -size-450:-450]))
            # # Set an index of where the mask is
            # roi[np.where(mask)] = 0
            # roi2[np.where(mask2)] = 0
            # roi += logo
            # roi2 += logo2
            # print(mask)
            # title = 'photogrammetry'
            # start_point = (0,0)
            # end_point = (250,250)
            # color = (0, 255, 0)
            # thickness = 9
            # bar = cv2.line(video, start_point, end_point, color, thickness)
            # cv2.imshow(title, bar)
            # cv2.line()
            ret, frame = video.read()
            # width = int(video.get(1))
            # height = int(video.get(2))
            bar = cv2.line(frame, (280, 200), (280, 300), (0, 255, 0,), 5)
            bar2 = cv2.line(frame, (355, 200), (355, 300), (0, 255, 0,), 5)
            cv2.imshow('screenshot', bar)
            cv2.imshow('screenshot', bar2)

            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                #emit thread
                self.ImageUpdate.emit(Pic)

    def stop(self):
        self.ThreadActive = False
        self.quit()

#initialize q main window
if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())