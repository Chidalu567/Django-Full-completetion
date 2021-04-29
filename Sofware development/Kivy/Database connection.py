from PyQt5.QtWidgets import QApplication,QDialog,QPushButton,QVBoxLayout,QMessageBox
from PyQt5 import QtGui,QtCore
import sys
import pymysql as mdb

class mywindow(QDialog): #child class
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parent attributes

        self.title='PyQt5 DataBase';
        self.top=100;
        self.left=100;
        self.width=700;
        self.height=300;

        self.initwindow(); #class method call

    def initwindow(self): #class method

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set window geometry

        vbox=QVBoxLayout(self); #create a vertical layout

        self.button=QPushButton('Connect To DataBase'); #create a button widget
        self.button.clicked.connect(self.dbconnect); #connect a signal to a slot
        vbox.addWidget(self.button); #add widget to vertical layout

        self.setLayout(vbox); #set windows layout to vertical layout

        self.show(); #show windows

    def dbconnect(self): #class method

        try:
            db=mdb.connect(host='localhost',user='root',password='',database='pyqt5 database'); #connect to a database
            QMessageBox.about(self,'Connections','Connected to DataBase Successfully'); #create a messagebox widget

        except mdb.Error as e:
            QMessageBox.about(self,'Connections','Falied to Connect to DataBase'); #messagebox widget
            sys.exit(1); #exit system


app=QApplication(sys.argv); #create window app
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute app