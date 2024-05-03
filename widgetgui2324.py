# importing libraries
from PyQt5.QtWidgets import * #class that can display data, receive user input, etc.
from PyQt5 import QtCore, QtGui #imports two specfic libraries under pyqt5
from PyQt5.QtGui import * #base class for graphical user interfaces imports all modules under the ibrary
from PyQt5.QtCore import * #class allows for object communication 
import sys #imports library for different Python functions and variables
import time


'''
screenshot for photogrammetry
show when in pilot inversion
show thruster values
show temperature sensor values(not working yet)
'''

#creates main GUI window
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

	# method for widgets
	def UiComponents(self):
		
        #camera label and styling
		self.camera_label = QLabel("CAMERAS", self)
		self.camera_label.setGeometry(75, 375, 450, 120)
		self.camera_label.setStyleSheet("border: 4px solid white; border-radius: 10; background: #5D7090; color: #F1F6FD")
		self.camera_label.setFont(QFont('Time', 15))
		self.camera_label.setAlignment(Qt.AlignCenter)
		self.camera_label.move(1380, 90)
		
	    #pilot inversion camera button and styling

		self.humidity_sensor = QLabel("Inversion Status: ", self)
		self.humidity_sensor.setGeometry(120, 350, 400, 200)
		self.humidity_sensor.move(1400, 220)
		self.humidity_sensor.setAlignment(Qt.AlignLeft)
		self.humidity_sensor.setStyleSheet("border-radius : 10; border: 3px solid midnightblue; color: midnightblue; padding: 15px")
		
		self.thruster_values = QLabel("Thruster Values: ", self)
		self.thruster_values.setGeometry(120, 350, 335, 400)
		self.thruster_values.move(630, 380)
		self.thruster_values.setAlignment(Qt.AlignLeft)
		self.thruster_values.setStyleSheet("border-radius : 15; border: 3px solid midnightblue; color: midnightblue; padding: 15px")

        #humidity sensor and styling
		self.temp_sensor = QLabel("Temperature Sensor Values: ", self)
		self.temp_sensor.setGeometry(120, 350, 335, 400)
		self.temp_sensor.move(970, 380)
		self.temp_sensor.setAlignment(Qt.AlignLeft)
		self.temp_sensor.setStyleSheet("border-radius : 10; border: 3px solid midnightblue; color: midnightblue; padding: 15px")

        #depth sensor and styling
		'''self.depth_sensor = QLabel("Depth Sensor: ", self)
		self.depth_sensor.setGeometry(120, 350, 335, 200)
		self.depth_sensor.move(630, 600)
		self.depth_sensor.setAlignment(Qt.AlignLeft)
		self.depth_sensor.setStyleSheet("border-radius : 10; border: 3px solid midnightblue; color: midnightblue; padding: 15px")'''
		
		
        #notepad label styling
		self.notepad_label = QLabel("NOTEPAD", self)
		self.notepad_label.setGeometry(75, 375, 450, 120)
		self.notepad_label.setStyleSheet("border: 4px solid white; border-radius: 10; background: #5D7090; color: #F1F6FD")
		self.notepad_label.setFont(QFont('Time', 15))
		self.notepad_label.setAlignment(Qt.AlignCenter)
		self.notepad_label.move(100, 90)
		
        #creates notepad to write on and styles it
		self.notepad = QTextEdit(self)
		self.notepad.resize(450, 600)
		self.notepad.setStyleSheet("border: 3px solid midnightblue; color: midnightblue")
		self.notepad.setFont(QFont('Time', 8))
		self.notepad.setAlignment(Qt.AlignLeft)
		self.notepad.move(100, 230)
		
		self.timerCount = 0
		#flag to check when timer is running or not
		self.running = False
		#set minutes counter to 15
		self.minutes = 15
		#set seconds to 0
		self.seconds = 0


		# creating label to show the seconds
		self.label = QLabel("TIMER: 15 : 00", self)

		# setting geometry of label
		self.label.setGeometry(100, 500, 670, 180)

		# setting border to the label
		self.label.setStyleSheet("border: 4px solid midnightblue; color: midnightblue;")

		# setting font to the label
		self.label.setFont(QFont('Times', 18))

		# setting alignment to the label
		self.label.setAlignment(Qt.AlignCenter)
		
        #moves labele to correct position
		self.label.move(630, 60)
		
		# creating start button
		start_button = QPushButton("START", self)

		#sets styling to the button
		start_button.setGeometry(125, 350, 215, 75)
		start_button.move(1088, 260)
		start_button.setStyleSheet("border-radius :25; border: 3px solid midnightblue; color: midnightblue")

		# adding action to the button by running the start_action function
		start_button.clicked.connect(self.start_action)

		# creating pause button
		pause_button = QPushButton("PAUSE", self)

		# setting style to the button 
		pause_button.setGeometry(125, 350, 215, 75)
		pause_button.move(858, 260)
		pause_button.setStyleSheet("border-radius :25; border: 3px solid midnightblue; color: midnightblue")

		# adding action to the button by running the pause_action function
		pause_button.clicked.connect(self.pause_action)

		# creating reset button
		reset_button = QPushButton("RESET", self)

		# setting style to the button
		reset_button.setGeometry(125, 350, 215, 75)
		reset_button.move(628, 260)
		reset_button.setStyleSheet("border-radius :25; border: 3px solid midnightblue; color: midnightblue")

		# adding action to the button by running the reset_action function
		reset_button.clicked.connect(self.reset_action)

		# creating a timer object
		timer = QTimer(self)

		# adding action to timer by running update function
		timer.timeout.connect(self.update)

		# updates the timer every tenth second
		timer.start(1000)
		
    #defines function to start timer
	def start_action(self):
		# making flag true
		if self.timerCount < 1:
			self.reset_action()
		if not self.running:
			self.update()
			self.running = True

    #defines function to pause timer
	def pause_action(self):
		# making flag true
		if self.running:
			self.running = False
			self.update()
			self.timerCount = 1

    #defines function to reset timer
	def reset_action(self):
		# making flag true
		if self.running:
			self.running = False
        
        #resets minutes and seconds to what it was in the start
		self.minutes = 15
		self.seconds = 0
		self.label.setText("TIMER: 15 : 00")

    #defines update function which runs the timer 
	def update(self):
		if self.running: 
			#once a minute has gone by then decrease a minute
			if self.seconds == 00:
				self.minutes -= 1
				self.seconds = 60
			#once all minutes are done, then reset the timer back to 15 minutes
			if self.minutes == 00:
				self.reset_action()
			self.seconds -= 1
			
            #formats time to include leading zeros
			self.minutes_string = f'{self.minutes}' if self.minutes > 9 else f'0{self.minutes}'
			self.seconds_string = f'{self.seconds}' if self.seconds > 9 else f'0{self.seconds}'
			
            #displays the minutes and seconds onto the window
			self.label.setText("TIMER: " + self.minutes_string + " : " + self.seconds_string)

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())