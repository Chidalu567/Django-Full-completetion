from PyQt5.QtWidgets import QApplication,QDialog,QTableWidget,QTableWidgetItem,QPushButton,QMessageBox,QVBoxLayout
from PyQt5 import QtGui,QtCore
import sys
import pymysql as mdb

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
        self.tablewidget.setColumnCount(2); #set column count

        self.tablewidget.setHorizontalHeaderItem(0,QTableWidgetItem('UserName')); #set item of UserName to tablewidget
        self.tablewidget.setHorizontalHeaderItem(1,QTableWidgetItem('Email')); #set item of Email to table widget
        vbox.addWidget(self.tablewidget); #add widget to vertical layout

        self.button=QPushButton('Insert Data'); #create buton widget
        self.button.clicked.connect(self.insertdata); #connect a signal to a slot
        vbox.addWidget(self.button); #add widget to vertical layout

        self.setLayout(vbox); #set windows layout to vertucal layout

        self.show(); #show window

    def insertdata(self): #class method
        name=[self.tablewidget.item(row,0).text() for row in range(self.tablewidget.rowCount())]; #python comphrehension list
        email=[self.tablewidget.item(row,1).text() for row in range(self.tablewidget.rowCount())]; #python list comphrehension
        newname=''.join(name);
        newemail=''.join(email);
        print(newname);
        print(newemail);
        conn=mdb.connect(host='localhost',user='root',password='',database='pyqt5 database'); #connect to database
        cur=conn.cursor(); #create a cursor widget
        cur.execute("INSERT INTO data(UserName,Email) VALUES('%s','%s')"%(newname,newemail)); #insert into table_name values()
        conn.commit(); #commit changes
        conn.close(); #close connection
        QMessageBox.about(self,'Connecting.....','Inserted Successfully'); #create an about messagebox widget


app=QApplication(sys.argv); #create a window app
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute window app
