from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QSlider,QStyle,QVBoxLayout,QGroupBox,QFileDialog,QHBoxLayout
from PyQt5 import QtCore,QtGui
import sys
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

class window(QWidget): #child class
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parent attribute

        self.title='ChiEngine';
        self.top=100;
        self.left=100;
        self.width=700;
        self.height=300;

        self.initui(); #class method call
        p=self.palette(); #create a palette
        p.setColor(QtGui.QPalette.Window,QtCore.Qt.black); #set palette color
        self.setPalette(p); #set palette

    def initui(self): #class method

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set geometry of windows

        self.mediaplayer=QMediaPlayer(None,QMediaPlayer.VideoSurface); #create a media player object

        self.videowidget=QVideoWidget(); #create a video widget object

        self.playbtn=QPushButton(); #create a button widget
        self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay)); #set icon of playbutton
        self.playbtn.clicked.connect(self.play_video); #connect a sigal to a slot
        self.playbtn.setEnabled(False); #set button enabled to false

        self.openbtn=QPushButton('Open Video'); #create a button widget
        self.openbtn.clicked.connect(self.open_video); #connect a signal to a slot

        self.slider=QSlider(QtCore.Qt.Horizontal); #create a slider object
        self.slider.setRange(0,0); #set range to 0,0
        self.slider.sliderMoved.connect(self.setposition); #connect a signal to a slot


        vbox=QVBoxLayout(self); #create a vertical layout

        hbox=QHBoxLayout(self); #create a horizontal layout
        hbox.setContentsMargins(0,0,0,0); #set contents margin

        hbox.addWidget(self.openbtn); #add widget to vertical layout
        hbox.addWidget(self.playbtn); #add widget to vertical layout
        hbox.addWidget(self.slider); #add widget to vertical layout

        self.setLayout(vbox);  # setwindows layout to vertical layout


        self.mediaplayer.stateChanged.connect(self.mediastate_changed);  #connect a signal to a slot
        self.mediaplayer.setVideoOutput(self.videowidget); #set video output to vide widget
        self.mediaplayer.positionChanged.connect(self.position_changed); #connect a signal to a slot
        self.mediaplayer.durationChanged.connect(self.duration_changed); #connect a signal to a slot

        vbox.addWidget(self.videowidget);# add widget to vertical layout
        vbox.addLayout(hbox); # add widget to vertical layout





        self.show(); #show windows

    def play_video(self): #.class method
        if self.mediaplayer.state() == QMediaPlayer.PlayingState:
            self.mediaplayer.pause(); #pause media
        else:
            self.mediaplayer.play(); #play media

    def open_video(self): #class method
        fn, _=QFileDialog.getOpenFileName(self,'Open Media'); #getopenfilename
        if fn!='':
            self.mediaplayer.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(fn))); #set media
            self.playbtn.setEnabled(True); #set button enabled true

    def mediastate_changed(self,state): #class method
        if self.mediaplayer.state() == QMediaPlayer.PlayingState:
            self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause)); #set button icon to pause
        else:
            self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay)); #set button icon play

    def position_changed(self,position): #class method
        self.slider.setValue(position); #set value of slider

    def duration_changed(self,duration): #class method
        self.slider.setRange(0,duration); #set range of slider

    def setposition(self,position): #classs method
        self.mediaplayer.setPosition(position); #set mediaplayer position to position

app=QApplication(sys.argv); #create an app
window=window(); #instance variable
sys.exit(app.exec()); #execute application