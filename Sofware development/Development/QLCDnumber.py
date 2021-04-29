from PyQt5.QtWidgets import QApplication,QLCDNumber,QWidget,QPushButton,QVBoxLayout
from PyQt5 import QtGui,QtCore
import sys
from random import randint

class mywindow(QWidget):# child class
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parent attributes

        self.top=100;
        self.title='LCD number';
        self.left=100;
        self.width=700;
        self.height=300;

        self.initwindow(); #class method call

    def initwindow(self): #class method

        self.setWindowTitle(self.title); #set windowtitle
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set window geometry

        self.lcd(); #class method call

        self.show(); #show windows

    def lcd(self): #class method definition

        vbox=QVBoxLayout(self); #create a vertical layout


        self.lcd=QLCDNumber(); #create an lcd widget
        self.lcd.setStyleSheet('background-color:yellow'); #set lcdstylesheet
        vbox.addWidget(self.lcd); #add widget to vertical layout


        self.button=QPushButton('Generate Random Numbers'); #create a button widget
        self.button.setFont(QtGui.QFont('sans-serif')); #set button font
        self.button.setStyleSheet('background-color:red'); #set button stylesheet
        self.button.clicked.connect(self.generate); #connect a signal to a slot
        vbox.addWidget(self.button); #add widget to vertical layout

        self.setLayout(vbox); #set windows layout to vertical layout

    def generate(self): #class method
       number=randint(1,500); #generate random integer from 1-500
       self.lcd.display(number); #display number in lcd


app=QApplication(sys.argv); #create an app
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute window app