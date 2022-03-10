import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

import time

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("PyQt Line Edit example (textfield)") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Counter:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(130, 32)
        self.nameLabel.move(20, 20)

        self.pybuttonStart = QPushButton('Start', self)
        self.pybuttonStart.clicked.connect(self.startMethod)
        self.pybuttonStart.resize(50,32)
        self.pybuttonStart.move(80, 60)        


        self.pybuttonStop = QPushButton('Stop', self)
        self.pybuttonStop.clicked.connect(self.stopMethod)
        self.pybuttonStop.resize(50,32)
        self.pybuttonStop.move(160, 60) 

        self.counter=0
        
    def loop(self):
        while self.okToLoop:
            self.line.setText(f"{self.counter}")
            time.sleep(1)
            self.counter += 1
            
    def startMethod(self):
        self.okToLoop=True
        self.loop()
            
    def stopMethod(self):
        self.okToLoop=False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )