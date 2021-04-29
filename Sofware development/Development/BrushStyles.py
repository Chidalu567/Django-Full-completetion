from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtGui,QtCore
import sys

class mywindow(QMainWindow): #class method definition
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parent attribute

        self.title='PyQt5 Brush Styles';
        self.top=100
        self.left=100
        self.width=900
        self.height=900;

        self.initwindow(); #class method call

    def initwindow(self): #class method definition

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set window geometry

        self.show(); #show window

    def paintEvent(self,event): #QPainter built-in function
        painter=QtGui.QPainter(self); #create a painter
        painter.setPen(QtGui.QPen(QtCore.Qt.black,5,QtCore.Qt.SolidLine)); #set pen for painter
        painter.setBrush(QtGui.QBrush(QtCore.Qt.red,QtCore.Qt.DiagCrossPattern)); #set brush to painter
        painter.drawRect(100,100,100,100); #draw rectangle

        painter=QtGui.QPainter(self); #create a painter
        painter.setPen(QtGui.QPen(QtCore.Qt.black,5,QtCore.Qt.SolidLine)); #set pen for painter
        painter.setBrush(QtGui.QBrush(QtCore.Qt.red,QtCore.Qt.VerPattern)); #set brush to painter
        painter.drawRect(400,100,100,100); #draw rectangle

        painter=QtGui.QPainter(self); #create a painter
        painter.setPen(QtGui.QPen(QtCore.Qt.black,5,QtCore.Qt.SolidLine)); #set pen for painter
        painter.setBrush(QtGui.QBrush(QtCore.Qt.red,QtCore.Qt.BDiagPattern)); #set brush to painter
        painter.drawRect(100,300,100,100); #draw rectangle

        painter=QtGui.QPainter(self); #create a painter
        painter.setPen(QtGui.QPen(QtCore.Qt.black,5,QtCore.Qt.SolidLine)); #set pen for painter
        painter.setBrush(QtGui.QBrush(QtCore.Qt.red,QtCore.Qt.HorPattern)); #set brush to painter
        painter.drawRect(400,300,100,100); #draw rectangle

        painter=QtGui.QPainter(self); #create a painter
        painter.setPen(QtGui.QPen(QtCore.Qt.black,5,QtCore.Qt.SolidLine)); #set pen for painter
        painter.setBrush(QtGui.QBrush(QtCore.Qt.red,QtCore.Qt.Dense1Pattern)); #set brush to painter
        painter.drawRect(100,600,100,100); #draw rectangle

        painter=QtGui.QPainter(self); #create a painter
        painter.setPen(QtGui.QPen(QtCore.Qt.black,5,QtCore.Qt.SolidLine)); #set pen for painter
        painter.setBrush(QtGui.QBrush(QtCore.Qt.red,QtCore.Qt.Dense3Pattern)); #set brush to painter
        painter.drawRect(400,600,100,100); #draw rectangle


app=QApplication(sys.argv); #create windowapp
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute app