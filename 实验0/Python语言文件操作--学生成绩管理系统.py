# -*- coding: UTF-8 -*-
# https://blog.csdn.net/tian_123456789/article/details/78914692

import os
import re
import numpy as np

class Student: #定义一个学生类
    def __init__(self):
        self.name = ''
        self.ID =''
        self.score1 = 0
        self.score2 = 0
        self.score3 = 0
        self.sum = 0


def searchByID(stulist, ID): #按学号查找看是否学号已经存在
    for item in stulist:
        if item.ID == ID:
            return True

def Add(stulist,stu): #添加一个学生信息
    if searchByID(stulist, stu.ID) == True:
        print("学号已经存在！")
        return False
    stulist.append(stu)
    print (stu.name,stu.ID, stu.score1, stu.score2, stu.score3, stu.sum)
    print ("是否要保存学生信息？")
    nChoose = input("Choose Y/N")
    if nChoose == 'Y' or nChoose == 'y':
        file_object = open("students.txt", "a")
        file_object.write(stu.ID)
        file_object.write(" ")
        file_object.write(stu.name)
        file_object.write(" ")
        file_object.write(str(stu.score1))
        file_object.write(" ")
        file_object.write(str(stu.score2))
        file_object.write(" ")
        file_object.write(str(stu.score3))
        file_object.write(" ")
        file_object.write(str(stu.sum))
        file_object.write("\n")
        file_object.close()
        print (u"保存成功！")

def Search(stulist, ID): #搜索一个学生信息
    print (u"学号   姓名    语文    数学    英语    总分")
    count = 0
    for item in stulist:
        if item.ID == ID:
            print (item.ID, '\t' ,item.name,'\t', item.score1,'\t',item.score2, '\t', item.score3, '\t',item.sum)
            break
        count = 0
    if count == len(stulist):
        print ("没有该学生学号！")

def Del(stulist, ID): #删除一个学生信息
    count = 0
    for item in stulist:
        if item.ID == ID:
            stulist.remove(item)
            print ("删除成功！")
            break
        count +=1
    # if count == len(stulist):
    #   print "没有该学生学号！"
    file_object = open("students.txt", "w")
    for stu in stulist:
        print (stu.ID, stu.name, stu.score1,stu.score2, stu.score3, stu.sum)
        file_object.write(stu.ID)
        file_object.write(" ")
        file_object.write(stu.name)
        file_object.write(" ")
        file_object.write(str(stu.score1))
        file_object.write(" ")
        file_object.write(str(stu.score2))
        file_object.write(" ")
        file_object.write(str(stu.score3))
        file_object.write(" ")
        file_object.write(str(stu.sum))
        file_object.write("\n")
        file_object.close()
    #   print "保存成功！"
    file_object.close()
def Change(stulist, ID):
    count = 0
    for item in stulist:
        if item.ID == ID:
            stulist.remove(item)
            file_object = open("students.txt", "w")
            for stu in stulist:
                #print li.ID, li.name, li.score
                file_object.write(stu.ID)
                file_object.write(" ")
                file_object.write(stu.name)
                file_object.write(" ")
                file_object.write(str(stu.score1))
                file_object.write(" ")
                file_object.write(str(stu.score2))
                file_object.write(" ")
                file_object.write(str(stu.score3))
                file_object.write(" ")
                file_object.write(str(stu.sum))
                file_object.write("\n")
            #   print "保存成功！"
            file_object.close()
            stu = Student()
            stu.name = input("请输入学生的姓名")
            while True:
                stu.ID = input("请输入学生的ID")
                p = re.compile('^[0-9]{3}$')
                if p.match(stu.ID):
                    break
                else:
                    print ("输入的有错误！")
            while True:
                stu.score1 = int(input("请输入学生语文成绩"))
                if stu.score1 <= 100 and stu.score1 > 0 :
                    break
                else:
                    print ("输入的学生成绩有错误！")
            while True:
                stu.score2 = int(input("请输入学生数学成绩"))
                if stu.score2 <= 100 and stu.score2 > 0 :
                    break
                else:
                    print ("输入的学生成绩有错误！")
            while True:
                stu.score3 = int(input("请输入学生英语成绩"))
                if stu.score3 <= 100 and stu.score3 > 0 :
                    break
                else:
                    print ("输入的学生成绩有错误！")
            stu.sum = stu.score1 + stu.score2 + stu.score3
            Add(stulist,stu)
def display(stulist): #显示所有学生信息
    print (u"学号   姓名    语文    数学    英语    总分")
    for item in stulist:
        print (item.ID, '\t' ,item.name,'\t', item.score1,'\t',item.score2, '\t', item.score3, '\t',item.sum)

def Sort(stulist): #按学生成绩排序
    Stu = []
    sum_count = []
    for li in stulist:
        temp = []
        temp.append(li.ID)
        temp.append(li.name)
        temp.append(int(li.score1))
        temp.append(int(li.score2))
        temp.append(int(li.score3))
        temp.append(int(li.sum))
        sum_count.append(int(li.sum))
        Stu.append(temp)

    #print sum_count
    #print Stu;
    #print stulist
    insertSort(sum_count, stulist)
    #print stulist;
    display(stulist)

def insertSort(a, stulist):
    for i in range(len(a)-1):
        #print a,i
        for j in range(i+1,len(a)):
            if a[i]<a[j]:
                temp = stulist[i]
                stulist[i] = stulist[j]
                stulist[j] = temp
    #return a

def Init(stulist):  #初始化函数
    print ("初始化......")
    file_object = open('students.txt', 'r')
    for line in file_object:
        stu = Student()
        line = line.strip("\n")
        s = line.split(" ")
        stu.ID = s[0]
        stu.name = s[1]
        stu.score1 = s[2]
        stu.score2 = s[3]
        stu.score3 = s[4]
        stu.sum = s[5]
        stulist.append(stu)
    file_object.close()
    print ("初始化成功！")
    main()

def main(): #主函数 该程序的入口函数
    while True:
        print ("*********************")
        print (u"--------菜单---------")
        print (u"增加学生信息--------1")
        print (u"查找学生信息--------2")
        print (u"删除学生信息--------3")
        print (u"修改学生信息--------4")
        print (u"所有学生信息--------5")
        print (u"按照分数排序--------6")
        print (u"退出程序------------0")
        print ("*********************")

        nChoose = input("请输入你的选择：")
        if nChoose == "1":
            stu = Student()
            stu.name = input("请输入学生的姓名")
            while True:
                stu.ID = input("请输入学生的ID")
                p = re.compile('^[0-9]{3}$')
                if p.match(stu.ID):
                    break
                else:
                    print ("输入的有错误！")
            while True:
                stu.score1 = int(input("请输入学生语文成绩"))
                if stu.score1 <= 100 and stu.score1 > 0 :
                    break
                else:
                    print ("输入的学生成绩有错误！")
            while True:
                stu.score2 = int(input("请输入学生数学成绩"))
                if stu.score2 <= 100 and stu.score2 > 0 :
                    break
                else:
                    print ("输入的学生成绩有错误！")
            while True:
                stu.score3 = int(input("请输入学生英语成绩"))
                if stu.score3 <= 100 and stu.score3 > 0 :
                    break
                else:
                    print ("输入的学生成绩有错误！")
            stu.sum = stu.score1 + stu.score2 + stu.score3
            Add(stulist,stu)

        if nChoose == '2':
            ID = input("请输入学生的ID")
            Search(stulist, ID)

        if nChoose == '3':
            ID = input("请输入学生的ID")
            Del(stulist, ID)
        if nChoose == '4':
            ID = input("请输入学生的ID")
            Change(stulist, ID)

        if nChoose == '5':
            display(stulist)

        if nChoose == '6':
            Sort(stulist)


        if nChoose == '0':
            break

if __name__ == '__main__':
    stulist =[]
Init(stulist)