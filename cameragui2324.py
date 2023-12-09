
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2

#create a holder for the url


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setStyleSheet("background-color: grey;")

        self.VBL = QVBoxLayout()

        self.feed = QLabel(self)
        self.feed.setToolTip("feedlabel")
        self.feed.setGeometry(125, 350, 400, 170)
        
        self.VBL.addWidget(self.feed)

        #self.FeedLabel2 = QLabel()
        #self.FeedLabel2.setToolTip("feedlabel2")
       # self.VBL.addWidget(self.FeedLabel2)
        

        self.CancelBTN = QPushButton("cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

       # self.Worker = Worker() #create a worker cam object
        self.Worker1 = Worker1()
        #self.Worker1.move(1400, 220) 

       # self.Worker.start()
        #self.Worker.ImageUpdate.connect(self.ImageUpdateSlot)
        

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)

    
    def ImageUpdateSlot(self, Image):
        self.feed.setPixmap(QPixmap.fromImage(Image))
        

    def CancelFeed(self):
        #self.Worker.stop()
        self.Worker1.stop()

class Worker(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        capture = cv2.VideoCapture("http://192.168.1.99:8080/stream")
        while self.ThreadActive:
            ret, frame = capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1) #mirrors
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1],
                                           FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
                #capture.release()
    def stop(self):
        self.ThreadActive = False
        self.quit()

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1) #mirrors
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1],
                                           FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
                #capture.release()
    def stop(self):
        self.ThreadActive = False
        self.quit()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = MainWindow()
    root.show()
    sys.exit(app.exec())
