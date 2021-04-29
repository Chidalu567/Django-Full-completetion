from PyQt5.QtWidgets import QDialog,QApplication,QPushButton,QVBoxLayout,QProgressBar
from PyQt5 import QtGui,QtCore
from PyQt5.QtCore import QThread,pyqtSignal
import sys
import time

class thread(QThread): #thread class

    change_value=pyqtSignal(int); #listen to a signal and collect it value

    def run(self): #class method (it is an inheritance from class QThread)
        counter=0 #variable declaration
        while counter < 100:
            counter+=1 #increment counter
            time.sleep(0.3); #time to slep before next block of code is ran
            self.change_value.emit(counter); #emit counter to change_value



class mywindow(QDialog): #child class
    def __init__(self):#class constructor
        super().__init__(); #inheritance from parent attributes
        self.title='Progress bar';
        self.top=100;
        self.left=100;
        self.width=700;
        self.height=300;

        self.initwindow(); #class method call


    def initwindow(self): #class method

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set window geometry

        self.create_progressbar(); #class method call

        self.show(); #show window



    def create_progressbar(self): #class method

        vbox=QVBoxLayout(self); #create a vertical layout

        self.progressbar=QProgressBar(); #create a progress bar widget
        #self.progressbar.setValue(60)
        self.progressbar.setMaximum(100); #set maximum value to 100
        self.progressbar.setMinimum(0); #set minimum value to 0
        vbox.addWidget(self.progressbar); #add progress bar to verticcal layout

        self.button=QPushButton('Click to install',self); #createbutton widget
        self.button.setIcon(QtGui.QIcon('logo.png')); #set button icon
        self.button.clicked.connect(self.start_progressbar); #connect signal to slot
        vbox.addWidget(self.button); #add button to vertical layout


        self.setLayout(vbox); #set windows layout to vertical layout

    def start_progressbar(self): #class method
        self.thread=thread(); #instance variable
        self.thread.change_value.connect(self.set_progressbar); #connect a signal to a slot
        self.thread.start(); #start thread


    def set_progressbar(self,val): #class method
        self.progressbar.setValue(val); #set progressbar value


app=QApplication(sys.argv); #create an app
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute app