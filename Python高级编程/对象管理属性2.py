class Person(object):
    name = 'python'
    age = 18

    def __init__(self):
        self.sex = 'boy'
        self.like = 'papapa'

    @staticmethod
    def stat_func():
        print ('this is stat_func')

    @classmethod
    def class_func(cls):
        print ('class_func')

class Hero(Person):
    name = 'super man'
    age = 1000

    def __init__(self):
        super(Hero, self).__init__()
        self.is_good = 'yes'
        self.power = 'fly'

person = Person()
print ('Person.__dict__: ', Person.__dict__)
print ('person.__dict__: ', person.__dict__)
# person.age = 22
person.aaa = 22
person.sex = 'girl'
print ('person.__dict__: ', person.__dict__)

hero = Hero()
print ('Hero.__dict__: ', Hero.__dict__ )
print ('hero.__dict__: ', hero.__dict__)

 # 类的普通方法、类方法、静态方法、全局变量以及一些内置的属性都是放在类对象dict里,而实例对象中存储了一些self.xxx的一些东西
# 类对象的dict虽然没有继承父类的，但是实例对象继承了父类的实例属性