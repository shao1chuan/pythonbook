# https://www.cnblogs.com/wozijisun/p/16635365.html

def singleton(cls):
    _instance_dict = {}  # 采用字典，可以装饰多个类，控制多个类实现单例模式

    def inner(*args, **kwargs):
        if cls not in _instance_dict:
            _instance_dict[cls] = cls(*args, **kwargs)
        return _instance_dict.get(cls)

    return inner
@singleton
class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age
@singleton
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get(self):
        t1 = Teacher("aa",52)
        return t1


    # def __new__(cls, *args, **kwargs):   # 将方法3的这部分代码搬到了函数装饰器中
    #   if not cls._instance:
    #     cls._instance = super().__new__(cls)
    #   return cls._instan


stu1 = Student('bb', 18)
stu2 = Student('jack', 18)
stu3 = Student('aaa', 19)
print(stu1 is stu3)
print(stu1.__dict__, stu3.__dict__)

t1 = Student('bb', 18).get()
t2 = Student('bb', 18).get()
print(t1 is t2)