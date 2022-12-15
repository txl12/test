# -*- coding: UTF-8 -*-
import json
class my_system:
    def change_room(self,study_num,room_num):

        #调整一个学生的寝室
        if room_num[0]=='1'and len(room_num)==3 :#男
            if self.judge_room_isfull(room_num):
                with open('test.json',encoding='utf-8') as f:
                    data = json.load(f)
                for key in data:
                    if key["study_num"] == study_num:
                        if key["gender"]=="男":
                            key.update({'room_num': room_num})
                            f.close()
                            f = open('test.json','w',encoding='utf-8')
                            f.write(json.dumps(data))
                            f.close()
                        else:
                            print("该学生是女生，不能调寝到男寝")
            else :
                print("目的寝室已经满员，请选择其他寝室")
        elif room_num[0]=='2'and len(room_num)==3 :#女
            if self.judge_room_isfull(room_num):
                with open('test.json',encoding='utf-8') as f:
                    data = json.load(f)
                for key in data:
                    if key["study_num"] == study_num:
                        if key["gender"]=="女":
                            key.update({'room_num': room_num})
                            f.close()
                            f = open('test.json','w',encoding='utf-8')
                            f.write(json.dumps(data))
                            f.close()
                        else:
                            print("该学生是男生，不能调寝到女寝")         
            else :
                print("目的寝室已经满员，请选择其他寝室")
        else:
            print("错误的寝室号")
    def exchange_room(self,study_num1,study_num2):
        #交换两个学生的寝室
        num=0
        with open('test.json',encoding='utf-8') as f:
            data = json.load(f)
        for key in data:
            # for key1 in data: 
            if key["study_num"] == study_num1:
                sex1=key["gender"]
                a=key["room_num"]
                num1=num
            elif key["study_num"] == study_num2:
                sex2=key["gender"]
                b=key["room_num"]
                num2=num
            num+=1
        if sex1==sex2:
            data[num1].update({'room_num':b})
            data[num2].update({'room_num': a})
            f.close()
            f = open('test.json','w',encoding='utf-8')
            f.write(json.dumps(data))
            f.close()
        else:
            print("性别不同不能调寝室！！！")
            f.close()
        
    def judge_room_isfull(self,room_num):
        #判断寝室满人
        with open('test.json',encoding='utf-8') as f:
            data = json.load(f)
        num=0
        for key in data:
            # for key1 in data:
            if key["room_num"] == room_num:
                num+=1
        if num<4 :
            print("当前寝室为"+room_num+"且未满，寝室人数为："+str(num))
            f.close()
            return True
        else:
            print("当前寝室为"+room_num+"且已满，不可入住")
            f.close()
            return False  
    def manually_room(self,room_num,gender):
        # 手动分配寝室
        if gender=="男":
            if int(room_num)>=100 and int(room_num)<200:
                return self.judge_room_isfull(room_num) 
            else :
                return False
        elif gender =="女":
            if int(room_num)>=200 and int(room_num)<300:
                return self.judge_room_isfull(room_num)   
            else:
                return False  
    def auto_room(self,gender):
        # 自动分配寝室
        room=""
        with open('test.json',encoding='utf-8') as f:
            data = json.load(f)
        if gender=="男":
            for key in data:
                # 先找未满的寝室
                room=room+ key["room_num"]+','
                if self.judge_room_isfull(key["room_num"])and(int(key["room_num"])>=100 and int(key["room_num"])<200):
                    f.close()
                    return key["room_num"]
            #寝室全部满员，创建新寝室
            print(room)
            for num in range(100,200):
                if str(num)in room:
                    continue
                else:
                    print(num)
                    return(str(num))
        if gender=="女":
            for key in data:
                # 先找未满的寝室
                room=room+ key["room_num"]+','
                if self.judge_room_isfull(key["room_num"])and(int(key["room_num"])>=200 and int(key["room_num"])<300):
                    f.close()
                    return key["room_num"]
            #寝室全部满员，创建新寝室
            print(room)
            for num in range(200,300):
                if str(num)in room:
                    continue
                else:
                    print(num)
                    return(str(num))
        
    def print_list_by_study_num(self,study_num,information):
        #通过学号打印信息
        with open('test.json',encoding='utf-8') as f:
            data = json.load(f)
        for key in data:
            # for key1 in data:
            if key["study_num"] == study_num:
                if information=="name" :
                    print("学号："+study_num+"的姓名："+key["name"])
                elif information=="gender" :
                    print("学号："+study_num+"的性别："+key["gender"])
                elif information=="room_num" :
                    print("学号："+study_num+"的寝室："+key["room_num"])
                elif information=="age" :
                    print("学号："+study_num+"的年龄："+key["age"])
                elif information=="all" :
                    print("姓名:"+key["name"]+" 学号:"+key["study_num"]+" 寝室:"+key["room_num"]+" 性别:"+key["gender"]+" 年龄:"+key["age"])
                else:
                    print("输入错误的参数！")
        f.close()
    def get_list_by_study_num(self,study_num):
        #通过学号打印信息
        with open('test.json',encoding='utf-8') as f:
            data = json.load(f)
        for key in data:
            # for key1 in data:
            if key["study_num"] == study_num:
                f.close()
                return key
        # return False
    def print_all_student_information(self):
        #打印全部信息
        with open('test.json',encoding='utf-8') as f:
            data = json.load(f)
        for key in data:
            print("姓名:"+key["name"]+" 学号:"+key["study_num"]+" 寝室:"+key["room_num"]+" 性别:"+key["gender"]+" 年龄:"+key["age"])
        f.close()
    def get_all_student_information(self):
        #打印全部信息
        with open('test.json',encoding='utf-8') as f:
            data = json.load(f)
        f.close()
        return data
        
    def judeg_study_num_is(self,study_num):
        with open('test.json',encoding='utf-8') as f:
            data = json.load(f)
        for key in data:
            if key["study_num"] == study_num:
                # print("该学号已有信息，请确认是否输入正确")
                f.close()
                return False
        f.close()
        return True
    def add_student_information(self,name,study_num,gender,room_num,age):
        #往JSON文件添加学生
        data={
        "name":name,
        "study_num":study_num,
        "gender":gender,
        "room_num":room_num,
        "age":age
    }   
        if ((gender=="女" and (room_num[0]=="2" and len(room_num)==3)))or ((gender=="男" and (room_num[0]=="1" and len(room_num)==3))):
            if self.judeg_study_num_is(study_num):
                f = open('test.json','r',encoding='utf-8')
                a=f.read()
                f.close()
                f = open('test.json','w',encoding='utf-8')
                f.write('['+a[1:-1]+','+ '{'+'"'+"name"+'"'+ ':'+'"'+data["name"]+'"'+','+'"'+"study_num"+'"'+ ':'+'"'+data["study_num"]+'"'+','+'"'+"gender"+'"'+ ':'+'"'+data["gender"]+'"'+','+'"'+"room_num"+'"'+ ':'+'"'+data["room_num"]+'"'+','+'"'+"age"+'"'+ ':'+'"'+data["age"]+'"'+'}'+']')
                f.close()
                # with open("test.json", "w", encoding='utf-8') as file:
                #     json.dump(data, file, ensure_ascii=False)  # 传入文件描述符，和dumps一样的结果，关闭默认以ASCII码存入json
                print(data)
        else:
            print("请检查信息是否有误！！！")
    def print_list_by_room(self,room_num):
        with open('test.json',encoding='utf-8') as f:
            data = json.load(f)
        print(room_num+"寝室人员：")#打印寝室的学生信息
        for key in data:
            # for key1 in data:
            if key["room_num"] == room_num:
                print(key["name"])
        f.close()
    def str_list_by_room(self,room_num):
        with open('test.json',encoding='utf-8') as f:
            data = json.load(f)
        string=""
        for key in data:
            # for key1 in data:
            if key["room_num"] == room_num:
                string=string+key["name"]+' '
        f.close()
        return string
    def main(self):
        while True:
            print("==================================")
            print("||1:录入学生信息                 ||")
            print("||2:打印各寝室人员列表           ||")
            print("||3:用学号索引打印特定学生信息   ||")
            print("||4:打印所有学生信息             ||")
            print("||5:调整寝室                     ||")
            print("||6:退出程序                     ||")
            print("==================================")
            print("请输入命令：")
            a=input()
            if a<='6' and a>'0':
                if a =='6':
                    print("||6:退出程序                     ||")
                    break
                if a=='1':
                    print("||1:录入学生信息                 ||")
                    print("请输入姓名：")
                    addname=input()
                    print("请输入学号：")
                    addstudy_num=input()
                    while self.judeg_study_num_is(addstudy_num)==False:
                        print("该学号已有信息，请确认是否输入正确")
                        print("请重新输入学号：")
                        addstudy_num=input()
                    print("请输入性别：")
                    addsex_num=input()
                    while not(addsex_num=="男"or addsex_num=="女"):
                        print("请重新输入性别：")
                        addsex_num=input()
                    print("请输入年龄：")
                    addage_num=input()
                    print("自动分配请输入auto,手动分配输入寝室号")
                    while True:
                        addroom_num=input()
                        if addroom_num=="auto":
                            addroom_num=self.auto_room(addsex_num)
                            break
                        else:
                            if self.manually_room(addroom_num,addsex_num):
                                break
                            else:
                                print("分配失败，请重新分配！")
                    self.add_student_information(addname,addstudy_num,addsex_num,addroom_num,addage_num)
                elif a=='2':
                    print("||2:打印各寝室人员列表           ||")
                    print("请输入寝室号：")
                    print_room_num=input()
                    if int(print_room_num)>=100 and int(print_room_num)<300:
                        self.print_list_by_room(print_room_num)
                    else:
                        print("寝室号输入错误")
                elif a=='3':
                    print("||3:用学号索引打印特定学生信息   ||")
                    print("请输入学号：")
                    print_stu_num=input()
                    print("||1:姓名         ||")
                    print("||2:寝室         ||")
                    print("||3:性别         ||")
                    print("||4:年龄         ||")
                    print("||5:全部信息     ||")
                    print("请输入想打印的信息：")
                    print_choice_num=input()
                    if print_choice_num =='1':
                        self.print_list_by_study_num(print_stu_num,"name")
                    elif print_choice_num =='2':
                        self.print_list_by_study_num(print_stu_num,"room_num")
                    elif print_choice_num =='3':
                        self.print_list_by_study_num(print_stu_num,"gender")
                    elif print_choice_num =='4':
                        self.print_list_by_study_num(print_stu_num,"age")
                    elif print_choice_num =='5':
                        self.print_list_by_study_num(print_stu_num,"all")
                elif a=='4':
                    print("||4:打印所有学生信息             ||")
                    self.print_all_student_information()
                else:
                    print("||1:调整寝室         ||")
                    print("||2:交换寝室         ||")
                    print("请输入调整寝室的方法：")
                    cmd=input()
                    if cmd =='1':
                        print("请输入学号：")
                        stu_num=input()
                        print("请输入寝室号：")
                        room_num_change=input()
                        self.change_room(self,stu_num,room_num_change)
                    elif cmd =='2':
                        print("请输入学生1学号：")
                        stu_num1=input()
                        print("请输入学生2学号：")
                        stu_num2=input()
                        self.exchange_room(stu_num1,stu_num2)

            else:
                print("错误的命令，请重新输入")
if __name__ == '__main__':
    a=my_system
    a.main(a)
