# 在开发中，如果希望在 创建对象的同时，就设置对象的属性，可以对 __init__ 方法进行 改造
class Cat:
    def __init__(self,name):
        self.name = 'Tom'
        print('init')
    def __str__(self):
        return(self.name)
    def drink(self):
        print('drink')
cat = Cat('Tom')
print(f'我是小猫{cat},我的id是{id(cat)}',cat,cat.name)
cat.drink()
