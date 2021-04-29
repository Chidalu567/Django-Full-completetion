from PyQt5.QtWidgets import QApplication,QPushButton,QDialog,QVBoxLayout,QLabel,QFileDialog
from PyQt5 import QtGui,QtCore
import sys
from PyQt5.QtGui import QPixmap

class mywindow(QDialog): #child class
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parents attributes

        self.title='Browsing Image';
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

        button=QPushButton('Browse Image',self); #create a button widget
        button.clicked.connect(self.browse_image); #connect a signal to a slot
        vbox.addWidget(button); #add widget to vertical layout

        self.label=QLabel(""); #create a label widget
        vbox.addWidget(self.label); #add widget to vertical layout

        self.setLayout(vbox); #set window layout to vertical layout

        self.show(); #show window

    def browse_image(self): #class method

        filename=QFileDialog.getOpenFileName(self,'Browse Image','c\\','Image Files(*.jpg *.png *.gif)'); #get open file name

        imagepath=filename[0]; #image path
        pixmap=QtGui.QPixmap(imagepath); #create a pixmap widget
        self.label.setPixmap(QtGui.QPixmap(pixmap)); #set pixmap to label
        self.resize(pixmap.width(),pixmap.height()); #resize image



app=QApplication(sys.argv); #create window app
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute app