from PyQt5.QtWidgets import QApplication,QWidget,QSystemTrayIcon,QMenu,QAction
from PyQt5 import QtCore,QtGui
import sys

class TrayIcon(QWidget): #child class name
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parent attributes

        self.tray=QSystemTrayIcon(QtGui.QIcon('chidalu.jpg')); #create a systemtrayicon
        self.tray.setToolTip('Click Me'); #set tooltip of trayicon
        self.tray.show(); #show trayicon

        menu=QMenu(self); #create a menu object

        exitAction=QAction('Exit'); #create an exit action
        exitAction.triggered.connect(app.quit); #connect a signal to a slot
        menu.addAction(exitAction); #add action to menu

        self.tray.setContextMenu(menu); #set context menu of trayicon

app=QApplication(sys.argv); #create an app
window=TrayIcon(); #Instance variable
sys.exit(app.exec()); #execute app
