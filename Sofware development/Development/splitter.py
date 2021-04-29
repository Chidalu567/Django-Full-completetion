from PyQt5.QtWidgets import QApplication,QWidget,QSplitter,QVBoxLayout,QLineEdit,QFrame
from PyQt5 import QtCore,QtGui
import sys

class mywindow(QWidget): #child class
    def __init__(self): #class constructor
        super().__init__(); #class inheritance

        self.title='QSplitter';
        self.top=100;
        self.left=200;
        self.width=700;
        self.height=300;

        self.initwindow(); #class method call

    def initwindow(self): #class method

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set windows geometry

        self.splitter(); #class method call

        self.show(); #show windows


    def splitter(self): #class method

        vbox=QVBoxLayout(self); #create a vertival layout

        frameleft=QFrame(self); #create a frame object
        frameleft.setFrameShape(QFrame.StyledPanel); #set frame shape

        self.lineedit=QLineEdit(); #create a lineedit widget

        splitter1=QSplitter(QtCore.Qt.Horizontal); #horizontal splitter
        splitter1.addWidget(frameleft); #add widget to horizontal splitter
        splitter1.addWidget(self.lineedit); #add widget to horizontal splitter

        framebottom=QFrame(); #create a frame widget
        framebottom.setFrameShape(QFrame.StyledPanel); #set frameshape

        splitter2=QSplitter(QtCore.Qt.Vertical); #create a vertical splitter
        splitter2.addWidget(splitter1); #add widget to splitter
        splitter2.addWidget(framebottom);#add widget to splitter

        vbox.addWidget(splitter2); #add splitter2 to vertical layout

        self.setLayout(vbox); #set windows layout to vertical layout


app=QApplication(sys.argv); #create windows app
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute the app