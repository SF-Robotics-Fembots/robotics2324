# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("Python ")

		# setting geometry
		self.setGeometry(100, 100, 800, 900)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for widgets
	def UiComponents(self):
		self.timerCount = 0
		self.running = True
		self.startTime = 0
		self.minutes = 15
		self.seconds = 0


		# creating label to show the seconds
		self.label = QLabel("TIMER: 15 : 00", self)

		# setting geometry of label
		self.label.setGeometry(100, 500, 500, 200)

		# setting border to the label
		self.label.setStyleSheet("border : 3px solid black")

		# setting font to the label
		self.label.setFont(QFont('Times', 15))

		# setting alignment to the label
		self.label.setAlignment(Qt.AlignCenter)

		# creating start button
		start_button = QPushButton("Start", self)

		# setting geometry to the button
		start_button.setGeometry(125, 350, 150, 40)

		# adding action to the button
		start_button.clicked.connect(self.start_action)

		# creating pause button
		pause_button = QPushButton("Pause", self)

		# setting geometry to the button
		pause_button.setGeometry(125, 400, 150, 40)

		# adding action to the button
		pause_button.clicked.connect(self.pause_action)

		# creating reset button
		reset_button = QPushButton("Reset", self)

		# setting geometry to the button
		reset_button.setGeometry(125, 450, 150, 40)

		# adding action to the button
		reset_button.clicked.connect(self.reset_action)

		# creating a timer object
		timer = QTimer(self)

		# adding action to timer
		timer.timeout.connect(self.update)

		# update the timer every tenth second
		timer.start(1000)

	def start_action(self):
		# making flag true
		if self.timerCount < 1:
			self.reset_action()
		if not self.running:
			self.update()
			self.running = True
			starttime = time.time()

	def pause_action(self):
		# making flag true
		if self.running:
			self.label(self.update)
			self.running = False
			#self.timerCount = 1

	def reset_action(self):
		# making flag true
		if self.running:
			self.running = False
        
		self.minutes = 15
		self.seconds = 0
		self.label.setText("TIMER: 15 : 00")

	def update(self):
		if self.seconds == 00:
			self.minutes -= 1
			self.seconds = 60
		if self.minutes == 00:
			self.reset_action()
		self.seconds -= 1

		self.minutes_string = f'{self.minutes}' if self.minutes > 9 else f'0{self.minutes}'
		self.seconds_string = f'{self.seconds}' if self.seconds > 9 else f'0{self.seconds}'
		self.label.setText("TIMER:" + self.minutes_string + " : " + self.seconds_string)

        

		

			
    

			



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
