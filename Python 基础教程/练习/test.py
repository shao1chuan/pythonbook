class Student:
    def __init__(self,name,experence,deligent,smart,isEnter):
        self.name = name
        self.experence = experence
        self.deligent = deligent
        self.smart = smart
        self.isEnter = isEnter

class Class:
    def __init__(self,date):
        self.stulist = []
        self.date = date
    def add(self,student:Student):
        self.stulist.append(student)

class Course:
    def __init__(self,name,hour):
        self.name = name
        self.hour = hour

class Company:
    def __init__(self):
        classlist = []
