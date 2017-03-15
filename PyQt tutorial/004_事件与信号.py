# -*- coding: utf-8 -*-
# @Time     : 2017/3/6 10:11
# @Author   : Span
# @Site     : 
# @File     : 004_事件与信号.py
# @Function : Purpose of this script
# @Software : PyCharm
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QSlider,QLCDNumber,QVBoxLayout

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal,self)
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300,300,200,200)
        self.setWindowTitle('signal and slot')
        self.show()

    def keyPressEvent(self, e):
        if e.key() == (Qt.Key_Alt and Qt.Key_Shift and Qt.Key_A):
            print ("hahahah")
            self.close()
            e.accept()
        # if e.key() == Qt.Key_Escape and e.key == Qt.Key_Shift:
        #     self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
