from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import QtCore,QtGui
import sys

class BallBounce(QWidget): #child class name
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parent attributes

        self.title='Ball Bouncing';


        self.resize(1000,800); #resize window

        self.initUI(); #class method call

    def initUI(self): #class method definition

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('chidalu.jpg')); #set window icon

        self.color=QtGui.QColor(QtCore.Qt.red); #create a color object

        self.circle=QtCore.QRect(0,0,50,50); #create a rect
        self.circle.moveCenter(QtCore.QPoint(self.width()/2,self.circle.height()/2)); #move rect center

        self.step=QtCore.QPoint(5,0); #step
        self.x_direction=1;

        self.timer=QtCore.QTimer(self,interval=12); #create a timer object
        self.timer.timeout.connect(self.update_value); #connect a signal to a slot
        self.timer.start(); #start timer



    def paintEvent(self,event): #built-in class method
        painter=QtGui.QPainter(self); #create a painter object
        painter.setPen(QtGui.QPen(QtCore.Qt.black)); #set pen of painter
        painter.setBrush(QtGui.QBrush(self.color)); #set brush of painter
        painter.drawEllipse(self.circle); #draw ellipse

    def update_value(self): #class method definition
    '''When the rught of cicle is greater than 400 and x is i take it backwoards (by setting x to -1)
    When 0 is greaterthan the left and direction if backwards take it forwards(by setting x +1)'''
        if self.circle.right()> 400 and self.x_direction==1:
            self.x_direction=-1;
        elif self.circle.left()<0 and self.x_direction==-1:
            self.x_direction=1;
        self.circle.translate(self.step*self.x_direction); #translate the cicle
        self.update();#update the value


app=QApplication(sys.argv); #create an app
window=BallBounce();#instance variable
window.show()
sys.exit(app.exec()); #execute app


