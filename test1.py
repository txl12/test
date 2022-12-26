# -*- coding: UTF-8 -*-
import json
class my_system1:
    def __init__(self):#初始化自动载入JSON文件，私有列表记录信息方便查找各个KEY值
            with open('information.json',encoding='utf-8') as f:
                self.data = json.load(f)#with语句自动调用close方法
            self.__roomnum=[]
            self.__stunum=[]
            self.__age=[]
            self.__sex=[]
            self.__name=[]
            for key in self.data:
                self.__roomnum.append(key["information"]["room_num"]) 
                self.__stunum.append(key["study_num"])
                self.__age.append(key["information"]["age"])
                self.__sex.append(key["information"]["gender"])
                self.__name.append(key["information"]["name"])
    def judgeroom(self,room_num,gender="男",judgeroom_full=False,judgesex=False,judgeroom_notnone=False):#判断房间范围，性别，是否为空等，不同功能由三个bool变量决定
        if room_num.isnumeric() and (int(room_num) in range(100,300)) :
            if (gender =="男" or gender=="女"):
                if (int(room_num) in range(100,200) and (gender =="男" or (not judgesex)))or(int (room_num)in range(200,300) and (gender =="女"or (not judgesex))):
                    if judgeroom_full ^ judgeroom_notnone:
                        num=self.__roomnum.count(room_num)
                        if (num==4 and judgeroom_full)or (num==0 and judgeroom_notnone):#0，judgeroom_notnone false   1，2，3，  4 judgeroom_full false
                            return False
                        else:
                            return True
                    else:
                        return True
                print(gender+"生寝室"+"寝室不应该是"+room_num)
            else:
                print("请输入正确性别")
        else:
            print("错误的寝室号:"+ room_num)
        return False
    def print_all_student_information(self):
        for key in self.data:#从全局变量遍历全部信息
            print("姓名:"+key["information"]["name"]+" 学号:"+key["study_num"]+" 寝室:"+key["information"]["room_num"]+" 性别:"+key["information"]["gender"]+" 年龄:"+key["information"]["age"])
    def getstudent(self,study_num):#返回self.__stunum列表里的学号偏移量，不在列表里，抛出异常，调用时使用try,except捕获异常
        return self.__stunum.index(study_num)
    def exchange_room(self,study_num1,study_num2):#交换两个学生的寝室
        if (study_num1 in self.__stunum)and (study_num2 in self.__stunum):
            try :
                stu1=self.getstudent(study_num1)
                stu2=self.getstudent(study_num2)
                if (self.data[stu1]["information"]["gender"]==self.data[stu2]["information"]["gender"]):
                    room=self.data[stu1]["information"]["room_num"]
                    self.data[stu1]["information"].update({'room_num': self.data[stu2]["information"]["room_num"]})
                    self.data[stu2]["information"].update({'room_num':room })
                    room=self.__roomnum[stu1]
                    self.__roomnum[stu1]=self.__roomnum[stu1]
                    self.__roomnum[stu1]=room#全局变量更新后，私有变量也得更新，保证索引值正确
                    return True
                else:
                    print("性别不同不能调寝室！！！")
            except:
                pass
        else:
            print("未找到这两个学生:"+study_num1 +","+study_num2)
        return False
    def change_room(self,study_num,room_num):#调整一个学生的寝室
        if  study_num in self.__stunum:
            try:
                key=self.getstudent(study_num)
                if self.judgeroom(room_num,self.data[key]["information"]["gender"],judgeroom_full=True,judgesex=True):#可以交换
                    self.data[key]["information"].update({'room_num':room_num})
                    self.__roomnum[key]=room_num#全局变量更新后，私有变量也得更新，保证索引值正确
                    return True
            except:
                pass
        else:
            print("错误的学号:"+study_num)
        return False
    def print_stu(self,study_num,information):#通过不同命令打印不同信息
        index=self.getstudent(study_num)
        string=""
        if "姓名" in information or "全部信息" in information:
            string="姓名:"+self.__name[index]
        if "寝室" in information or "全部信息" in information:
            string=string +" 寝室:"+self.__roomnum[index]
        if "性别" in information or "全部信息" in information:
            string=string +" 性别:"+self.__sex[index]
        if "年龄" in information or "全部信息" in information:
            string=string +" 年龄:"+self.__age[index]
        if string:
            print(string)
        else:
            print("要打印的信息输入错误："+information)
    def findbyroom(self,room_num):#通过寝室号打印寝室成员
        if  room_num in self.__roomnum :#不在寝室列表返回false
            print("寝室%s成员:"%room_num)
            for key in self.data:
                if key["information"]["room_num"]==room_num:
                    print(key["information"]["name"])
            return True
        return False
    def distribute_room(self,cmd,gender):#根据命令分配寝室
        if gender=="男":
            range1=range(100,200)
        elif gender=="女":
            range1=range(200,300)
        else:
            return False
        if cmd =="auto":
            for x in range1:
                if self.judgeroom(str(x),gender=gender,judgeroom_full=True,judgesex=True):
                    return str(x)
        elif cmd.isnumeric() and( int(cmd) in range1 )and self.judgeroom(cmd,gender=gender,judgeroom_full=True,judgesex=True):
            return cmd
        else:
            return False
    def add_stu(self,study_num,gender,room_num,name,age):#更新全局变量和私有变量
        self.__roomnum.append(room_num) 
        self.__stunum.append(study_num)
        self.__age.append(age)
        self.__sex.append(gender)
        self.__name.append(name)
        newstu={
            "study_num": study_num,
            "information": {
            "name": name,
            "gender":gender,
            "room_num": room_num,
            "age": age}}
        self.data.append(newstu)
    def save_json(self):#保存文件
        try:
            with open('information.json', 'w',encoding='utf-8') as f_new:
                json.dump(self.data, f_new,ensure_ascii=False)
        except:
            print("打开文件失败")#with语句自动调用close方法
def main():
    a=my_system1()
    while True:
        print("==================================")
        print("||1:录入学生信息                 ||")
        print("||2:打印各寝室人员列表           ||")
        print("||3:用学号索引打印特定学生信息   ||")
        print("||4:打印所有学生信息             ||")
        print("||5:调整寝室                     ||")
        print("||6:保存并退出程序               ||")
        print("==================================")
        cmd=input("请输入命令：")
        if cmd =="1":
            print("||1:录入学生信息                 ||")
            addname=input("请输入姓名：")
            while True: 
                addstudy_num=input("请输入学号：")
                try:
                    a.getstudent(addstudy_num)
                    print("该学号已经有学生了,请确认学号是否正确")
                except:
                    if addstudy_num.isnumeric():
                        break
                    print("请输入正确的学号")
            while True: 
                addsex_num=input("请输入性别：(男|女)")
                if addsex_num=="男" or addsex_num=="女":
                    break
                else:
                    print("请输入正确的性别")
            while True: 
                addage_num=input("请输入年龄：(如:18)")
                if addage_num.isnumeric():
                        break
                else :
                    print("格式错误！！!")
            while True: 
                addroom_num=a.distribute_room(input("自动分配请输入auto,手动分配输入寝室号"),addsex_num)
                if addroom_num:
                    print("分配寝室成功,寝室号为%s"%addroom_num)
                    break
                else:
                    print("错误的寝室号，请重新输入")
            a.add_stu(addstudy_num,addsex_num,addroom_num,addname,addage_num)
        elif cmd=="2":
            print("||2:打印各寝室人员列表           ||")
            room_num=input("请输入寝室号：")
            if not a.findbyroom(room_num):
                print("错误的寝室号"+room_num)
        elif cmd=="3":
            print("||3:用学号索引打印特定学生信息   ||")
            while True: 
                print_stu_num=input("请输入学号：")
                try:
                    a.getstudent(print_stu_num)
                    print("||姓名         ||")
                    print("||寝室         ||")
                    print("||性别         ||")
                    print("||年龄         ||")
                    print("||全部信息     ||")
                    print_choice_num=input("请输入想打印的信息：")
                    a.print_stu(print_stu_num,print_choice_num)
                    break
                except:
                    print("该学号%s没有信息,请输入正确的学号"%print_stu_num)
        elif cmd=="4":
            print("||4:打印所有学生信息             ||")
            a.print_all_student_information()
        elif cmd=="5":
            print("||1:调整寝室         ||")
            print("||2:交换寝室         ||")
            method=input("请输入调整寝室的方法：")
            if method =='1':
                stu_num=input("请输入学号：")
                room_num_change=input("请输入寝室号：")
                if a.change_room(stu_num,room_num_change):
                    print("调整寝室成功")
                else:
                    print("调整寝室失败")
            elif method =='2':
                stu_num1=input("请输入学生1学号:")
                stu_num2=input("请输入学生2学号:")
                if a.exchange_room(stu_num1,stu_num2):
                    print("交换寝室成功")
                else:
                    print("交换寝室失败")
            else:
                print("错误的命令："+method)
        elif cmd=="6":
            print("||6:保存并退出程序               ||")
            a.save_json()
            break
        else:
            print("错误的命令，请重新输入")
if __name__ == '__main__':
    main()
    

