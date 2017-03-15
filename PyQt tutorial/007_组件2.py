# -*- coding: utf-8 -*-
# @Time     : 2017/3/14 11:07
# @Author   : Span
# @Site     : 
# @File     : 007_组件2.py
# @Function : Purpose of this script
# @Software : PyCharm
import sys
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QLabel,QApplication,QLineEdit,QSplitter,QFrame,QStyleFactory,QComboBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        # self.initUI_Pixmap()
        # self.initUI_LineEdit()
        # self.initUI_Splitter()
        self.initUi_QComBox()

    def initUI_Pixmap(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("icon/test.jpg")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300,200)
        self.setWindowTitle("Red Rock")
        self.show()
    def initUI_LineEdit(self):
        self.lbl = QLabel(self)
        qle = QLineEdit(self)

        qle.move(60,100)
        self.lbl.move(60,40)

        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300,200,280,170)
        self.setWindowTitle("QLineEdit")
        self.show()

    def onChanged(self,text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def initUI_Splitter(self):
        # 创建一个水平箱布局
        hbox = QHBoxLayout(self)

        #创建一个QFrame框架窗口
        topleft = QFrame(self)

        #设置QFrame的形状参数为一个枚举对象
        # draws a rectangular panel with a look that depends on the current GUI style. It can be raised or sunken
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        # This type is used to signify an object's orientation
        #QSplitter的参数指定了组件的方向
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        #创建一个垂直方向布局所添加组件的QSplitter组件
        splitter2 = QSplitter(Qt.Vertical)
        #将splitter1添加到splitter2中
        splitter2.addWidget(splitter1)
        #垂直方向布局 再添加bottom Frame
        splitter2.addWidget(bottom)

        #将包含了splitter1的splitter2 添加到hbox中
        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle("QSplitter")
        self.show()

    def initUi_QComBox(self):
        self.lbl = QLabel("Ubuntu",self)
        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")

        combo.move(50,50)
        self.lbl.move(50,150)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle("QComboBox")
        self.show()

    def onActivated(self,text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())