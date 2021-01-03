# 类对象所拥有的方法，需要用修饰器@classmethod来标识其为类方法，
# 对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数
# （当然可以用其他名称的变量作为其第一个参数，但是大部分人都习惯以'cls'作为第一个参数的名字），
# 能够通过实例对象和类对象去访问。

class people:
    country="china"

    @classmethod
    def getCountry(cls):
        return cls.country
    @classmethod
    def setCountry(cls,country):
        cls.country=country


p=people()
print(p.getCountry())   #实例对象调用类方法
print(people.getCountry())  #类对象调用类方法

p.setCountry("Japan")

print(p.getCountry())
print(people.getCountry())

# 需要通过修饰器@staticmethod来进行修饰，静态方法不需要定义参数
class people3:
    country="china"

    @staticmethod
    def getCountry():
        return people3.country

p=people3()
print(p.getCountry())   #实例对象调用类方法
print(people3.getCountry())  #类对象调用类方法