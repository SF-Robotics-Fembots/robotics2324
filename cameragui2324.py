# import the require packages.
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QLabel, QGridLayout, QScrollArea, QSizePolicy
from PyQt5.QtGui import QPixmap, QIcon, QImage, QPalette
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QEvent, QObject
from PyQt5 import QtCore
import sys


class CaptureCam(QThread):
    # Signal emitted when a new image or a new frame is ready.
    ImageUpdated = pyqtSignal(QImage)

    def __init__(self, url) -> None:
        super(CaptureCam, self).__init__()
        # Declare and initialize instance variables.
        self.url = url
        self.__thread_active = True
        self.fps = 0
        self.__thread_pause = False

    def run(self) -> None:
        # Capture video from a network stream.
        cap = cv2.VideoCapture(self.url)
        # If video capturing has been initialized already.q
        if cap.isOpened():
            # While the thread is active.
            while self.__thread_active:
                #
                ret, frame = cap.read()
                # If frame is read correctly.
                if ret:
                    height, width, channels = frame.shape
                    bytes_per_line = width * channels
                    cv_rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    qt_rgb_image = QImage(cv_rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
                    qt_rgb_image_scaled = qt_rgb_image.scaled(1280, 720, Qt.KeepAspectRatio)
                    self.ImageUpdated.emit(qt_rgb_image_scaled)
                else:
                    break
        cap.release()
        self.quit()

    def stop(self) -> None:
        self.__thread_active = False

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        self.url_1 = cv2.VideoCapture('http://192.168.1.99:8080/stream')
        self.url_2 = cv2.VideoCapture("http://192.168.1.99:8082/stream")
        self.url_3 = cv2.VideoCapture("http://192.168.1.99:8084/stream")
        self.url_4 = 0

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

    
        self.camera_3 = QLabel()
        self.camera_3.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.camera_3.setScaledContents(True)
        self.camera_3.installEventFilter(self)
        self.camera_3.setObjectName("Camera_3")
        self.list_cameras["Camera_3"] = "Normal"

        self.QScrollArea_3 = QScrollArea()
        self.QScrollArea_3.setBackgroundRole(QPalette.Dark)
        self.QScrollArea_3.setWidgetResizable(True)
        self.QScrollArea_3.setWidget(self.camera_3)


        self.camera_4 = QLabel()
        self.camera_4.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.camera_4.setScaledContents(True)
        self.camera_4.installEventFilter(self)
        self.camera_4.setObjectName("Camera_4")
        self.list_cameras["Camera_4"] = "Normal"

        self.QScrollArea_4 = QScrollArea()
        self.QScrollArea_4.setBackgroundRole(QPalette.Dark)
        self.QScrollArea_4.setWidgetResizable(True)
        self.QScrollArea_4.setWidget(self.camera_4)

        self.__SetupUI()

        self.CaptureCam_1 = CaptureCam(self.url_1)
        self.CaptureCam_1.ImageUpdated.connect(lambda image: self.ShowCamera1(image))

        self.CaptureCam_2 = CaptureCam(self.url_2)
        self.CaptureCam_2.ImageUpdated.connect(lambda image: self.ShowCamera2(image))

        self.CaptureCam_3 = CaptureCam(self.url_3)
        self.CaptureCam_3.ImageUpdated.connect(lambda image: self.ShowCamera3(image))

        self.CaptureCam_4 = CaptureCam(self.url_4)
        self.CaptureCam_4.ImageUpdated.connect(lambda image: self.ShowCamera4(image))

        self.CaptureCam_1.start()
        self.CaptureCam_2.start()
        self.CaptureCam_3.start()
        self.CaptureCam_4.start()

    def __SetupUI(self):
        grid_layout = QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.addWidget(self.QScrollArea_1, 0, 0)
        grid_layout.addWidget(self.QScrollArea_2, 0, 1)
        grid_layout.addWidget(self.QScrollArea_3, 1, 0)
        grid_layout.addWidget(self.QScrollArea_4, 1, 1)

        self.widget = QWidget(self)
        self.widget.setLayout(grid_layout)

        self.setCentralWidget(self.widget)
        self.setMinimumSize(800, 600)
        self.showMaximized()
        self.setStyleSheet("QMainWindow {background: '#F1F6FD';}")
        self.setWindowIcon(QIcon(QPixmap("camera_2.png")))

        self.setWindowTitle("CAMERA GUI")

    @QtCore.pyqtSlot()
    def ShowCamera1(self, frame: QImage) -> None:
        self.camera_1.setPixmap(QPixmap.fromImage(frame))

    @QtCore.pyqtSlot()
    def ShowCamera2(self, frame: QImage) -> None:
        self.camera_2.setPixmap(QPixmap.fromImage(frame))

    @QtCore.pyqtSlot()
    def ShowCamera3(self, frame: QImage) -> None:
        self.camera_3.setPixmap(QPixmap.fromImage(frame))

    @QtCore.pyqtSlot()
    def ShowCamera4(self, frame: QImage) -> None:
        self.camera_4.setPixmap(QPixmap.fromImage(frame))

    def eventFilter(self, source: QObject, event: QEvent) -> bool:
        if event.type() == QtCore.QEvent.MouseButtonDblClick:
            if source.objectName() == 'Camera_1':
                if self.list_cameras["Camera_1"] == "Normal":
                    self.QScrollArea_2.hide()
                    self.QScrollArea_3.hide()
                    self.QScrollArea_4.hide()
                    self.list_cameras["Camera_1"] = "Maximized"
                else:
                    self.QScrollArea_2.show()
                    self.QScrollArea_3.show()
                    self.QScrollArea_4.show()
                    self.list_cameras["Camera_1"] = "Normal"
            elif source.objectName() == 'Camera_2':
                if self.list_cameras["Camera_2"] == "Normal":
                    self.QScrollArea_1.hide()
                    self.QScrollArea_3.hide()
                    self.QScrollArea_4.hide()
                    self.list_cameras["Camera_2"] = "Maximized"
                else:
                    self.QScrollArea_1.show()
                    self.QScrollArea_3.show()
                    self.QScrollArea_4.show()
                    self.list_cameras["Camera_2"] = "Normal"
            elif source.objectName() == 'Camera_3':
                if self.list_cameras["Camera_3"] == "Normal":
                    self.QScrollArea_1.hide()
                    self.QScrollArea_2.hide()
                    self.QScrollArea_4.hide()
                    self.list_cameras["Camera_3"] = "Maximized"
                else:
                    self.QScrollArea_1.show()
                    self.QScrollArea_2.show()
                    self.QScrollArea_4.show()
                    self.list_cameras["Camera_3"] = "Normal"
            elif source.objectName() == 'Camera_4':
                if self.list_cameras["Camera_4"] == "Normal":
                    self.QScrollArea_1.hide()
                    self.QScrollArea_2.hide()
                    self.QScrollArea_3.hide()
                    self.list_cameras["Camera_4"] = "Maximized"
                else:
                    self.QScrollArea_1.show()
                    self.QScrollArea_2.show()
                    self.QScrollArea_3.show()
                    self.list_cameras["Camera_4"] = "Normal"
            else:
                return super(MainWindow, self).eventFilter(source, event)
            return True
        else:
            return super(MainWindow, self).eventFilter(source, event)

    def close(self, event) -> None:
        if self.CaptureCam_1.isRunning():
            self.CaptureCam_1.quit()
        if self.CaptureCam_2.isRunning():
            self.CaptureCam_2.quit()
        if self.CaptureCam_3.isRunning():
            self.CaptureCam_3.quit()
        event.accept()


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
    main()