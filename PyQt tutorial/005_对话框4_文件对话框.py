# -*- coding: utf-8 -*-
# @Time     : 2017/3/9 22:20
# @Author   : Span
# @Site     : 
# @File     : 005_对话框4_文件对话框.py
# @Function : Purpose of this script
# @Software : PyCharm
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QTextEdit,QAction,QFileDialog
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('exit.png'),'Open',self)
        openFile.setShortcut('Ctrl + O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300,300,250,200)
        self.setWindowTitle('File Dialog')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self,'Open File','/home')
        if fname[0]:
            f = open(fname[0],'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
