from PyQt5.QtWidgets import QApplication,QMenuBar,QMainWindow,QToolBar,QFontDialog,QColorDialog,QAction
import sys
from PyQt5 import QtCore,QtGui
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog,QPrintPreviewDialog

class mywindow(QMainWindow): #child class
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parent attribute
        self.title='PyQt5 MenuBar';
        self.top=100;
        self.left=100;
        self.width=700;
        self.height=300;
        self.initwindow(); #class method call
    def initwindow(self): #class method

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set window geometry

        self.createmenu(); #class method call

        self.show(); #show window

    def createmenu(self): #class method

        menubar=self.menuBar(); #create a menubar widget
        filemenu=menubar.addMenu('File'); #add file to menubar
        editmenu=menubar.addMenu('Edit'); #add Edit to menubar
        viewmenu=menubar.addMenu('View'); #add View to menubar
        helpmenu=menubar.addMenu('Help'); #add help to menubar

        openaction=QAction(QtGui.QIcon('open.png'), 'open', self); #create aan aCTION
        openaction.setShortcut('Ctrl+o'); #create action shortcut
        filemenu.addAction(openaction); #add action to filemenu

        saveaction=QAction(QtGui.QIcon('save-as.png'), 'save', self); #create aan aCTION
        saveaction.setShortcut('Ctrl+s'); #create action shortcut
        filemenu.addAction(saveaction); #add action to filemenu

        copyaction=QAction(QtGui.QIcon('copy.png'), 'copy', self); #create aan aCTION
        copyaction.setShortcut('Ctrl+c'); #create action shortcut
        filemenu.addAction(copyaction); #add action to filemenu

        quitaction=QAction(QtGui.QIcon('Quit.png'), 'quit', self); #create aan aCTION
        quitaction.setShortcut('Ctrl+e'); #create action shortcut
        quitaction.triggered.connect(self.exit); #connect a signal to a slot
        filemenu.addAction(quitaction); #add action to filemenu

    def exit(self): #class method
        self.close(); #close window


app=QApplication(sys.argv); #create a window app
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute window app