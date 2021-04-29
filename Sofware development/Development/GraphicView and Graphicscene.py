from PyQt5.QtWidgets import QApplication,QMainWindow,QGraphicsView,QGraphicsScene,QGraphicsItem
from PyQt5 import QtGui,QtCore
import sys

class window(QMainWindow): #child class
    def __init__(self): #class constructor
        super().__init__(); #inheritance from parent attributes

        self.title='PyQt5 Graphic(View and Scene)';
        self.top=100;
        self.left=100;
        self.width=700;
        self.height=300;

        self.initwindow(); #class method call

    def initwindow(self): #class method

        self.setWindowTitle(self.title); #set window title
        self.setWindowIcon(QtGui.QIcon('home.png')); #set window icon
        self.setGeometry(QtCore.QRect(self.top,self.left,self.width,self.height)); #set window geometry
        self.createGraphicView(); #class method call

        self.show(); #show windows

    def createGraphicView(self): #class method

        self.scene=QGraphicsScene(); #create a graphicsScene

        self.graphicview=QGraphicsView(self.scene,self); #create a graphic view and set scene to it
        self.graphicview.setGeometry(100,100,900,500); #set geometry of graphicview

        self.greenbrush=QtGui.QBrush(QtCore.Qt.green,QtCore.Qt.VerPattern); #green brush
        self.bluebrush=QtGui.QBrush(QtCore.Qt.blue,QtCore.Qt.HorPattern); #create a blue brush
        self.pen=QtGui.QPen(QtCore.Qt.red,5); #create a pen object

        ellipse=self.scene.addEllipse(10,10,150,150,self.pen,self.greenbrush); #add an ellipse to the scene
        rectangle=self.scene.addRect(100,100,200,200,self.pen,self.bluebrush); #add a rectangle to the scene

        ellipse.setFlag(QGraphicsItem.ItemIsMovable); #graphicsitem is movable
        rectangle.setFlag(QGraphicsItem.ItemIsMovable); #graphicsitem is movable

        ellipse.setFlag(QGraphicsItem.ItemIsSelectable); #setflag of item to be selectable

app=QApplication(sys.argv); #create window app
window=window(); #class instance variable
sys.exit(app.exec()); #execute app
