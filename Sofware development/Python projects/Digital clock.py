from PyQt5.QtWidgets import QApplication,QLabel,QVBoxLayout,QWidget
from PyQt5 import QtGui,QtCore
import sys

class Digitalclock(QWidget): #child class name
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parent attributes

        self.title='Digital Clock';
        self.top=100;
        self.left=100;
        self.width=600;
        self.height=700;
        self.initui(); #class method call

    def initui(self): #class method definition

        self.setWindowTitle(self.title); #set window title
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set geometry of windows

        vbox=QVBoxLayout(self); #create a vertical layout

        self.label=QLabel(); #create a label widget

        vbox.addWidget(self.label); #add widget to vertical layout

        self.setLayout(vbox); #set layout of window to vertical layout

        Timer=QtCore.QTimer(self); #create a timer object
        Timer.timeout.connect(self.displaytext); #connect a signal to a slot
        Timer.start(1000); #start timer

    def displaytext(self): #class method definiton
        time=QtCore.QTime.currentTime(); #current time on system
        self.label.setText(time.toString("hh:mm:ss")); #set text of label

app=QApplication(sys.argv); #create an app
clock=Digitalclock(); #create an instance variable
sys.exit(app.exec()); #execute app
