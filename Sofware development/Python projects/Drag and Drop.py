from PyQt5.QtWidgets import QApplication,QWidget,QListWidget,QListWidgetItem,QHBoxLayout
from PyQt5 import QtGui,QtCore
import sys

class mywindow(QWidget): #child class
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parent attribute

        self.title='PyQt Drag and Drop';
        self.top=100;
        self.left=100
        self.width=600;
        self.height=300;

        self.initwindow(); #class method call

    def initwindow(self): #class method

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon("home.png")); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set window geometry

        self.drag_and_drop(); #class method call

        self.show(); #show windows

    def drag_and_drop(self): #class method

        self.hbox=QHBoxLayout(); #create a horizontal layout

        self.leftlist=QListWidget(); #create a list widget
        self.rightlist=QListWidget(); #create a list widget

        self.rightlist.setViewMode(QListWidget.IconMode); #set view mode of listwidget

        self.rightlist.setAcceptDrops(True); # set accept drops true
        self.rightlist.setDragEnabled(True); #set drag enabled
        self.leftlist.setAcceptDrops(True); #set accept drops true
        self.leftlist.setDragEnabled(True); #set drag enabled

        l1=QListWidgetItem(QtGui.QIcon("Quit.png"),'Quit'); # listwidgetitem
        l2=QListWidgetItem(QtGui.QIcon("save-as.png"),'Save-as'); #listwidgetitem
        l3=QListWidgetItem(QtGui.QIcon("print.png"),'Print'); #listwidgetitem
        l4=QListWidgetItem(QtGui.QIcon('About.png'),'About'); #listwidgetitem
        l5=QListWidgetItem(QtGui.QIcon('open.png'),'Open'); #list widget item
        l6=QListWidgetItem(QtGui.QIcon('copy.png'),'Copy'); #list widget item

        self.leftlist.insertItem(1,l1); #insertitem in list
        self.leftlist.insertItem(2,l2); #insertitem in list
        self.leftlist.insertItem(3,l3); #insertitem in list
        self.leftlist.insertItem(4,l4); #insertitem in list
        self.leftlist.insertItem(5,l5); #insertitem in list
        self.leftlist.insertItem(6,l6); #insertitem tolist


        QListWidgetItem(QtGui.QIcon('Choice.png'),'Choice',self.rightlist); #create a listitem in rightlist vertically
        QListWidgetItem(QtGui.QIcon('font.png'),'Font',self.rightlist); #create a listitem
        QListWidgetItem(QtGui.QIcon('color.png'),'Color',self.rightlist); #create a listitem
        QListWidgetItem(QtGui.QIcon('logo.png'),'Lenovo',self.rightlist); #create a list item

        self.hbox.addWidget(self.leftlist); #add widget to horizontal layout
        self.hbox.addWidget(self.rightlist); #add widget to horizontal layout

        self.setLayout(self.hbox); #set window layout to vertical layout



app=QApplication(sys.argv); #create an app
window=mywindow();#class instance variable
sys.exit(app.exec()); #execute app