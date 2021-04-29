from __future__ import division
from PyQt5.QtWidgets import QApplication,QDialog,QTextBrowser,QLineEdit,QVBoxLayout
from PyQt5 import QtCore,QtGui
import sys
from math import*


class mywindow(QDialog): #child class
    def __init__(self): #child constructpr
        super().__init__(); #inheritance from parent attributes

        self.setWindowTitle('TextBrowser'); #set window title
        self.setWindowIcon(QtGui.QIcon("home.png")); #set window icon
        self.setGeometry(QtCore.QRect(100,100,700,300)); #set window geometry
        self.initui(); #class method call

    def initui(self): #class method definition

        vbox=QVBoxLayout(self); #create a vertical layout

        self.browser=QTextBrowser(); #create a textbrowser widget
        self.lineedit=QLineEdit(); #create a line edit widget
        self.lineedit.returnPressed.connect(self.show_in_text_browser); #connect a signal to a slot

        vbox.addWidget(self.browser); #add widget to vertical layout
        vbox.addWidget(self.lineedit); #add widget to vertical layout
        self.show(); #show window

    def show_in_text_browser(self): #class method definition\
        try:
            text=self.lineedit.text(); #get text in line edit
            #the eval turns the string to unicode,therefore we can operate on a given string
            self.browser.append("<b>%s</b> = <i>%i</i>"%(text,eval(text))); #append value to textbrowser
        except:
            self.browser.append("<font color='red'><b>%s</b> is invalid</font>"%(text)); #append value ot string


app=QApplication(sys.argv); #create an application
window=mywindow();#instance variable
sys.exit(app.exec()); #execute app