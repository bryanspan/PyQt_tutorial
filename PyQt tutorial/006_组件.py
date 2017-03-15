# -*- coding: utf-8 -*-
# @Time     : 2017/3/10 21:31
# @Author   : Span
# @Site     : 
# @File     : 006_组件.py
# @Function : Purpose of this script
# @Software : PyCharm

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QPushButton,QFrame,QSlider,QLabel,QProgressBar,QCalendarWidget
from PyQt5.QtCore import Qt,QBasicTimer,QDate
from PyQt5.QtGui import QColor,QPixmap

class Example(QWidget):
    def __init__(self):
        super().__init__()
        # self.initUI_CheckBox()
        self.initUI_Button_Shift()
        # self.initUI_Slider()
        # self.initUI_ProgressBar()
        # self.initUI_Calender()

    def initUI_CheckBox(self):
        cb = QCheckBox('Show Title',self)
        cb.move(20,20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300,300,250,200)
        self.setWindowTitle('CheckBox')
        self.show()

    def changeTitle(self,state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')

    def initUI_Button_Shift(self):
        self.col = QColor(0,0,0)
        redb = QPushButton('Red',self)
        redb.setCheckable(True)
        redb.move(10,10)
        # clicked[bool] 说明点击的信号是一个bool值 将这个bool值信号 和setcolor槽连接
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green',self)
        greenb.setCheckable(True)
        greenb.move(10,60)
        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue',self)
        blueb.setCheckable(True)
        blueb.move(10,110)
        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet('QWidget {background-color:%s}' % self.col.name())

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('Toggle Button')
        self.show()

    def setColor(self,pressed):
        #因为有多个组件都绑定到了槽中 通过self.sender()来找出发送信号的是哪一个组件
        #然后根据组件clicked返回值对组件的颜色进行设置
        source = self.sender()
        if pressed:
            val = 255
        else:
            val = 0
        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        self.square.setStyleSheet('QFrame{background-color: %s}'%self.col.name())

    def initUI_Slider(self):
        sld = QSlider(Qt.Horizontal,self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30,40,100,30)
        sld.valueChanged[int].connect(self.valueChange)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('icon\\mute.png'))
        self.label.setGeometry(160,40,80,30)

        self.setGeometry(300,300,280,200)
        self.setWindowTitle('QSlider')
        self.show()

    def valueChange(self,value):
        if value == 0:
            self.label.setPixmap(QPixmap('icon\\mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('icon\\min.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('icon\\med.png'))
        else:
            self.label.setPixmap(QPixmap('icon\\max.png'))

    def initUI_ProgressBar(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30,40,200,25)

        self.btn = QPushButton('Start',self)
        self.btn.move(40,80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('Progress Bar')
        self.show()
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100,self)
            self.btn.setText('Stop')

    def initUI_Calender(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(30,20)
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130,260)

        self.setGeometry(300,300,350,300)
        self.setWindowTitle('Calender')
        self.show()

    def showDate(self,date):
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())