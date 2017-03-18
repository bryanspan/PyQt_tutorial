# -*- coding: utf-8 -*-
# @Time     : 2017/3/17 14:52
# @Author   : Span
# @Site     : 
# @File     : 008_QMessageBox.py
# @Function : Purpose of this script
# @Software : PyCharm

# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox,QApplication,QWidget,QPushButton,QLineEdit,QInputDialog

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.myButton = QPushButton(self)
        self.myButton.setObjectName("mybutton")
        self.myButton.setText("Text")
        self.myButton.clicked.connect(self.msg2)

    def msg(self):
        reply = QMessageBox.information(self,"标题","消息",QMessageBox.Yes | QMessageBox.No)

    def msg2(self):
        soubleNum,ok1 = QInputDialog.getDouble(self,"标题","计数：",37.56,-10000,10000,2)
        intNum,ok2 = QInputDialog.getInt(self,"标题","计数：",37,-10000,10000,2)
        stringNum,ok3 = QInputDialog.getText(self,"标题","姓名：",QLineEdit.Normal,"王尼玛")
        items = ["Sprint","Summer","Fall","Winter"]
        item,ok4 = QInputDialog.getItem(self,"标题","Season：",items,1,True)
        text,ok5 = QInputDialog.getMultiLineText(self,"标题","Address:","John Doe\nFreedom Street")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())