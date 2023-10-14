import socket
import time
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class Window(QMainWindow):
    
    '''
    def __init__(self): #initialize the self (sle?) 
        super().__init__() #returns the parent object of the Example class

        self.initUI() #create the gui '''

    def initUI(self):
        super().__init__()
        self.setWindowTitle('GUI')
        self.setWindowIcon(QIcon('web.png'))
        self.setGeometry(200, 120, 2500, 1500) #(x-coor, y-coor, width, height)
        self.UiComponents()
        self.show()


        '''button styling
        btn = QPushButton('Button', self)
        btn.setToolTip('this is a <b><font color = pink>bye</font></b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.setStyleSheet("background-color: pink;"
                          "font color: white;")'''

    def UiComponents(self):
        
        #count variable
        '''self.start = 15
        self.time = self.start * 60
        self.countdownsec = True
        self.count = 0'''

        #start switch
        #self.start = False

        # creating label to show the seconds
        self.label = QLabel("15 : 00", self)
 
        # setting geometry of label
        self.label.setGeometry(100, 200, 200, 50)
 
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
 
        # creating pause button
        pause_button = QPushButton("Pause", self)
 
        # setting geometry to the button
        pause_button.setGeometry(125, 400, 150, 40)
 
        # creating reset  button
        reset_button = QPushButton("Reset", self)
 
        # setting geometry to the button
        reset_button.setGeometry(125, 450, 150, 40)
 
        # creating a timer object
        timer = QTimer(self)

        #timer.timeout.connect(self.updateTime)

        #timer.start(100)

    # method called by timer
    '''def updateTime(self):
        if self.start:
                # incrementing the counter
            self.minutes = self.time / 60
            self.seconds = self.time % 60

    
                # timer is completed
            if self.count == 0:
    
                # making flag false
                self.start = False

                    # getting text from count
        if self.start:
            text = str(self.minutes) + " : " + str(self.seconds)
 
            # showing text
            self.label.setText(text)

    def start_action(self):
            # making flag true
            self.start = True
    
            # count = 0
            if self.count == 0:
                self.start = False
    
    def pause_action(self):
    
        # making flag false
        self.start = False
    
    def reset_action(self):
    
        # making flag false
        self.start = False
    
        # setting count value to 0
        self.count = 0
'''

def main():

    app = QApplication(sys.argv)
    window = Window()
    window.initUI()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
