class Typed:
    def __init__(self, key, expected_type):  # 构造函数接收所传入的参数和参数类型
        self.key = key
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        print('get方法')
        return instance.__dict__[self.key]  # 从底层字典获取值

    def __set__(self, instance, value):
        print('set方法')
        if not isinstance(value, self.expected_type):  # 类型判断
            raise TypeError('%s 传入的类型不是%s' % (self.key, self.expected_type)) # 格式化抛出异常
        instance.__dict__[self.key] = value # 修改底层字典

    def __delete__(self, instance):
        print('delete方法')
        instance.__dict__.pop(self.key)


class People:
    name = Typed('name', str)  # p1.__set__()  self.__set__()，触发描述符__set__方法，设置参数类型传给构造函数
    age = Typed('age', int)  # p1.__set__()  self.__set__()
    salary = Typed('salary', float)  # p1.__set__()  self.__set__()
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

# p1=People('alex','13',13.3)#类型有误，报错
p1 = People('alex', 13, 13.3)
print(p1.__dict__)
print(p1.name)
p1.name = 'egon'
print(p1.__dict__)
del p1.name
print(p1.__dict__)
# print(p1.name)  # 相应的键值对已在底层字典中删除了，报错