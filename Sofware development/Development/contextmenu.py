from PyQt5.QtWidgets import QApplication,QMainWindow,QMenu
from PyQt5 import QtCore,QtGui
import sys

class mywindow(QMainWindow): #class method

    def __init__(self): #class constructor
        super().__init__(); #inheritance of parent attributes

        self.title='PyQt5 Context Menu';
        self.top=100;
        self.left=100;
        self.width=700;
        self.height=300;

        self.initwindow(); #class method call


    def initwindow(self): #class method

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set windows geometry


        self.show(); #show windows


    def contextMenuEvent(self,event): #PyQt5 built-in method
        contextmenu=QMenu(self); #create a menu widget

        newAction=contextmenu.addAction('New'); #add action to contextmenu
        openAction=contextmenu.addAction('Open'); #add action to context menu
        quitAction=contextmenu.addAction('Quit'); #add action to context menu

        action=contextmenu.exec_(self.mapToGlobal(event.pos())); #maptoglobal event position when clicked

        if action==quitAction:
            self.close(); #close window


app=QApplication(sys.argv); #create application
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute application