class Cat:
    """这是一个猫类"""
    def eat(self):
        print(f"小猫爱吃鱼,我是{self.name},self的地址是{id(self)}")
    def drink(self):
        print("小猫在喝水")

tom = Cat()
print(f'tom对象的id是{id(tom)}')
tom.name = "Tom"
tom.eat()
print('-'*60)
lazy_cat = Cat()
print(f'lazy_cat对象的id是{id(lazy_cat)}')
lazy_cat.name = "大懒猫"
lazy_cat.eat()

class Cat:
    def __init__(self, name):
        print("初始化方法 %s" % name)
        self.name = name

tom = Cat("Tom")
lazy_cat = Cat("大懒猫")


# _str_ 方法，如果在开发中，希望使用 print 输出 对象变量 时，能够打印 自定义的内容，就可以利用 __str__ 这个内置方法了

class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print("%s 来了" % self.name)


    def __str__(self):
        return "我是小猫：%s" % self.name

tom = Cat("Tom")
print(tom)
