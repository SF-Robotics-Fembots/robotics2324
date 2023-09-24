import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QIcon, QFont, QColor



class Example(QWidget):
    

    def __init__(self): #initialize the sle 
        super().__init__() #returns the parent object of the Example class

        self.initUI() #create the gui


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('this is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('this is a <b><font color = pink>bye</font></b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.setStyleSheet("background-color: pink;"
                          "font color: white;")

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
