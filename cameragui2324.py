import time
import typing
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import os
import sys

from PyQt5.QtWidgets import QWidget

#main window class
class MainWindow(QMainWindow):
    
    #self constructor
    def __init__(self):
        super().__init__()

        #setting geometry
        self.setGeometry(100, 100, 800, 600)

        #set the style sheet
        self.setStyleSheet("background : lightgrey;")

        #get the available cameras
        self.available_cameras = QCameraInfo.availableCameras()

        print(self.available_cameras)

        #if no camera found
        if not self.available_cameras:
            #exit the code
            sys.exit() #does this just mean exit system?

        #create a status bar
        self.status = QStatusBar()

        #set the stylesheet to the status bar
        self.status.setStyleSheet("background : white;")

        #add the status bar to the main window
        self.setStatusBar(self.status)

        #path to save
        self.save_path = ""

        #create a camera viewfinder object
        self.viewfinder = QCameraViewfinder()

        #show the viewfinder
        self.viewfinder.show()

        #make the central widget of main window
        self.setCentralWidget(self.viewfinder)

        #set default camera
        self.select_camera(0) #this sets it to webcam

        #create a tool bar
        toolbar = QToolBar("camera tool bar")

        #add tool bar to mian window
        self.addToolBar(toolbar)

        #create a photo action (take pic)
        clickaction = QAction("click photo", self)

        #adding status tip to the photo action
        clickaction.setStatusTip("this will capture picture")

        #adding tool tip
        clickaction.setToolTip("capture picture")

        
        #adding action baybeeee
        #calling take_photo method
        clickaction.triggered.connect(self.click_photo)

        #adding this to the tool bar
        toolbar.addAction(clickaction)


        #creating a combo box for selecting camera
        camera_selector = QComboBox()

        #adding status tip to it
        camera_selector.setStatusTip("choose camera to take pictures")

        #adding tooltip to it
        camera_selector.setToolTip("select camera")
        camera_selector.setToolTipDuration(2500)

        #adding items to the combo box
        camera_selector.addItems([camera.description()
                                  for camera in self.available_cameras])
        
        #adding action to the combo box
        #calling the select camera method
        camera_selector.currentIndexChanged.connect(self.select_camera)

        #adding to tool bar
        toolbar.addWidget(camera_selector)

        #setting tool bar stylesheet
        toolbar.setStyleSheet("background : white;")


        #setting window title
        self.setWindowTitle("pyqt5 cam")

        #show the main window
        self.show()

    #method to select camera
    def select_camera(self, i):

        #getting the selected camera
        self.camera = QCamera(self.available_cameras[i])

        #setting the view finder to the camera
        self.camera.setViewfinder(self.viewfinder)

        #setting capture mode to the camera
        self.camera.setCaptureMode(QCamera.CaptureStillImage)

        #show the alert for any error
        self.camera.error.connect(lambda: self.alert(self.camera.errorString()))

        #start the camera
        self.camera.start()

        #creating an image capture object
        self.capture = QCameraImageCapture(self.camera)

        #showing alert if error occur
        self.capture.error.connect(lambda error_msg, error, msg: self.alert(msg))

        #when image captured showing message
        self.capture.imageCaptured.connect(lambda d, 
                                           i: self.status.showMessage("image captured : "
                                                                      + str(self.save_seq)))
        
        #getting current camera name
        self.current_camera_name = self.available_cameras[i].description()

        #initial save sequence
        self.save_seq = 0

    #method to take photo
    def click_photo(self):

        #time stamp
        timestamp = time.strftime("%d-%b-%Y-%H_%M_%S")

        #capture the image and save it on the save path
        self.capture.capture(os.path.join(self.save_path,
                                          "%s-%04d-%s.jpg" % (
            self.current_camera_name,
            self.save_seq,
            timestamp 
            )))
        
        #increment the sequence
        self.save_seq += 1

    #change folder method
    def change_folder(self):
        
        #open the dialog to select path
        path = QFileDialog.getExistingDirectory(self,
                                                "picture location", "")
        
        #if path is selected
        if path: 

            #update the path
            self.save_path = path
            
            #update the sequence
            self.save_seq = 0

    #method for alerts
    def alert(self, msg):

        #error message
        error = QErrorMessage(self)

        #setting text to the error message
        error.showMessage(msg)

#driver code
if __name__ == "__main__" :

    #create pyqt5 app
    app = QApplication(sys.argv)

    #create the instance of our window
    window = MainWindow()

    #start the app
    sys.exit(app.exec())