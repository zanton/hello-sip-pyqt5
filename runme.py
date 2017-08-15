#!/usr/bin/python

import sys, random, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sip

sys.path.append(os.getcwd()+"/sip")
import hello

class Viewport(QWidget):
    def __init__(self):
        super(Viewport, self).__init__()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        
        qp.setPen(Qt.red)
        qp.setBrush(QColor(255, 80, 0, 160))
        qp.drawRect(100, 20, 50, 30)
        qp.drawText(200, 35, "I'm drawn in Python")

        # delegate drawing to C++ 
        h = hello.Hello()
        h.printme()
        h.draw(sip.unwrapinstance(qp))
        
        qp.end()
        
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        
    def initUI(self):
        # main window
        self.setGeometry(300, 200, 500, 300)
        self.center()
        self.setWindowTitle('Hello')

        # status bar
        self.statusBar().showMessage('Ready')

        # menu bar
        menubar = self.menuBar()
        #menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        
        exitAct = QAction('&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAct)
        
        # toolbar
        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.addAction(exitAct)

        # central widget
        cwidget = Viewport()
        self.setCentralWidget(cwidget)
        
        # show
        self.show()

    def contextMenuEvent(self, event):
           cmenu = QMenu(self)
           openAct = cmenu.addAction("Open")
           quitAct = cmenu.addAction("Quit")
           action = cmenu.exec_(self.mapToGlobal(event.pos()))
           if action == quitAct:
               qApp.quit()
               
    def xcloseEvent(self, event):
        print("closeEvent handler.")
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        windowrec = self.frameGeometry()
        centerpt = QDesktopWidget().availableGeometry().center()
        windowrec.moveCenter(centerpt)
        self.move(windowrec.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
