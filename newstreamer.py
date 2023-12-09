
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2

#create a holder for the url


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 800, 600)

        self.VBL = QGridLayout()

        self.FeedLabel = QLabel()
        self.FeedLabel.setToolTip("feedlabel")
        self.FeedLabel.show()

        self.CancelBTN = QPushButton("cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)

        self.Worker = Worker() #create a worker cam object

        self.Worker.start()
        self.Worker.ImageUpdate.connect(self.ImageUpdateSlot)
        
    
    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker.stop()

class Worker(QThread):
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
