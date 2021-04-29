from PyQt5.QtWidgets import QApplication,QMenuBar,QMainWindow,QToolBar,QFileDialog,QTextEdit,QFontDialog,QColorDialog,QAction
import sys
from PyQt5 import QtCore,QtGui
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog,QPrintPreviewDialog

class mywindow(QMainWindow): #child class
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
        self.createmenu(); #class method call
     #   self.create_editor();

        self.show(); #show window

    def createmenu(self): #class method


        menubar=self.menuBar(); #create a menubar widget
        filemenu=menubar.addMenu('File'); #add file to menubar
        editmenu=menubar.addMenu('Edit'); #add Edit to menubar
        viewmenu=menubar.addMenu('View'); #add View to menubar
        helpmenu=menubar.addMenu('Help'); #add help to menubar

        self.editor=QTextEdit(); #create a text edit widget
        self.setCentralWidget(self.editor);

        openaction=QAction(QtGui.QIcon('open.png'), 'open', self); #create aan aCTION
        openaction.setShortcut('Ctrl+o'); #create action shortcut
        filemenu.addAction(openaction); #add action to filemenu

        saveaction=QAction(QtGui.QIcon('save-as.png'), 'save', self); #create aan aCTION
        saveaction.setShortcut('Ctrl+s'); #create action shortcut
        saveaction.triggered.connect(self.saveas('me')); #connection a signal to a slot
        filemenu.addAction(saveaction); #add action to filemenu

        copyaction=QAction(QtGui.QIcon('copy.png'), 'copy', self); #create aan aCTION
        copyaction.setShortcut('Ctrl+c'); #create action shortcut
        filemenu.addAction(copyaction); #add action to filemenu

        quitaction=QAction(QtGui.QIcon('Quit.png'), 'quit', self); #create aan aCTION
        quitaction.setShortcut('Ctrl+e'); #create action shortcut
        quitaction.triggered.connect(self.exit); #connect a signal to a slot
        filemenu.addAction(quitaction); #add action to filemenu

        fontaction=QAction(QtGui.QIcon('font.png'), 'font', self); #create an action
        fontaction.setShortcut('Crtl+f'); #set action shortcut
        fontaction.triggered.connect(self.create_fontdialog); #connect a signal to a slot
        editmenu.addAction(fontaction); #add action to menubar

        coloraction=QAction(QtGui.QIcon('color.png'), 'color', self); #create an action
        coloraction.triggered.connect(self.colordialog); #connect a signal to a slot
        editmenu.addAction(coloraction); #add action to menubar

        printaction=QAction(QtGui.QIcon('print.png'), 'print', self); #create an action
        printaction.setShortcut('Ctrl+p'); #set action shortcut
        printaction.triggered.connect(self.printdialog); #connect a signal to a slot
        viewmenu.addAction(printaction); #add action to menubar

        printpreviewaction=QAction(QtGui.QIcon('printpreview.png'), 'preview', self); #create an action
        printpreviewaction.triggered.connect(self.ppdialog); #connect a signal to a slot
        viewmenu.addAction(printpreviewaction); #add action to menubar

        toolbar=self.addToolBar('toolbar'); #create a toolbar widget
        '''ADD Actions to toolbar'''
        toolbar.addAction(copyaction);
        toolbar.addAction(openaction);
        toolbar.addAction(fontaction);
        toolbar.addAction(coloraction);
        toolbar.addAction(printaction);
        toolbar.addAction(printpreviewaction)
        toolbar.addAction(quitaction);



    def create_fontdialog(self): #clas method
        font,ok=QFontDialog.getFont(); #get selected font in fontdialog
        if ok:
            self.editor.setFont(font); #set texteditor font to selected font

    def colordialog(self): #class method
        color=QColorDialog.getColor(); #get selected color in colordialog
        self.editor.setTextColor(color); #change the text color in editor


    def exit(self): #class method
        self.close(); #close window

    def printdialog(self): #class method
        printer=QPrinter(QPrinter.HighResolution); #create a printer object
        dialog=QPrintDialog(printer,self); #add printer to printdialog

        if dialog.exec_() == QPrintDialog.Accepted:
            self.editor.print_(printer); #print text to printer

    def ppdialog(self):
        printer=QPrinter(QPrinter.HighResolution); #create a printer object
        previewdialog=QPrintPreviewDialog(printer,self);
        previewdialog.paintRequested.connect(self.printpreview); #connect a signal to a slot
        previewdialog.exec_(); #execute my preview dialog

    def printpreview(self,printer):
        self.editor.print_(printer);

    def saveas(self,filename): #class method

        fn, _=QFileDialog.getSaveFileName(self,'Export pdf',filename,'Pdf files (.pdf);;All Files()'); #get the filename in filedialog
        if fn !='':
            if QtCore.QFileInfo(fn).suffix()=='': fn+='.pdf'
            printer=QPrinter(QPrinter.HighResolution); #create a printer object
            printer.setOutputFileName(fn); #set printer outputfilename
            printer.setOutputFormat(QPrinter.PdfFormat); #set printer format
            self.editor.document().print_(printer); #print the file as pdf


app=QApplication(sys.argv); #create a window app
window=mywindow(); #instance variable
sys.exit(app.exec()); #execute window app