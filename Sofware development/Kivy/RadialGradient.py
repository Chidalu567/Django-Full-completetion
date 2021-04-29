from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore,QtGui
import sys


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
    def paintEvent(self,e): #built_in function in QPainter class
        painter=QtGui.QPainter(self); #create a painter object
        painter.setPen(QtGui.QPen(QtCore.Qt.black,5,QtCore.Qt.SolidLine)); #set pen of painter

        radial=QtGui.QRadialGradient(QtCore.QPoint(100,100),100); #create a radial gradient
        radial.setColorAt(0.0,QtCore.Qt.white); #set color at 0.0 white
        radial.setColorAt(0.5,QtCore.Qt.green); #set color at 0.5 green
        radial.setColorAt(1.0,QtCore.Qt.black); #set color at 1.0 black

        painter.setBrush(QtGui.QBrush(radial)); #set brush of painter
        painter.drawRect(10,10,200,200); #draw rectangle





app=QApplication(sys.argv); #create application
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute application