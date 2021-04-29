from PyQt5.QtWidgets import QApplication,QDialog,QCalendarWidget,QLabel,QVBoxLayout
from  PyQt5 import QtGui,QtCore
import sys

class mywindow(QDialog): #child class
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parent attributes

        self.title='PyQt5 Calendar';
        self.top=100;
        self.left=100;
        self.width=700;
        self.height=300;

        self.initwindow(); #class method call


    def initwindow(self): #class method

        self.setWindowTitle(self.title);#set window title
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set window geometry

        self.calendar(); #class method call

        self.show(); #show windows


    def calendar(self): #class method

        vbox=QVBoxLayout(self); #create a vertical layout


        self.calendar=QCalendarWidget(); #create a calendar widget
        self.calendar.setGridVisible(True); #set calendar grid visible
        self.calendar.selectionChanged.connect(self.onselectionchanged); #connect a signal to a slot
        vbox.addWidget(self.calendar); #add widget to vertical layout

        self.label=QLabel(); #create a label widget
        self.label.setFont(QtGui.QFont('sans-serif',14)); #set font of label
        vbox.addWidget(self.label); #add widget to vertical layout

        self.setLayout(vbox); #set windowlayout to vertical layout


    def onselectionchanged(self): #class method

        calval=self.calendar.selectedDate(); #selected date value
        self.label.setText(str(calval));#set label text

app=QApplication(sys.argv); #create an app
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute window app