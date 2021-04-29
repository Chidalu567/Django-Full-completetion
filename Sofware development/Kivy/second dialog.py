from PyQt5.QtWidgets import QApplication,QDialog,QPushButton,QMainWindow,QVBoxLayout
from PyQt5 import QtCore,QtGui
import sys

class mywindow(QDialog): # child class
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parent attribute

        self.title='PyQt5 second';
        self.top=100;
        self.left=100;
        self.width=700;
        self.height=300;

        self.initwindow(); #class method call

    def initwindow(self): #class method

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set geometry of window

        vbox=QVBoxLayout(self); #create a vertical layout

        self.btn=QPushButton('Open Second Dialog'); #create a button widget
        self.btn.setFont(QtGui.QFont('sans-serif',13)); #set font-family and size of button
        self.btn.clicked.connect(self.seconddialog); #connect a signal to a slot

        vbox.addWidget(self.btn); #add widget to vertical layout

        self.setLayout(vbox); #set window layout to vertical layout

        self.show(); #show windows

    def seconddialog(self): #class method
        mydialog=QDialog(self); #create a dialog widget
        mydialog.setModal(True); #set modal true
        mydialog.exec(); #execute the dialog

app=QApplication(sys.argv); #create window app
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute window app