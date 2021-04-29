from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtGui,QtCore
import sys
from PyQt5.QtGui import QPainter,QPen,QBrush,QPolygon
from PyQt5.QtCore import QPoint

class mywindow(QMainWindow): #class method

    def __init__(self): #class constructor
        super().__init__(); #inheritance of parent attributes

        self.title='PyQt5 Context Menu';
        self.top=100;
        self.left=100;
        self.width=600;
        self.height=500;

        self.initwindow(); #class method call


    def initwindow(self): #class method

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set windows geometry


        self.show(); #show windows

    def paintEvent(self,event): #built-in class method
        painter=QtGui.QPainter(self); #create a painter object
        painter.setPen(QtGui.QPen(QtCore.Qt.black,5,QtCore.Qt.SolidLine)); #set pen of painter
        painter.setBrush(QtGui.QBrush(QtCore.Qt.green,QtCore.Qt.DiagCrossPattern)); #set brush of painter

        points=QtGui.QPolygon([
            QtCore.QPoint(100,100),
            QtCore.QPoint(200,50),
            QtCore.QPoint(20,20),
            QtCore.QPoint(200,100)
        ]); #create a polygon point

        painter.drawPolygon(points); #draw polygon




app=QApplication(sys.argv); #create application
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute application