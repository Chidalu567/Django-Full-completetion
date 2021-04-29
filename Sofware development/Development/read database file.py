from PyQt5.QtWidgets import QApplication,QDialog,QTableWidget,QTableWidgetItem,QPushButton,QMessageBox,QVBoxLayout
from PyQt5 import QtGui,QtCore
import sys
import pymysql as mdb
import ast

def myconverter(mydata): #function definitioni
    def cvt(data): #function definition
        try:
            return ast.literal_eval(data); #retun a literal_evaluation of data
        except Exception:
            return str(data);
    return tuple(map(cvt,mydata));


class mywindow(QDialog): #child class

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

        vbox=QVBoxLayout(self); #create a vertucal layout

        self.tablewidget=QTableWidget(); #create a table widget
        self.tablewidget.setRowCount(1); #set tabkle widget row count
        self.tablewidget.setColumnCount(3); #set column count

        self.tablewidget.setHorizontalHeaderItem(0,QTableWidgetItem('ID')); #set item of ID to tablewidget
        self.tablewidget.setHorizontalHeaderItem(1,QTableWidgetItem('UserName')); #set horizontal header item of UserName to tablewidget
        self.tablewidget.setHorizontalHeaderItem(2,QTableWidgetItem('Email')); #set horizontal header item of Email to table widget
        vbox.addWidget(self.tablewidget); #add widget to vertical layout

        self.button=QPushButton('Load Data'); #create buton widget
        self.button.clicked.connect(self.loaddata); #connect a signal to a slot
        vbox.addWidget(self.button); #add widget to vertical layout

        self.setLayout(vbox); #set windows layout to vertucal layout

        self.show(); #show window

    def loaddata(self): #class method definition
        conn=mdb.connect(host='localhost',user='root',password='',database='pyqt5 database'); #connect to the database
        cur=conn.cursor(); #create a cursor to carry out sql commands
        rows=cur.execute("select * from data"); #select * from table_name
        data=cur.fetchall(); #fetch all value in data
        for row in data:
            self.addTable(myconverter(row)); #class method call
        conn.commit(); #commit to connections
        conn.close(); #close connections


    def addTable(self,columns): #class method defnition
        rowpos=self.tablewidget.rowCount(); #do a row count of tablewidget
        self.tablewidget.insertRow(rowpos); #insert rowposition
        for i,column in enumerate(columns):
            self.tablewidget.setItem(rowpos,i,QTableWidgetItem(str(column))); #set item to tablewidget



app=QApplication(sys.argv); #create a window app
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute window app
