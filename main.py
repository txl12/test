# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QLineEdit,QVBoxLayout, QPushButton, QFormLayout
import sys
from test import my_system
import student 
class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(lineEditDemo, self).__init__(parent)
        self.setWindowTitle("QLineEdit 例子")
        flo = QVBoxLayout()
        self.btnPress1 = QPushButton("录入学生信息")
        self.btnPress2 = QPushButton("打印各寝室人员列表")
        self.btnPress3 = QPushButton("用学号索引打印特定学生信息")
        self.btnPress4 = QPushButton("打印所有学生信息")
        self.btnPress5 = QPushButton("调整寝室")
        self.btnPress6 = QPushButton("退出程序")
        flo.addWidget(self.btnPress1)
        flo.addWidget(self.btnPress2)
        flo.addWidget(self.btnPress3)
        flo.addWidget(self.btnPress4)
        flo.addWidget(self.btnPress5)
        flo.addWidget(self.btnPress6)
        self.setLayout(flo)
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)
        self.btnPress3.clicked.connect(self.btnPress3_Clicked)
        self.btnPress4.clicked.connect(self.btnPress4_Clicked)
        self.btnPress5.clicked.connect(self.btnPress5_Clicked)
        self.btnPress6.clicked.connect(self.btnPress6_Clicked)
    def btnPress1_Clicked(self):
        self.one = student.first()
        self.one.show()
        # print("录入学生信息")
    def btnPress2_Clicked(self):
        self.two = student.second()
        self.two.show()
        print("打印各寝室人员列表")
    def btnPress3_Clicked(self):
        self.three = student.third()
        self.three.show()
        print("用学号索引打印特定学生信息")
    def btnPress4_Clicked(self):
        self.four = student.fourth()
        self.four.show()
        print("打印所有学生信息")
    def btnPress5_Clicked(self):
        self.five = student.fifth()
        self.five.show()
        print("调整寝室")
    def btnPress6_Clicked(self):
        print("退出程序")
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(app.exec_())
