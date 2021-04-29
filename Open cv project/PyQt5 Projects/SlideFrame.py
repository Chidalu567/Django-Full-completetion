from PyQt5.QtWidgets import QFrame,QPushButton,QApplication,QVBoxLayout,QWidget,QGroupBox,QHBoxLayout
from PyQt5 import QtGui,QtCore
import sys

class MainWindow(QWidget): #child class name
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parent attributes

        self.title='Window Slide';
        self.top=100;
        self.left=100;
        self.width=1000;
        self.height=700;

        self.initUI(); #class  method call

    def initUI(self): #class method definition

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('android.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set geometry of window

        self.button=QPushButton(); #create a button widget
        self.button.setIcon(QtGui.QIcon('bars.svg')); #set icon of button widget
        self.button.setMinimumWidth(70); #set minimum width of button
        self.button.setMaximumWidth(70); #set maximum wudth of button widget
        self.button.setFixedHeight(50); #set fixed height of button widget
        self.button.setIconSize(QtCore.QSize(20,20)); #set icon size
        self.button.setStyleSheet("QPushButton"
                                    "{"
                                    "background-color:Turquoise;"
                                    "border:2px solid transparent;"
                                    "}"
                                    "QPushButton:active"
                                    "{"
                                    "background-color:rgb(0,92,157);"
                                    "border-right:4px solid black;"
                                    "}"
                                    "QPushButton:hover"
                                    "{"
                                    "border-bottom:2px solid black;"
                                    "border-right:2px solid transparent;"
                                    "}"); #set stylesheet of button
        self.button.move(60,30); #button move
        self.button.clicked.connect(self.slide_frame); #connect a signal to a slot

        self.frame=QFrame(); #create a frame widget
        self.frame.setFrameShape(QFrame.StyledPanel); #set frame shape
        self.frame.setMinimumWidth(70); #set minimum width of frame
        self.frame.setFixedWidth(90); #set fixed width of frame
        self.frame.setStyleSheet("QFrame"
                                "{"
                                "border:2px solid transparent;"
                                "background-color:rgb(0,92,127);"
                                "border-right:3px solid black;"
                                "border-radius:8px;"
                                "border-bottom:1px inset black;"
                                "}"); #set stylesheet of frame widget

        self.settings_button=QPushButton('Settings'); #create a button widgeticon
        self.settings_button.setFixedHeight(70); #set fixed height of button
        self.settings_button.setFont(QtGui.QFont('Georgia',10)); #set font-family and size of button widget
        self.settings_button.setStyleSheet("QPushButton"
                                            "{"
                                            "padding:10px;"
                                            "border:2px solid transparent;"
                                            "background-color:rgb(0,92,127);"
                                            "background-image:url('settings.png');"
                                            "background-repeat:none;"
                                            "background-position:center left;"
                                            "border-left:4px solid black;"
                                            "padding-left:47px;"
                                            "}"
                                            "QPushButton:hover"
                                            "{"
                                            "border-radius:20px;"                                            "border-bottom:1px solid black;"
                                            "border-left:2px solid transparent;"
                                            "border-bottom:3px solid black;"
                                            "color:white;"
                                            "}"); #set stylesheet of button
        #self.settings_button.setIconSize(QtCore.QSize(40,40)); #set icon size

        hbox=QHBoxLayout(self); #create an horizontal layout
        hbox.addWidget(self.settings_button); #ad widget to horizontal layout
        self.frame.setLayout(hbox); #set layout of frame

        vbox=QVBoxLayout(self); #create a vertical layout
        vbox.addWidget(self.button); #add widget to vertical layout
        vbox.addWidget(self.frame); #add widget to vertical layout

        self.setLayout(vbox); #set layout of windows




        self.show(); #show window

    def slide_frame(self): #class method definition
        width_of_frame=self.frame.width(); #gets the width of frame

        if width_of_frame==90:
            new_width=170;
        else:
            new_width=90;

        self.animation=QtCore.QPropertyAnimation(self.frame,b'minimumWidth'); #create a property animation
        self.animation.setDuration(1500); #set duration of animation
        self.animation.setStartValue(width_of_frame); #set startvalue of animation
        self.animation.setEndValue(new_width); #set endvalue of animation
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart); #set easingcurve of animation
        self.animation.start(); #start animation


app=QApplication(sys.argv); #create an app
window=MainWindow(); #instance variable
sys.exit(app.exec()); #execute app
