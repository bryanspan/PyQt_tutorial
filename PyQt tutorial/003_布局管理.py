# -*- coding: utf-8 -*-
# @Time     : 2017/3/5 19:43
# @Author   : Span
# @Site     : 
# @File     : 003_布局管理.py
# @Function : Purpose of this script
# @Software : PyCharm
import sys
from PyQt5.QtWidgets import QWidget,QLabel,QApplication,QPushButton,QHBoxLayout,QVBoxLayout,QGridLayout,QTextEdit,QLineEdit

class Example(QWidget):

    def __init__(self):
        super().__init__()

        # self.initUI_Absolute()
        # self.initUI_Box()

    def initUI_Absolute(self):
        lbl1 = QLabel('Zetcode',self)
        lbl1.move(15,10)

        lbl2 = QLabel('tutorials',self)
        lbl2.move(35,40)

        lbl3 = QLabel('for programers',self)
        lbl3.move(55,70)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle("Absolute")

        self.show()

    def initUI_Box(self):
        okButton = QPushButton("Ok")
        cancelButton = QPushButton("Cancel")
        vbutton = QPushButton("vertical")

        hbox = QHBoxLayout()
        # hbox.addStretch(1.txt)
        hbox.addWidget(okButton)
        hbox.addStretch(1)
        hbox.addWidget(cancelButton)


        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        vbox.addWidget(vbutton)

        self.setLayout(vbox)

        self.setGeometry(300,100,500,100)
        self.setWindowTitle("Box")
        self.show()

    def initUI_Grid(self):
        grid = QGridLayout()
        self.setLayout(grid)
        names = ['Cls','Bck','','Close',
                 '7','8','9','/',
                 '4','5','6','*',
                 '1.txt','2','3','-',
                 '0','.','=','+']
        positions = [(i,j) for i in range(5)for j in range(4)]

        for position,name in zip(positions,names):
            if name =='':
                continue
            button = QPushButton(name)
            grid.addWidget(button,*position)

        # for i in zip(positions,names):
        #     print (i)
        self.move(300,150)
        self.setWindowTitle('Calculator')
        self.show()

    def initUI_TextEdit(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)

        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)
        grid.addWidget(review,3,0)
        grid.addWidget(reviewEdit,3,1,3,1)

        self.setLayout(grid)

        self.setGeometry(300,300,350,300)

        self.setWindowTitle('Review')
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex= Example()
    # ex.initUI_Absolute()
    # ex.initUI_Box()
    # ex.initUI_Grid()
    ex.initUI_TextEdit()
    sys.exit(app.exec_())