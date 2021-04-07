# Notepad using pyqt5
# Made by Yash Rajput Date:-14-05-2020 ,Time=11:18 PM
import os
import sys
from PyQt5.QtGui import QFont, QPageSize, QPageLayout, QTextCursor, QResizeEvent, QTextBlockFormat, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenuBar, QMenu, QTextEdit, QScrollBar, QStatusBar, \
    QMessageBox, QFileDialog, QInputDialog, QDialogButtonBox, QFontDialog, QDialog, QHBoxLayout, QSizeGrip, QLayout, \
    QGridLayout, QVBoxLayout, QLCDNumber, QFrame, QLabel
from PyQt5.QtCore import Qt,QRect,QTime,QTimer
from PyQt5.QtPrintSupport import QPrinter,QPageSetupDialog,QPrintDialog,QPrintPreviewDialog,QPrintPreviewWidget
from datetime import datetime
from finddialog import *
from replacedialogbox import *
from go import *
class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600,600)
        self.setWindowTitle("Untitled-Notepad")
        self.setWindowIcon(QIcon(r'C:\Users\Yash\PycharmProjects\ppppp\Notepad\icons.png'))
        #self.timer=QTimer(self)
        #self.timer.timeout.connect(self.geometrychange)
        #self.timer.start(10)
        self.menu=QMenuBar(self)
        self.file=QMenu("File",self.menu)
        file=self.file.addAction("New")
        file.setShortcut("Ctrl+N")
        file.triggered.connect(self.files)
        opens=self.file.addAction('Open')
        opens.setShortcut("Ctrl+O")
        opens.triggered.connect(self.open)
        save=self.file.addAction("Save")
        save.setShortcut("Ctrl+S")
        save.triggered.connect(self.save)
        saveas=self.file.addAction("Save as")
        saveas.triggered.connect(self.saveas)
        self.file.addSeparator()
        printsetup=self.file.addAction("Print Preview")
        printsetup.triggered.connect(self.printsetup)
        prints=self.file.addAction("Print")
        prints.setShortcut("Ctrl+P")
        prints.triggered.connect(self.prints)
        self.file.addSeparator()
        exits=self.file.addAction("Exit")
        exits.setShortcut("Alt+X")
        exits.triggered.connect(self.exists)
        self.menu.addMenu(self.file)

        self.edit=QMenu("Edit",self.menu)
        undo=self.edit.addAction("Undo")
        undo.setShortcut("Ctrl+Z")
        undo.triggered.connect(self.undos)
        self.edit.addSeparator()
        self.cuts=self.edit.addAction("Cut")
        self.cuts.setShortcut("Ctrl+X")
        self.cuts.triggered.connect(self.cut)
        self.copys=self.edit.addAction("Copy")
        self.copys.setShortcut("Ctrl+C")
        self.copys.triggered.connect(self.copy)
        self.pastes=self.edit.addAction("Paste")
        self.pastes.setShortcut("Ctrl+V")
        self.pastes.triggered.connect(self.paste)
        self.deletes=self.edit.addAction("Delete")
        self.deletes.setShortcut("Del")
        self.deletes.triggered.connect(self.delete)
        self.edit.addSeparator()
        self.finding=self.edit.addAction("Find")
        self.finding.setShortcut("Ctrl+F")
        self.finding.triggered.connect(self.finds)
        self.findnexts=self.edit.addAction("Find Next")
        self.findnexts.setShortcut("F3")
        self.findnexts.triggered.connect(self.nexts)
        replace=self.edit.addAction("Replace")
        replace.setShortcut("Ctrl+H")
        replace.triggered.connect(self.replace)
        go=self.edit.addAction("Go To")
        go.setShortcut("Ctrl+G")
        go.triggered.connect(self.go)
        check=QTimer(self)
        check.timeout.connect(self.check)
        check.start(100)
        self.edit.addSeparator()
        select=self.edit.addAction("Select All")
        select.setShortcut("Ctrl+A")
        select.triggered.connect(self.select)
        time=self.edit.addAction("Time/Date")
        time.setCheckable(True)
        time.setShortcut("F5")
        time.triggered.connect(self.todaytime)
        self.menu.addMenu(self.edit)

        self.format=QMenu("Format",self.menu)
        self.wrap=self.format.addAction("Word Wrap")
        self.wrap.setCheckable(True)
        self.wrap.setChecked(True)
        self.wrap.triggered.connect(self.word)
        font=self.format.addAction("Font")
        font.triggered.connect(self.fonts)
        self.menu.addMenu(self.format)

        self.view=QMenu("View",self.menu)
        zoom=QMenu("Zoom",self.view)
        In=zoom.addAction("Zoom In")
        In.setShortcut("Ctrl++")
        In.triggered.connect(self.zoomin)
        out=zoom.addAction("Zoom Out")
        out.setShortcut("Ctrl+-")
        out.triggered.connect(self.zoomout)
        restore=zoom.addAction("Restore Default Zoom")
        restore.setShortcut("Ctrl+0")
        restore.triggered.connect(self.restore)
        self.view.addMenu(zoom)
        self.statused=self.view.addAction("Status Bar")
        self.statused.setCheckable(True)
        self.statused.setChecked(True)
        self.statused.triggered.connect(self.status)
        self.menu.addMenu(self.view)

        self.help=QMenu("Help",self.menu)
        help=self.help.addAction("View Help")
        help.triggered.connect(self.helps)
        self.help.addSeparator()
        about=self.help.addAction("About Notepad")
        about.triggered.connect(self.about)
        self.menu.addMenu(self.help)
        self.setMenuBar(self.menu)


        self.centralwidget = QWidget(self)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QRect(0, 0, 600, 579))
        self.textEdit.setUndoRedoEnabled(True)
        font=QFont()
        font.setFamily('Arial')
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.textEdit.setLineWrapMode(self.textEdit.WidgetWidth)
        self.textEdit.setLineWidth(2)
        try:
            self.path=str(sys.argv[1])
            f=open(self.path,'r',encoding='utf-8')
            data=f.read()
            self.textEdit.setText(data)
            self.setWindowTitle(os.path.basename(self.path) + '-Notepad')
        except:
            pass
        self.setCentralWidget(self.centralwidget)
        self.show()
    def closeEvent(self,event):
        if self.close:
            reply = QMessageBox.question(self, "You want to quit? ",
                                               "Task is in progress !",
                                               QMessageBox.Yes,
                                               QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
    def resizeEvent(self,event):
        if self.statused.isChecked()==True:
            self.status()
            self.statusbar.setGeometry(QRect(self.geometry().x()-self.geometry().getCoords()[0],self.geometry().width(),self.geometry().width(), 20))
            self.textEdit.setGeometry(QRect(self.geometry().x()-self.geometry().getCoords()[0], self.geometry().y() -self.geometry().getCoords()[1], self.geometry().width(),
                                        self.geometry().height() - 42))
        else:
            self.textEdit.setGeometry(QRect(self.geometry().x()-self.geometry().getCoords()[0], self.geometry().y() -self.geometry().getCoords()[1], self.geometry().width(),
                                        self.geometry().height() - 21))
    def check(self):
        if len(self.textEdit.toPlainText())==0:
            self.copys.setDisabled(True)
            self.cuts.setDisabled(True)
            self.pastes.setDisabled(True)
            self.deletes.setDisabled(True)
            self.finding.setDisabled(True)
            self.findnexts.setDisabled(True)
        else:
            self.finding.setDisabled(False)
            self.findnexts.setDisabled(False)
            self.copys.setDisabled(False)
            self.cuts.setDisabled(False)
            self.pastes.setDisabled(False)
            self.deletes.setDisabled(False)
        if self.statused.isChecked()==True:
            time = QTime.currentTime()
            text = time.toString("hh:mm:ss")
            self.time.display(text)
            cursor=self.textEdit.textCursor()
            row=cursor.blockNumber()+1
            col=cursor.columnNumber()
            self.label.setText("Row: "+str(row)+"| Col: "+str(col))
    def status(self):
        if self.statused.isChecked()==True:
            self.statusbar = QStatusBar(self)
            self.statusbar.setGeometry(QRect(self.geometry().x() - self.geometry().getCoords()[0], self.geometry().width(), self.geometry().width(), 20))
            self.textEdit.setGeometry(QRect(self.geometry().x() - self.geometry().getCoords()[0],
                                            self.geometry().y() - self.geometry().getCoords()[1],
                                            self.geometry().width(),
                                            self.geometry().height() - 42))
            font = QFont()
            font.setPointSize(10)
            self.statusbar.setFont(font)
            self.label=QLabel("Row: 0 | Col: 0")
            self.statusbar.addPermanentWidget(self.label)
            self.time = QLCDNumber()
            self.time.setDigitCount(8)
            self.time.setFrameShadow(QFrame.Sunken)
            self.time.setFrameShape(QFrame.Panel)
            self.statusbar.addWidget(self.time)
            self.setStatusBar(self.statusbar)
        else:
            self.textEdit.setGeometry(QRect(self.geometry().x() - self.geometry().getCoords()[0],
                                            self.geometry().y() - self.geometry().getCoords()[1],
                                            self.geometry().width(),
                                            self.geometry().height() - 21))

            vboxlayout = QVBoxLayout()
            vboxlayout.setContentsMargins(QtCore.QMargins())
            vboxlayout.setSpacing(0)
            sizegrip = QSizeGrip(self.centralwidget)
            sizegrip.setVisible(True)
            vboxlayout.addWidget(sizegrip, 0, Qt.AlignBottom | Qt.AlignRight)
            self.centralwidget.setLayout(vboxlayout)
            self.statusbar.hide()
    def helps(self):
        QMessageBox.information(self,"Help","This is your notepad made by PyQt5")
    def about(self):
        QMessageBox.information(self,"About","This is the Notepad made by Yash Rajput")
    def files(self):
        self.textEdit.setText('')
        self.setWindowTitle("Untitled-Notepad")
        self.filename=["Untitled-Notepad"]
        self.new=True
    def open(self):
        self.filename=QFileDialog.getOpenFileName(self,'Open File','\home','Text Files (*.txt);;All Files (*)')
        if self.filename[0]:
            f=open(self.filename[0],'r',encoding='utf-8')
        try:
            data=f.read()
            self.textEdit.setText(data)
            self.setWindowTitle(os.path.basename(self.filename[0]) + '-Notepad')
        except:
            pass
    def save(self):
        try:
            if self.new==False:
                w=open(self.filename[0],'w')
                print(self.filename[0])
                w.write(self.textEdit.toPlainText())
                w.close()
            elif self.new==True:
                self.saveas()
        except:
            self.saveas()
    def saveas(self):
        self.filename=QFileDialog.getSaveFileName(self,"Save as",'\home','Text Files(*.txt);;All Files(*)')
        try:
            f=open(self.filename[0],'w')
            f.write(self.textEdit.toPlainText())
            f.close()
            self.new=False
            self.setWindowTitle(os.path.basename(self.filename[0])+'-Notepad')
        except:
            pass
    def exists(self):
        box=QMessageBox.question(self, "You want to quit? ",
                                               "Task is in progress !",
                                               QMessageBox.Yes,
                                               QMessageBox.No)
        if box.exec()==box.Yes:
            self.destroy()
    def undos(self):
        self.textEdit.undo()
    def cut(self):
        self.textEdit.cut()
    def copy(self):
        self.textEdit.copy()
    def paste(self):
        self.textEdit.paste()
    def select(self):
        self.textEdit.selectAll()
    def delete(self):
        cursor=self.textEdit.textCursor()
        cursor.removeSelectedText()
    def todaytime(self):
        self.textEdit.insertPlainText(str(datetime.today()))
    def word(self):
        if self.wrap.isChecked():
            self.textEdit.setLineWrapMode(self.textEdit.WidgetWidth)
        else:
            self.textEdit.setLineWrapMode(self.textEdit.NoWrap)
    def fonts(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)
    def zoomin(self):
        font=QFont(self.textEdit.font())
        size=font.pointSize()
        font.setPointSize(size+1)
        self.textEdit.setFont(font)
    def zoomout(self):
        font = QFont(self.textEdit.font())
        size = font.pointSize()
        font.setPointSize(size-1)
        self.textEdit.setFont(font)
    def restore(self):
        font=QFont()
        font.setPointSize(8)
        font.setFamily('Arial')
        self.textEdit.setFont(font)
    def finds(self):
        self.pc=Find(w)
        self.pc.exec()
    def replace(self):
        p=replaces(w)
        p.exec()
    def go(self):
        temp=Go(w)
        temp.exec()
    def prints(self):
        self.printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            w.textEdit.print_(self.printer)
    def printsetup(self):
        self.printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintPreviewDialog(self.printer, self)
        dialog.paintRequested.connect(self.handle_paint_request)
        dialog.exec_()
    def handle_paint_request(self, printer):
        self.textEdit.print(printer)

    def nexts(self):
        self.pc.click()
class Find(QDialog):
    def __init__(self,parent):
        super(Find,self).__init__(parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.pos=0
        self.prev=0
        self.ui.radioButton.setCheckable(True)
        self.ui.pushButton.clicked.connect(self.click)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.show()
    def click(self):
        self.cursor = w.textEdit.textCursor()
        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtGui.QColor("light blue")))
        # Setup the regex engine
        pattern = self.ui.lineEdit.text()
        regex = QtCore.QRegExp(pattern)
        # Process the displayed document
        if self.pos==len(w.textEdit.toPlainText()):
            self.pos=0
        index = regex.indexIn(w.textEdit.toPlainText(), self.pos)
        self.pos=index+regex.matchedLength()
        self.cursor.setPosition(index,QtGui.QTextCursor.MoveAnchor)
        self.cursor.setPosition(self.pos, QtGui.QTextCursor.KeepAnchor)
        w.textEdit.setTextCursor(self.cursor)
class replaces(QDialog):
    def __init__(self,parent):
        super(replaces,self).__init__(parent)
        self.ui=Ui_Find()
        self.ui.setupUi(self)
        self.pos=0
        self.prev=0
        self.index=0
        self.power=False
        self.click()
        self.ui.pushButton.clicked.connect(self.click)
        self.ui.pushButton_2.clicked.connect(self.replace)
        self.ui.pushButton_3.clicked.connect(self.replaceall)
        self.ui.pushButton_4.clicked.connect(self.Close)
        self.show()
    def click(self):
        self.cursor = w.textEdit.textCursor()
        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtGui.QColor("light blue")))
        # Setup the regex engine
        pattern = self.ui.lineEdit.text()
        regex = QtCore.QRegExp(pattern)
        # Process the displayed document
        if self.pos==len(w.textEdit.toPlainText()):
            self.pos=0
        index = regex.indexIn(w.textEdit.toPlainText(), self.pos)
        self.pos=index+regex.matchedLength()
        self.cursor.setPosition(index,QtGui.QTextCursor.MoveAnchor)
        self.cursor.setPosition(self.pos, QtGui.QTextCursor.KeepAnchor)
        try:
            w.textEdit.setTextCursor(self.cursor)
        except: pass
        self.power=True
    def replace(self):
        self.cursor.removeSelectedText()
        if self.power==True:
            self.cursor.insertText(self.ui.lineEdit_2.text())
            self.power=False
        self.cursor.clearSelection()
        w.textEdit.setTextCursor(self.cursor)
    def replaceall(self):
        cursor=w.textEdit.textCursor()
        word=self.ui.lineEdit.text()
        regex=QtCore.QRegExp(word)
        self.pos=0
        index=regex.indexIn(w.textEdit.toPlainText(),self.pos)
        while index!=-1:
            self.pos=index+regex.matchedLength()
            cursor.setPosition(index, QtGui.QTextCursor.MoveAnchor)
            cursor.setPosition(self.pos, QtGui.QTextCursor.KeepAnchor)
            w.textEdit.setTextCursor(cursor)
            cursor.removeSelectedText()
            cursor.insertText(self.ui.lineEdit_2.text())
            w.textEdit.setTextCursor(cursor)
            index = regex.indexIn(w.textEdit.toPlainText(), self.pos)
        self.power=False
    def Close(self):
        self.close()
class Go(QDialog):
    def __init__(self,parent):
        super(Go,self).__init__(parent)
        self.ui=Ui_Go()
        self.ui.setupUi(self)
        point=w.textEdit.textCursor()
        self.ui.lineEdit.setText(str(point.blockNumber()+1))
        self.ui.pushButton.clicked.connect(self.check)
        self.ui.pushButton_2.clicked.connect(self.cancel)
    def check(self):
        try:
            int(self.ui.lineEdit.text())
            self.nexts()
        except:
            QMessageBox.critical(self,"Error","Please enter integer only")
    def nexts(self):
        cursor=w.textEdit.textCursor()
        number=int(self.ui.lineEdit.text())-cursor.blockNumber()
        if number>0:
            cursor.movePosition(QtGui.QTextCursor.Down,QtGui.QTextCursor.MoveAnchor,number-1)
        else:
            cursor.movePosition(QtGui.QTextCursor.Up,QtGui.QTextCursor.MoveAnchor,abs(number)+1)
        w.textEdit.setTextCursor(cursor)
        self.close()
    def cancel(self):
        self.close()

if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon(r'C:\Users\Yash\PycharmProjects\ppppp\Notepad\icons.png'))
    app.setApplicationVersion("1.0.0")
    w=GUI()
    w.show()
    app.exec()