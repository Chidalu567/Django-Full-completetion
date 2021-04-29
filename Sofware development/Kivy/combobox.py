from PyQt5.QtWidgets import QApplication,QLabel,QComboBox,QDialog,QVBoxLayout
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

        self.label=QLabel(); #create   label widget
        self.label.setFont(QtGui.QFont('sans-serif',13)); #set font-family and size of label

        self.combo=QComboBox(); #create a combobox widget
        self.combo.addItem('Python'); #add item to combobox
        self.combo.addItem('C++'); #add item to combobox
        self.combo.addItem('C#');#add item to combobox
        self.combo.addItem('Java'); #add item to combobox
        self.combo.addItem('Javascript'); #add Item to combobox
        self.combo.currentTextChanged.connect(self.comboboxchoice); #connect a signal to a slot

        vbox.addWidget(self.combo); #add widget to vertical layout
        vbox.addWidget(self.label); #add label to vertical layout

        self.setLayout(vbox); #set layout of windows to vertical layout

    def comboboxchoice(self): #class method
        choice=self.combo.currentText(); #current text in combo box
        self.label.setText('You Have Selected: '+str(choice)); #set label text


app=QApplication(sys.argv); #create an app
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute window app