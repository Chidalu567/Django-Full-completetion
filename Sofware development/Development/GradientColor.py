from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore,QtGui
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QLinearGradient

class mywindow(QMainWindow): #class method

    def __init__(self): #class constructor
        super().__init__(); #inheritance of parent attributes

        self.title='PyQt5 Rectangle';
        self.top=100;
        self.left=100;
        self.width=400;
        self.height=300;

        self.initwindow(); #class method call


    def initwindow(self): #class method

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set windows geometry


        self.show(); #show windows
    def paintEvent(self,e): #built_in function in QPainter class
        painter=QtGui.QPainter(self); #create a painter object
        painter.setPen(QtGui.QPen(Qt.black,5,Qt.SolidLine)); #set pen of painter

        grad1=QLinearGradient(20,100,100,15); #create a gradient widget
        grad1.setColorAt(0.0,QtCore.Qt.darkGray); #set color at o.o to be darkgray
        grad1.setColorAt(0.5,Qt.yellow); #set color at 0.5 to be yellow
        grad1.setColorAt(1.0,Qt.blue); #set color at 1.0 to be blue

        painter.setBrush(QtGui.QBrush(grad1)); #set brush for painter
        painter.drawRect(10,10,200,200); #draw rectangle



app=QApplication(sys.argv); #create application
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute application