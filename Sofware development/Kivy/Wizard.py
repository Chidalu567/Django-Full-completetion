from PyQt5.QtWidgets import QApplication,QPushButton,QWidget,QWizard,QVBoxLayout
from PyQt5 import QtGui,QtCore
import sys

class mywindow(QWidget): #child class
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parents attributes

        self.title='PyQt5 Wizard';
        self.top=100;
        self.left=100;
        self.width=700;
        self.height=300;

        self.initui(); #class method call

    def initui(self): #class method definition

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set window geometry

        vbox=QVBoxLayout(self); #create a vertical layout

        button=QPushButton('Launch',self); #create a button widget
        button.clicked.connect(self.on_clixked); #connect a signal to a slot
        vbox.addWidget(button); #add widget to vertical layout

        self.setLayout(vbox); #set window layout to vertical layout

        self.wizard=QWizard(); #create a wizard widget
        self.wizard.setWindowTitle('Launching....'); #set wizard window title
        self.wizard.setWindowIcon(QtGui.QIcon('logo.png')); #set wizard window icon


        self.show(); #show window

    def on_clixked(self): #class method
        self.wizard.open(); #open wizard widget whoen button is clicked

app=QApplication(sys.argv); #create window app
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute app