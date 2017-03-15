# -*- coding: utf-8 -*-
# @Time     : 2017/3/9 9:31
# @Author   : Span
# @Site     : 
# @File     : 005_对话框2_颜色选择.py
# @Function : Purpose of this script
# @Software : PyCharm

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QFrame,QColorDialog
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        col = QColor(0,0,0)

        self.btn = QPushButton('Dialog',self)
        self.btn.move(20,20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet('QWidget { background-color:%s}'%col.name())
        # print (format('%s'%col.name()))
        self.frm.setGeometry(130,22,100,100)

        self.setGeometry(300,300,250,180)
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()
        print(format('%s' % col.name()))

        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s}' % col.name())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())