# import the require packages.
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QLabel, QGridLayout, QScrollArea, QSizePolicy, QWidget, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QImage, QPalette
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QEvent, QObject
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys
import time
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

#gets camera frames
class CaptureCam(QThread):
    ImageUpdate = pyqtSignal(QImage)

    def __init__(self, url):
        super(CaptureCam, self).__init__()
        self.url = url
        self.threadActive = True

    def run(self) -> None:
        capture = cv2.VideoCapture(self.url)

        if capture.isOpened():
            while self.threadActive:
                #
                ret, frame = capture.read()
                if self.url == 0:
                    frame = cv2.rotate(frame, cv2.ROTATE_180)
                # frame setup
                if ret:
                    height, width, channels = frame.shape
                    bytes_per_line = width * channels
                    cv_rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    qt_rgb_image = QImage(cv_rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
                    qt_rgb_image_scaled = qt_rgb_image.scaled(520, 480, Qt.KeepAspectRatio)
                        
                    self.ImageUpdate.emit(qt_rgb_image_scaled)
                else:
                    break
        capture.release()
        self.quit()

    def stop(self) -> None:
        self.threadActive = False

#ui setup
class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        #get camera streams
        self.url_1 = 1
        self.url_2 = 0

        #self.url_1 = 0
        #self.url_2 = 0
        #self.url_3 = 0
        #self.url_4 = 0

        self.list_cameras = {}

        self.camera_1 = QLabel()
        self.camera_1.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.camera_1.setScaledContents(True)
        self.camera_1.installEventFilter(self)
        self.camera_1.setObjectName("Camera_1")
        self.list_cameras["Camera_1"] = "Normal"

        self.QScrollArea_1 = QScrollArea()
        self.QScrollArea_1.setBackgroundRole(QPalette.Dark)
        self.QScrollArea_1.setWidgetResizable(True)
        self.QScrollArea_1.setWidget(self.camera_1)

        
        self.camera_2 = QLabel()
        self.camera_2.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.camera_2.setScaledContents(True)
        self.camera_2.installEventFilter(self)
        self.camera_2.setObjectName("Camera_2")
        self.list_cameras["Camera_2"] = "Normal"

        self.QScrollArea_2 = QScrollArea()
        self.QScrollArea_2.setBackgroundRole(QPalette.Dark)
        self.QScrollArea_2.setWidgetResizable(True)
        self.QScrollArea_2.setWidget(self.camera_2)

        self.camera1_label = QLabel("BACK GRIPPER", self)
        self.camera1_label.setStyleSheet("color: #F1F6FD")
        self.camera1_label.setAlignment(Qt.AlignCenter)
        self.camera2_label = QLabel("FRONT GRIPPER", self)
        self.camera2_label.setStyleSheet("color: #F1F6FD")
        self.camera2_label.setAlignment(Qt.AlignCenter)

        #screenshot stuff
        self.SSbutton = QPushButton("Screenshot", self)
        self.SSbutton.setToolTip('This is a screenshot button!')
        self.SSbutton.clicked.connect(self.screen_shot)

        self.__SetupUI()

        #connects to ImageUpdate to keep updating the frames
        self.CaptureCam_1 = CaptureCam(self.url_1)
        self.CaptureCam_1.ImageUpdate.connect(lambda image: self.ShowCamera1(image))

        self.CaptureCam_2 = CaptureCam(self.url_2)
        self.CaptureCam_2.ImageUpdate.connect(lambda image: self.ShowCamera2(image))

        #.start() runs the .run() function in CaptureCam that changes frame settings
        self.CaptureCam_1.start()
        self.CaptureCam_2.start()

    def __SetupUI(self):
        grid_layout = QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.addWidget(self.QScrollArea_1, 0, 0)
        grid_layout.addWidget(self.QScrollArea_2, 0, 1)
        grid_layout.addWidget(self.camera1_label, 1, 0)
        grid_layout.addWidget(self.camera2_label, 1, 1)

        #ss button
        grid_layout.addWidget(self.SSbutton)
       
        self.widget = QWidget(self)
        self.widget.setLayout(grid_layout)

        self.setCentralWidget(self.widget)
        self.setMinimumSize(1570, 1440)
        #self.showMaximized()
        self.setStyleSheet("QMainWindow {background: 'midnightblue';}")

        self.setWindowTitle("CAMERA GUI")

    @QtCore.pyqtSlot()
    def ShowCamera1(self, frame: QImage) -> None:
        self.camera_1.setPixmap(QPixmap.fromImage(frame))

    @QtCore.pyqtSlot()
    def ShowCamera2(self, frame: QImage) -> None:
        self.camera_2.setPixmap(QPixmap.fromImage(frame))

#screenshot function
    def screen_shot(self):
        random = int(time.time())
        file = "C:/Users/rosar/Downloads/guiSS/" + str(random) + ".png"
        window = pygetwindow.getWindowsWithTitle('CAMERA GUI')[self.url_2]
        left, top = window.topleft
        right, bottom = window.bottomright
        pg.screenshot(file)
        im = Image.open(file)
        im = im.crop((left+695, top, right-15, bottom-60))
        im.save(file)
        im.show(file)

# funtcion maximizes certain windows when double clicked
    def eventFilter(self, source: QObject, event: QEvent):
        if event.type() == QtCore.QEvent.MouseButtonDblClick:
            if source.objectName() == 'Camera_1':
                if self.list_cameras["Camera_1"] == "Normal":
                    self.QScrollArea_2.hide()
                    self.QScrollArea_3.hide()
                    self.QScrollArea_4.hide()
                    self.camera2_label.hide()
                    self.camera3_label.hide()
                    self.camera4_label.hide()
                    self.list_cameras["Camera_1"] = "Maximized"
                else:
                    self.QScrollArea_2.show()
                    self.QScrollArea_3.show()
                    self.QScrollArea_4.show()
                    self.camera2_label.show()
                    self.camera3_label.show()
                    self.camera4_label.show()
                    self.list_cameras["Camera_1"] = "Normal"
            elif source.objectName() == 'Camera_2':
                if self.list_cameras["Camera_2"] == "Normal":
                    self.QScrollArea_1.hide()
                    self.QScrollArea_3.hide()
                    self.QScrollArea_4.hide()
                    self.camera1_label.hide()
                    self.camera3_label.hide()
                    self.camera4_label.hide()
                    self.list_cameras["Camera_2"] = "Maximized"
                else:
                    self.QScrollArea_1.show()
                    self.QScrollArea_3.show()
                    self.QScrollArea_4.show()
                    self.camera1_label.show()
                    self.camera3_label.show()
                    self.camera4_label.show()
                    self.list_cameras["Camera_2"] = "Normal"
            else:
                return super(MainWindow, self).eventFilter(source, event)
            return True
        else:
            return super(MainWindow, self).eventFilter(source, event)

    def close(self, event):
        if self.CaptureCam_1.isRunning():
            self.CaptureCam_1.quit()
        if self.CaptureCam_2.isRunning():
            self.CaptureCam_2.quit()
        event.accept()


#runs window
def main():
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
    main()