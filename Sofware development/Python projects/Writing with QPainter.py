'''The mdi application is a multi document interface that opens a lot of windows on a mainwindow'''
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtGui,QtCore
import sys
from PyQt5.QtGui import QPainter,QTextDocument

class mywindow(QMainWindow): #child class

    count=0; #class variable
    def __init__(self): #class constructor
        super().__init__(); #inheritance of attributes from parent class

        self.title='MDI Application';
        self.top=100;
        self.left=100;
        self.width=400;
        self.height=200;

        self.initwindow(); #class method call

    def initwindow(self): #class method

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set window geometry


        self.show(); #show windows

    def paintEvent(self,event): #QPainter built-int method

        painter=QPainter(self); #create a painter
        painter.setPen(QtGui.QPen(QtCore.Qt.black,5,QtCore.Qt.SolidLine)); #set pen to painter
        rectangle=QtCore.QRectF(100,100,300,300); #rectangle object
        painter.drawRect(rectangle); #draw rectangle
        painter.drawText(rectangle,QtCore.Qt.AlignCenter,'Hello World'); #drawtext in a rectangle

        document=QTextDocument(self); #create a textdocument
        size_of_text=QtCore.QRectF(0,0,70,70); #position and size
        document.setTextWidth(size_of_text.width()); #set text width
        document.setHtml("<b>This is how to set html using QPainter class</b>"); #set the html command to document
        document.setHtml("<font size='3' color='red' float=right>Complete Writing</font>"); #sethtml
        document.drawContents(painter,size_of_text); #draw contents in the document



app=QApplication(sys.argv); #create window app
window=mywindow(); #class instance variable
sys.exit(app.exec()); #execute app