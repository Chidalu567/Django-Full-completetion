from PyQt5.QtWidgets import QApplication,QLineEdit,QCompleter,QDialog,QVBoxLayout
from PyQt5 import QtGui,QtCore
import sys

class mywindow(QDialog): #child class
    def __init__(self): #class comstructor
        super().__init__(); #inheritance of parent attribute

        self.title='PyQt5 ComboBox';
        self.top=100;
        self.left=100;
        self.width=700;
        self.height=300;

        self.initwindow(); #class method call

    def initwindow(self): #class method

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set window geometry

        self.initui(); #class method call

        self.show(); #show windows

    def initui(self): #class method

        vbox=QVBoxLayout(); #create a vertical layout widget

        names=['Afghanistan','Pakistan','UAE','Australia','Japan','India','Indonesia','America','South-Korea','North-Korea','Nigeria','Portugal','Sudan','Uganda']; #python list definition
        self.completer=QCompleter(names); #create a completer widget and add list to it

        self.lineedit=QLineEdit(); #create lineedit widget
        self.lineedit.setCompleter(self.completer); #set completer to line edit

        vbox.addWidget(self.lineedit); #add widget to vertical layout
        self.setLayout(vbox); #set windows layout to vertical layout


app=QApplication(sys.argv); #create an app
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute window app