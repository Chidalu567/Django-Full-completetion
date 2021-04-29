from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QFrame
from PyQt5 import QtGui,QtCore
import sys
from PyQt5.QtCore import QPropertyAnimation

class window(QMainWindow): #child class
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parent attributes

        self.title='PyQt5 Graphic(View and Scene)';
        self.top=100;
        self.left=100;
        self.width=700;
        self.height=300;

        self.initwindow(); #class method call

    def initwindow(self): #class method

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set window geometry

        self.button=QPushButton('Start Animation',self); #create a button widget
        self.button.clicked.connect(self.doAnimation); #connect a signal to a slot
        self.button.move(50,50); #manual positioning

        self.frame=QFrame(self); #create a frame widget
        self.frame.setFrameStyle(QFrame.StyledPanel|QFrame.Panel); #setFrameStyle
        self.frame.setGeometry(QtCore.QRect(150,300,100,100)); #setgeometry of frame

        self.show(); #show windows

    def doAnimation(self): #class method definition
        self.anim=QPropertyAnimation(self.frame,b'geometry'); #set property animation to frame
        self.anim.setDuration(10000); #set duration of animation
        self.anim.setStartValue(QtCore.QRect(150,150,400,400)); #set start value of animation
        self.anim.setEndValue(QtCore.QRect(500,500,700,700)); #se end value of animation
        self.anim.start(); #start animation


app=QApplication(sys.argv); #create window app
window=window(); #class instance variable
sys.exit(app.exec()); #execute app
