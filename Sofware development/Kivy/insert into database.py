from PyQt5.QtWidgets import QApplication,QDialog,QPushButton,QVBoxLayout,QMessageBox,QLabel,QLineEdit
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

        self.label1=QLabel('Name'); #create a label widget
        self.label1.setStyleSheet('color:red'); #set label stylesheet
        vbox.addWidget(self.label1);

        self.nameedit=QLineEdit(); #create a lineedit widget
        self.nameedit.setPlaceholderText('Enter UserName'); #set placeholdertext
        self.nameedit.setFont(QtGui.QFont('sans-serif',8)); #set font-family and size of text
        self.nameedit.setStyleSheet('background-color:yellow'); #set lineedit background color
        vbox.addWidget(self.nameedit); #add widget to vertical layout

        self.label2=QLabel('Email'); #create a label widget
        self.label2.setStyleSheet('color:red'); #set label stylesheet
        vbox.addWidget(self.label2); #add widget to vertical layout

        self.emailedit=QLineEdit(); #create a lineedit widget
        self.emailedit.setPlaceholderText('Enter Email'); #set placeholdertext
        self.emailedit.setFont(QtGui.QFont('sans-serif',8)); #set font-family and size of text
        self.emailedit.setStyleSheet('background-color:yellow'); #set line edit backgrund color
        vbox.addWidget(self.emailedit); #add widget to vertical layout

        self.button=QPushButton('Insert Data'); #create a button widget
        self.button.setStyleSheet('background-color:green'); #set button stylesheet
        self.button.setFont(QtGui.QFont('sans-serif',13)); #set font of button
        self.button.clicked.connect(self.insertdata); #connect a signal to a slot
        vbox.addWidget(self.button); #add widget to vertical layout

        self.setLayout(vbox); #set windows layout to vertical layout

        self.show(); #show windows

    def insertdata(self): #class method
        conn=mdb.connect(host='localhost',user='root',password='',database='pyqt5 database'); #create a connection object
        cur=conn.cursor(); #create a cursor object
        cur.execute("INSERT INTO data(UserName,Email) VALUES('%s','%s')"%(str(self.nameedit.text()),str(self.emailedit.text())));
        conn.commit(); #commit changes
        conn.close(); #close connections
        QMessageBox.about(self,'Connections','Inserted Successfully'); #create an about message box widget
        self.close(); #close window


app=QApplication(sys.argv); #create window app
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute app