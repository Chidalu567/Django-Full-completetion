from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout
from PyQt5 import QtGui,QtCore
import sys

class MyWindow(QWidget): #child class name definition
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parent attributes

        self.setWindowTitle('Loading Window'); #set window title
        self.setGeometry(QtCore.QRect(100,100,500,500)); #set geometry of window

        self.label=QLabel('THIS IS THE MAIN WINDOW'); #create a label widget
        self.label.setAlignment(QtCore.Qt.AlignCenter); #set alignment of label

        vbox=QVBoxLayout(self); #create a vertical layout
        vbox.addWidget(self.label); #add widget to vertical layout

        self.setLayout(vbox); #set layout of window to vertical layout

        self.show(); #show window




class LoadingScreen(QWidget): #child class name
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parent attributes

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint|QtCore.Qt.CustomizeWindowHint); #set window flags
        self.resize(QtCore.QSize(200,200)); #resize window

        self.movie=QtGui.QMovie('35.gif'); #create a movie object
        self.label_for_movie=QLabel(); #crate a label widget
        self.label_for_movie.setMovie(self.movie); #set movie of label

        vbox=QVBoxLayout(self); #create  vertical layout
        vbox.addWidget(self.label_for_movie); #add widget to vertical layout


        self.startAnimation(); #class method call

        QtCore.QTimer.singleShot(3000,self.stopAnimation); #create a timer object

        self.setLayout(vbox); #set layout of window to vertical layout

        self.show(); #show window




    def startAnimation(self): #class method definition
        self.movie.start(); #start movie

    def stopAnimation(self): #class method definition
        self.movie.stop(); #stop movie
        self.close(); #close window
        window=MyWindow(); #instance variable


app=QApplication(sys.argv); #create an app
Loading=LoadingScreen(); #instance variable declaration
sys.exit(app.exec()); #execute app


