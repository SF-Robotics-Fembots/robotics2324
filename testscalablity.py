# importing libraries
from PyQt5.QtWidgets import * #class that can display data, receive user input, etc.
from PyQt5 import QtCore, QtGui #imports two specfic libraries under pyqt5
from PyQt5.QtGui import * #base class for graphical user interfaces imports all modules under the ibrary
from PyQt5.QtCore import * #class allows for object communication 
import sys #imports library for different Python functions and variables
import time

class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# assigns title
		self.setWindowTitle("Widget GUI")

		# setting geometry
		self.setGeometry(400, 270, 1900, 900)
		self.setStyleSheet("background: #F1F6FD;")

		# calling method of all ui components made for the window
		self.UiComponents()

		# showing all the widgets
		self.show()
	def UiComponents(self):
		self.layout = QVBoxLayout()
		
		self.camera_label = QLabel("CAMERAS", self)
		self.camera_label.setGeometry(75, 375, 450, 120)
		self.camera_label.setStyleSheet("border: 4px solid white; border-radius: 10; background: #5D7090; color: #F1F6FD")
		self.camera_label.setFont(QFont('Time', 15))
		self.camera_label.setAlignment(Qt.AlignCenter)
		self.camera_label.move(1380, 90)
		
		
	    #front camera button and styling
		front_button = QPushButton("Front", self)
		front_button.setGeometry(125, 350, 400, 170)
		front_button.move (1400, 220)
		front_button.setStyleSheet("border-radius: 25; border: 3px solid midnightblue; color: midnightblue")
		front_button.setFont(QFont('Time', 11))
		
		self.layout.addWidget(self.camera_label)
		self.layout.addWidget(front_button)
		self.layout.addSpacing(9)
		

	    #pilot inversion camera button and styling
		#inverse_button = QPushButton("Inversion", self)
		#inverse_button.setGeometry(125, 350, 400, 170)
		##inverse_button.move (1400, 400)
		#inverse_button.setStyleSheet("border-radius: 25; border: 3px solid midnightblue; color: midnightblue")
		#inverse_button.setFont(QFont('Time', 11))
		
# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())