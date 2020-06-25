class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    #定义对私有属性的get方法，获取私有属性
    def getAge(self):
        return self.__age

    #定义对私有属性的重新赋值的set方法，重置私有属性
    def setAge(self,age):
        self.__age = age

person1 = Person("tom",19)
person1.setAge(20)
print(person1.name,person1.getAge())  #tom 20