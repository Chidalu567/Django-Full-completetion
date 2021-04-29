'''The mdi application is a multi document interface that opens a lot of windows on a mainwindow'''
from PyQt5.QtWidgets import QApplication,QMainWindow,QMdiArea,QMdiSubWindow,QTextEdit,QMenuBar,QAction
from PyQt5 import QtGui,QtCore
import sys

class mywindow(QMainWindow): #child class

    count=0; #class variable
    def __init__(self): #class constructor
        super().__init__(); #inheritance of attributes from parent class

        self.title='MDI Application';
        self.top=100;
        self.left=100;
        self.width=700;
        self.height=300;

        self.initwindow(); #class method call

    def initwindow(self): #class method

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set window geometry

        self.bar=self.menuBar(); #create a menubar widget
        file=self.bar.addMenu('file'); #add menu to menubar

        newAction=QAction(QtGui.QIcon('home.png'),'New',self); #create an action
        cascadeAction=QAction('Cascade',self); #create an action
        TiledAction=QAction('Tile',self); #create an action
        file.addAction(newAction); #add action to menubar
        file.addAction(cascadeAction); #add action to menubar
        file.addAction(TiledAction); #add action to menubar
        file.triggered.connect(self.WindowTrig); #connect a signal to a slot

        self.mdi=QMdiArea(); #create an multi document interface area
        self.setCentralWidget(self.mdi); #set central widget of window to mdi

        self.show(); #show windows


    def WindowTrig(self,p): #class method
        '''We create and handle actions here'''
        if p.text()=='New':
            mywindow.count=mywindow.count+1; #incrementing the class variable
            sub=QMdiSubWindow(); #create an Mdi Sub Window
            textedit=QTextEdit(self); #create a text edit widget
            sub.setWidget(textedit); #set widget to Sub
            sub.setWindowTitle('Sub Window '+str(mywindow.count)); #set window title
            self.mdi.addSubWindow(sub); #add subwindow to mdi

            sub.show(); #show sub window

        if p.text()=='Cascade':
            self.mdi.cascadeSubWindows(); #cascade sub windows

        if p.text()=='Tile':
            self.mdi.tileSubWindows(); #tilesub windows

app=QApplication(sys.argv); #create window app
window=mywindow(); #class instance variable
sys.exit(app.exec()); #execute app