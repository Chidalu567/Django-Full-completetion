from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore,QtGui
import sys
from PyQt5.QtCore import Qt

class mywindow(QMainWindow): #class method

    def __init__(self): #class constructor
        super().__init__(); #inheritance of parent attributes

        self.title='PyQt5 Rectangle';
        self.top=100;
        self.left=100;
        self.width=700;
        self.height=300;

        self.initwindow(); #class method call


    def initwindow(self): #class method

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set windows geometry


        self.show(); #show windows

    def paintEvent(self,event): #QPainter built-in function
        painter=QtGui.QPainter(self); #create a painter
        painter.setPen(QtGui.QPen(Qt.black,5,Qt.SolidLine)); #set pen for painter
        painter.setBrush(QtGui.QBrush(Qt.green,Qt.DiagCrossPattern)); #set brush for painter
        painter.drawEllipse(100,100,400,200); #draw ellipse


app=QApplication(sys.argv); #create application
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute application