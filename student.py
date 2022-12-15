# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtCore
from test import my_system
class first(QWidget):
    def __init__(self, parent=None):
        super(first, self).__init__(parent)
        self.setWindowTitle("first")
        flo = QFormLayout()
        self.nameLineEdit = QLineEdit()
        self.studypNoEchoLineEdit = QLineEdit()
        self.sexLineEdit = QLineEdit()
        self.roomEditLineEdit = QLineEdit()
        self.ageEditLineEdit = QLineEdit()

        flo.addRow("姓名:", self.nameLineEdit)
        flo.addRow("学号:", self.studypNoEchoLineEdit)
        flo.addRow("性别:", self.sexLineEdit)
        flo.addRow("寝室:",self.roomEditLineEdit)
        flo.addRow("年龄:",self.ageEditLineEdit)

        self.nameLineEdit.setPlaceholderText("请输入姓名")
        self.studypNoEchoLineEdit.setPlaceholderText("请输入学号")
        self.sexLineEdit.setPlaceholderText("请输入性别")
        self.roomEditLineEdit.setPlaceholderText("请输入寝室")
        self.ageEditLineEdit.setPlaceholderText("请输入年龄")

        # 设置显示效果
        self.nameLineEdit.setEchoMode(QLineEdit.Normal)
        self.studypNoEchoLineEdit.setEchoMode(QLineEdit.Normal)
        self.sexLineEdit.setEchoMode(QLineEdit.Normal)
        self.roomEditLineEdit.setEchoMode(QLineEdit.Normal)
        self.ageEditLineEdit.setEchoMode(QLineEdit.Normal)

        self.btnPress1 = QPushButton("自动分配寝室")
        self.btnPress2 = QPushButton("保存学生信息")
        self.btnPress3 = QPushButton("退出")
        flo.addWidget(self.btnPress1)
        flo.addWidget(self.btnPress2)
        flo.addWidget(self.btnPress3)
        self.setLayout(flo)
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)
        self.btnPress3.clicked.connect(self.btnPress3_Clicked)
    def btnPress1_Clicked(self):
        a=my_system()
        sex=self.sexLineEdit.text()
        if sex=="男"or sex=="女":
            self.roomEditLineEdit.setText(a.auto_room(self.sexLineEdit.text()))
            print("自动分配寝室成功")
        else:
            print("自动分配寝室失败")

    def btnPress2_Clicked(self):
        print("保存学生信息")
        a=my_system()
        if(self.nameLineEdit.text()):
            if(self.studypNoEchoLineEdit.text()) and ( a.judeg_study_num_is(self.studypNoEchoLineEdit.text())):
                if(self.sexLineEdit.text())and (self.sexLineEdit.text()=="男"or self.sexLineEdit.text()=="女"):
                    if(self.roomEditLineEdit.text()):
                        if(self.ageEditLineEdit.text()):
                            if a.manually_room(self.roomEditLineEdit.text(),self.sexLineEdit.text()):
                                a.add_student_information(self.nameLineEdit.text(),self.studypNoEchoLineEdit.text(),self.sexLineEdit.text(),self.roomEditLineEdit.text(),self.ageEditLineEdit.text())
                                print("保存成功")
                            else:
                               print("错误的寝室号") 
                        else:
                            print("请输入年龄")
                    else:
                        print("请输入寝室")
                else:
                    print("请输入性别")
            else:
                print("请输入正确的学号")
        else:
           print("请输入姓名")
        # a.add_student_information(addname,addstudy_num,addsex_num,addroom_num,addage_num)
    def btnPress3_Clicked(self):
        print("退出")
        self.close()
class second(QWidget):
    #打印各寝室人员列表
    def __init__(self, parent=None):
        super(second, self).__init__(parent)
        self.setWindowTitle("second")
        flo = QFormLayout()
        self.LineEdit = QLineEdit()
        self.LineEdit1 = QLineEdit()
        flo.addRow("姓名:", self.LineEdit)
        self.LineEdit.setPlaceholderText("请输入寝室号")
        self.LineEdit1 = QLineEdit()
        self.btnPress1 = QPushButton("查询")
        self.btnPress2 = QPushButton("退出")
        self.LineEdit1.setEnabled(False)
        flo.addWidget(self.LineEdit1)
        flo.addWidget(self.btnPress1)
        flo.addWidget(self.btnPress2)
        # layout = QVBoxLayout()
        self.setLayout(flo)
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)
    def btnPress1_Clicked(self):  
        b=my_system()   
        self.LineEdit1.setText(b.str_list_by_room(self.LineEdit.text()))


    def btnPress2_Clicked(self):
        self.close()

        
class third(QWidget):
    #用学号索引打印特定学生信息
    def __init__(self, parent=None):
        super(third, self).__init__(parent)
        self.setWindowTitle("third")
        flo = QFormLayout()
        self.flag=0b0
        self.setGeometry(500,300,250,150)
        self.LineEdit = QLineEdit()
        self.LineEdit1 = QLineEdit()

        self.chkBox1 = QCheckBox(self)
        self.chkBox1.setText("姓名")

        self.chkBox2 = QCheckBox(self)
        self.chkBox2.setText("性别")

        self.chkBox3 = QCheckBox(self)
        self.chkBox3.setText("年龄")
        self.chkBox3.move(80, 30)

        self.chkBox4 = QCheckBox(self)
        self.chkBox4.setText("寝室")
        self.chkBox4.move(80, 50)
        
        self.chkBox5 = QCheckBox(self)
        self.chkBox5.setText("全部")
        self.chkBox5.move(130, 30)

        self.chkBox1.stateChanged.connect(lambda: self.btnstate(self.chkBox1))
        self.chkBox2.stateChanged.connect(lambda: self.btnstate(self.chkBox2))
        self.chkBox3.stateChanged.connect(lambda: self.btnstate(self.chkBox3))
        self.chkBox4.stateChanged.connect(lambda: self.btnstate(self.chkBox4))
        self.chkBox5.stateChanged.connect(lambda: self.btnstate(self.chkBox5))

        self.LineEdit.setPlaceholderText("请输入学号")
        self.LineEdit1 = QLineEdit()
        self.btnPress1 = QPushButton("查询")
        self.btnPress2 = QPushButton("退出")
        
        flo.addWidget(self.LineEdit)
        flo.addWidget(self.chkBox1)
        flo.addWidget(self.chkBox2)
        # flo.addWidget(self.chkBox3)
        flo.addWidget(self.LineEdit1)
        flo.addWidget(self.btnPress1)
        flo.addWidget(self.btnPress2)
        self.LineEdit1.setEnabled(False)
        # layout = QVBoxLayout()
        self.setLayout(flo)
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)
    def btnPress1_Clicked(self):  
        a=my_system()   
        string=""
        if(self.LineEdit.text()) and (not a.judeg_study_num_is(self.LineEdit.text())):
            string=a.get_list_by_study_num(self.LineEdit.text())
            
            if self.flag & 0b00010000== 0b00010000:#全部
                self.LineEdit1.setText("姓名："+string["name"]+','+"性别:"+string["gender"]+','+"年龄:"+string["age"]+','+"寝室:"+string["room_num"])
                #"姓名："+string["name"]+','+"性别:"+string["gender"]+','+"年龄:"+string["age"]+"寝室:"+string["room_num"]
            else: 
                str1=""            
                if self.flag & 0b00000001== 0b00000001:#姓名
                    str1=str1+"姓名："+string["name"]+','
                if self.flag & 0b00000010== 0b00000010:#性别
                    str1=str1+"性别:"+string["gender"]+','
                if self.flag & 0b00000100== 0b00000100:#年龄
                    str1=str1+"年龄:"+string["age"]+','
                if self.flag & 0b00001000== 0b00001000:#寝室
                    str1=str1+"寝室:"+string["room_num"]
                self.LineEdit1.setText(str1)
                del str1
        else:
            self.LineEdit1.clear()
        del a
    def btnPress2_Clicked(self):
        self.close()
    def btnstate(self, btn):
        if btn==self.chkBox1:
            print("姓名")
            if self.chkBox1.isChecked() :
                self.flag=self.flag | 0b00000001
            else:
                self.flag=self.flag & 0b11111110
            print(self.flag)
        elif btn==self.chkBox2:
            print("性别")
            if self.chkBox2.isChecked() :
                self.flag=self.flag | 0b00000010
            else:
                self.flag=self.flag & 0b11111101
            print(self.flag)
        elif btn==self.chkBox3:
            print("年龄")
            if self.chkBox3.isChecked() :
                self.flag=self.flag | 0b00000100
            else:
                self.flag=self.flag & 0b11111011
            print(self.flag)
        elif btn==self.chkBox4:
            print("寝室")
            if self.chkBox4.isChecked() :
                self.flag=self.flag | 0b00001000
            else:
                self.flag=self.flag & 0b11110111
            print(self.flag)
        elif btn==self.chkBox5:
            print("全部")
            if self.chkBox5.isChecked() :
                self.flag=self.flag | 0b00010000
            else:
                self.flag=self.flag & 0b11101111
            print(self.flag)
 

class fourth(QWidget):
    #打印所有学生信息
    def __init__(self, parent=None):
        super(fourth, self).__init__(parent)
        self.setWindowTitle("fourth")
        self.setGeometry(500,300,550,200)
        a=my_system()
        data=a.get_all_student_information()
        i=0
        for key in data:
            i+=1
        print(i)
        # self.label=QLabel(self)
        # self.label.setText('学号：')
        # #标签1的背景填充更改为True，否则无法显示背景
        # self.label.setAutoFillBackground(True)
        flo = QFormLayout()
        self.tableWidget = QTableWidget(i,5)
        # self.tableWidget.setGeometry(QtCore.QRect(10, 130, 701, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(["学号","姓名","性别","寝室","年龄"])#表头标签默认从"1"开始，"1","2"...
        # self.tableWidget.horizontalHeader().hide()
        self.tableWidget.verticalHeader().setDisabled(True) #不让用户改行高
        self.tableWidget.horizontalHeader().setDisabled(True) #不让用户改列宽
        self.tableWidget.verticalHeader().hide()
        for num in range(0,i):
            self.tableWidget.setItem(num,0, QTableWidgetItem(data[num]["study_num"]))
            self.tableWidget.setItem(num,1, QTableWidgetItem(data[num]["name"]))
            self.tableWidget.setItem(num,2, QTableWidgetItem(data[num]["gender"]))
            self.tableWidget.setItem(num,3, QTableWidgetItem(data[num]["room_num"]))
            self.tableWidget.setItem(num,4, QTableWidgetItem(data[num]["age"]))
        
        self.tableWidget.sortItems(3,QtCore.Qt.AscendingOrder)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#默认
        # flo.addWidget(self.label)
        flo.addWidget(self.tableWidget)
        self.setLayout(flo)
    def btnPress_Clicked(self):
        print("退出")

class fifth(QWidget):
    #调整寝室
    def __init__(self, parent=None):
        super(fifth, self).__init__(parent)
        self.setWindowTitle("fifth")
        flo = QFormLayout()
        self.LineEdit = QLineEdit()
        self.LineEdit1 = QLineEdit()
        self.LineEdit2 = QLineEdit()
        self.flag=False
        flo.addRow("学号1:", self.LineEdit)
        self.LineEdit.setPlaceholderText("请输入学号")
        flo.addRow("学号2:", self.LineEdit1)
        self.LineEdit1.setPlaceholderText("请输入学号")
        flo.addRow("寝室:", self.LineEdit2)
        self.LineEdit2.setPlaceholderText("请输入寝室号")

        self.btnPress1 = QPushButton("调整寝室")
        self.btnPress2 = QPushButton("交换寝室")
        self.btnPress3 = QPushButton("确认")
        self.btnPress4 = QPushButton("退出")
        self.LineEdit1.setEnabled(False)

        flo.addWidget(self.btnPress1)
        flo.addWidget(self.btnPress2)
        flo.addWidget(self.btnPress3)
        flo.addWidget(self.btnPress4)
        # layout = QVBoxLayout()
        self.setLayout(flo)
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)
        self.btnPress3.clicked.connect(self.btnPress3_Clicked)
        self.btnPress4.clicked.connect(self.btnPress4_Clicked)
    def btnPress1_Clicked(self):
        print("调整寝室")
        self.flag=False
        self.LineEdit1.setEnabled(False)
        self.LineEdit2.setEnabled(True)
        self.LineEdit1.clear()
        

    def btnPress2_Clicked(self):
        print("交换寝室")
        self.flag=True
        self.LineEdit1.setEnabled(True)
        self.LineEdit2.setEnabled(False)
        self.LineEdit2.clear()
    def btnPress3_Clicked(self):
        print("确认")
        if not self.flag:
            a=my_system()
            if(self.LineEdit.text()) and (not a.judeg_study_num_is(self.LineEdit.text())):

                if(self.LineEdit2.text()):
                    a.change_room(self.LineEdit.text(),self.LineEdit2.text())
        else:
            a=my_system()
            if(self.LineEdit.text()) and (not a.judeg_study_num_is(self.LineEdit.text())):
                if(self.LineEdit1.text()):
                    a.exchange_room(self.LineEdit.text(),self.LineEdit1.text())
    def btnPress4_Clicked(self):
        print("退出")
        self.close()


if __name__ == "__main__":
    # a=my_system()
    # a.main()
    app = QApplication(sys.argv)
    win = third()
    win.show()
    sys.exit(app.exec_())
