class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def getAge(self):
        return self.__age
    def setAge(self,age):
        self.__age = age
p = Person('aa',23)
print(p.name,p.getAge())