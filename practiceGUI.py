import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QLabel, QGridLayout, QScrollArea, QSizePolicy
from PyQt5.QtGui import QPixmap, QIcon, QImage, QPalette
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QEvent, QObject
from PyQt5 import QtCore
import sys
import threading
import os
import subprocess 
import logging
import socket

class CaptureCam(QThread):
    ImageUpdate = pyqtSignal(QImage)
    ImageUpdate1 = pyqtSignal(QImage)

    def __init__(self, camera_id):
        super(CaptureCam, self).__init__()
        self.ThreadActive = True
      #  self.ThreadActive1 = True
        self.camera_id = 0
        if self.camera_id == 0:
            self.camera = 0
        #elif self.camera_id == 1:
           # self.camera = "http://192.168.1.99:8080/stream"
        
    def run(self, num) -> None:
        self.ThreadActive = False
        capture1 = cv2.VideoCapture(num)
     #  capture2 = cv2.VideoCapture(0)
        #list = [capture1, capture2]
        while self.ThreadActive:
                #ret is boolean to see if there is a return of frame, frame is the return of frame
                ret, frame = capture1.read()
                #ret1, frame1 = capture2.read()

                if ret:
                    Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    FlippedImage = cv2.flip(Image, 1) #mirrors
                    ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1],
                                            FlippedImage.shape[0], QImage.Format_RGB888)
                    Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                    self.ImageUpdate.emit(Pic)
                else:
                    break

    def camprint(self):
        print("is running")
#    def run2(self) -> None:

 #               if ret1:
 #                   Image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
 #                   FlippedImage1 = cv2.flip(Image1, 1) #mirrors
 #                   ConvertToQtFormat1 = QImage(FlippedImage1.data, FlippedImage1.shape[1],
 #                                       FlippedImage1.shape[0], QImage.Format_RGB888)
 #                   Pic1 = ConvertToQtFormat1.scaled(640, 480, Qt.KeepAspectRatio)
 #                   self.ImageUpdate1.emit(Pic1)


    #hconcat
    #cam1 = threading.Thread(target= run, args=())
   # cam2 = threading.Thread(target = run2, args=())

    #cam1.start()
    #cam2.start()

    #cam1.join()
    #cam2.join()

    def stop(self):
        self.ThreadActive = False
       # self.ThreadActive1 = False
        self.quit()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        #self.camera_1 = 2
        #self.camera_2 = cv2.VideoCapture('dev/video[0]')

        self.camera_1 = QLabel()
        self.camera_1.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.camera_1.setScaledContents(True)
        self.camera_1.installEventFilter(self)
        self.camera_1.setObjectName("Camera_1")

        self.QScrollArea_1 = QScrollArea()
        self.QScrollArea_1.setBackgroundRole(QPalette.Dark)
        self.QScrollArea_1.setWidgetResizable(True)
        self.QScrollArea_1.setWidget(self.camera_1)

        self.camera_2 = QLabel()
        self.camera_2.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.camera_2.setScaledContents(True)
        self.camera_2.installEventFilter(self)
        self.camera_2.setObjectName("Camera_2")

        self.QScrollArea_2 = QScrollArea()
        self.QScrollArea_2.setBackgroundRole(QPalette.Dark)
        self.QScrollArea_2.setWidgetResizable(True)
        self.QScrollArea_2.setWidget(self.camera_2)

        self.SetupUI()

        self.CaptureCam_1 = CaptureCam(self.camera_1)
        self.CaptureCam_1.ImageUpdate.connect(lambda image: self.ShowCamera1(image))

        self.CaptureCam_2 = CaptureCam(self.camera_2)
        self.CaptureCam_2.ImageUpdate1.connect(lambda image: self.ShowCamera2(image))

        self.CaptureCam_1.run(0)
        self.CaptureCam_1.camprint()
        #self.CaptureCam_2.start()
        #self.CaptureCam_1.camrun(0)
        #self.CaptureCam_2.run(1)

    def SetupUI(self):
        grid_layout = QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.addWidget(self.QScrollArea_1, 0, 0)
        grid_layout.addWidget(self.QScrollArea_2, 0, 1)
    
        self.widget = QWidget(self)
        self.widget.setLayout(grid_layout)

        self.setCentralWidget(self.widget)
        self.setMinimumSize(800, 600)
        self.showMaximized()
        self.setStyleSheet("QMainWindow {background: 'black';}")
        self.setWindowTitle("Camera GUI")

    @QtCore.pyqtSlot()
    def ShowCamera1(self, frame: QImage) -> None:
        self.camera_1.setPixmap(QPixmap.fromImage(frame))

    @QtCore.pyqtSlot()
    def ShowCamera2(self, frame1: QImage) -> None:
        self.camera_2.setPixmap(QPixmap.fromImage(frame1))    

def main() -> None:
    # Create a QApplication object. It manages the GUI application's control flow and main settings.
    # It handles widget specific initialization, finalization.
    # For any GUI application using Qt, there is precisely one QApplication object
    app = QApplication(sys.argv)
    # Create an instance of the class MainWindow.
    window = MainWindow()
    # Show the window.
    window.show()
    # Start Qt event loop.
    sys.exit(app.exec_())

if __name__ == '__main__':
    #getCamsInfo()
    main()