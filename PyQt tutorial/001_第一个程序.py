# -*- coding: utf-8 -*-
# @Time     : 2017/3/3 20:51
# @Author   : Span
# @Site     : 
# @File     : 001_第一个程序.py
# @Function : Purpose of this script
# @Software : PyCharm
import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QToolTip,QMessageBox,QDesktopWidget)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication

# if __name__ == '__main__':
#     c = []
#     app = QApplication(c)
#     w = QWidget()
#     w.resize(250,150)
#     w.move(300,300)
#     w.setWindowTitle('Simplw')
#     w.show()
#     sys.exit(app.exec_())

#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300,200,300,100)
#         self.setWindowTitle('Icon')
#         self.setWindowIcon(QIcon('web1.png'))
#         self.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     app.exec_()
#     sys.exit()


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('quit',self)
        btn.setToolTip('This is a <b>QPushButton</b>widget')
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(150,150)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Message Box')
        self.setWindowIcon(QIcon('web1.png'))
        self.center()
        self.show()

    def closeEvent(self,event):
        reply = QMessageBox.question(self,'Message','Are you sure to exit?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
