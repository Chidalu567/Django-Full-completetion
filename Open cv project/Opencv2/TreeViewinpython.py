from PyQt5.QtWidgets import QApplication,QFileSystemModel,QTreeView,QVBoxLayout,QWidget
from PyQt5.QtCore import QModelIndex
from PyQt5 import QtGui, QtCore
import sys

class TreeViewShow(QWidget): #child class name definition
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parent attributes

        self.setWindowTitle('TreeView'); #set window title
        self.setGeometry(QtCore.QRect(100, 100,500,600)); #set window geometry

        self.model=QFileSystemModel(); #create a filesystemmodel
        self.model.setRootPath(r"C:\Users\chidalu craving"); #set root path of model

        self.tree_view=QTreeView(); #create a treeview object
        self.tree_view.setModel(self.model); # set model of tree view
        self.tree_view.setRootIndex(self.model.index(r"C:\Users\chidalu craving")); #set root indexof trreeview
        self.tree_view.setColumnWidth(0,250); #set set column width of treeview.
        self.tree_view.setAlternatingRowColors(True); #set alternating row colours

        vbox=QVBoxLayout(self); #create a vertical layout
        vbox.addWidget(self.tree_view); #add widget to vertical layout

        self.setLayout(vbox); #set layout of windows to vertical layout

        self.setFocus(True); #set focus on window

        app.focusChanged.connect(self.blur); #connect a signal to a slot
        self.show(); #show window

    def blur(self): #class method definition
        self.setWindowOpacity(0.7); #set windowopacity

app=QApplication(sys.argv); #create an app
window=TreeViewShow(); #instance variable
sys.exit(app.exec()); #execute app
