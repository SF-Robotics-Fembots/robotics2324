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

#create main window object
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        title = "photogrammetry"
        #video = cv2.VideoCapture(0)
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
        #self.Worker1 = Worker1()

        #self.Worker1.start()
       # self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
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
        #self.Worker1.stop()
        time.sleep(0)
        cv2.destroyAllWindows()

    def screenshot(self):
            #titles = pygetwindow.getAllTitles() #prob dont need this
            random = int(time.time())
            file = "C:/Users/rosar/Downloads/guiSS/" + str(random) + ".png"
            window = pygetwindow.getWindowsWithTitle('photogrammetry')[0]
            left, top = window.topleft
            right, bottom = window.bottomright
            pg.screenshot(file)
            im = Image.open(file)
            im = im.crop((left+19, top+42, right-19, bottom-106))
            im.save(file)
            im.show(file)
            
    def screenrecord(self):
            cam = cv2.VideoCapture(0)
            width = int(cam.get(3))
            height = int(cam.get(4))
            fps = 20
            out = cv2.VideoWriter("C:/Users/alyss/Downloads/vid.avi", cv2.VideoWriter_fourcc('M','J', 'P', 'G'), fps, (width, height))

            while cam.isOpened():
                retu, frameu = cam.read()
                if retu == True:
                    out.write(frameu)
                    cv2.imshow('frameu', frameu)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                    else:
                        break
            
            cam.release()
            out.release()

            cv2.destroyWindow('frameu')

#makes connection with camera and captures vid

#initialize q main window
if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())