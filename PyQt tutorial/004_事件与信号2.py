# -*- coding: utf-8 -*-
# @Time     : 2017/3/8 17:15
# @Author   : Span
# @Site     : 
# @File     : 004_事件与信号2.py
# @Function : Purpose of this script
# @Software : PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        btn1 = QPushButton('Button1',self)
        btn1.move(30,50)

        btn2 = QPushButton('Button2',self)
        btn2.move(150,50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Event Sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())