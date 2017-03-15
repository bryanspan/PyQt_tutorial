# -*- coding: utf-8 -*-
# @Time     : 2017/3/4 10:35
# @Author   : Span
# @Site     : 
# @File     : 002_菜单和工具栏.py
# @Function : Purpose of this script
# @Software : PyCharm

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QAction,qApp,QTextEdit
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction(QIcon('exit.png'),'&Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        exitAction.triggered.connect(self.close)

        self.statusBar().showMessage('Ready')
        self.toolbar = self.addToolBar('Exit')

        self.toolbar.addAction(exitAction)

        menubar = self.menuBar()
        filemenu = menubar.addMenu('&File')
        funcmeun = menubar.addMenu('&Print')
        filemenu.addAction(exitAction)


        self.setGeometry(300,300,250,200)
        self.setWindowTitle('StatusBar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())