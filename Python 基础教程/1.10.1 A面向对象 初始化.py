# 类是抽象的概念，仅仅是模板。 比如说：“人”， 类定义了人这种类型属性（name，age...）和方法(study,work...)。
# 对象是一个你能够看得到、摸得着的具体实体： 赵本山，刘德华，赵丽颖，这些具体的人都具有人类型中定义的属性和方法，不同的是他们各自的属性不同。
# 根据类来创建对象被称为实例化。

# 语法格式
# class 类名:
#
#     def 方法1(self, 参数列表):
#         pass
#
#     def 方法2(self, 参数列表):
#         pass
class Cat:
    name = 'lili'
    def __init__(self):
        self.name = 'Tom'
        print('init')
    def __str__(self):
        return(self.name)
    def drink(self):
        print('drink')
cat = Cat()
# cat.name = 'Jack'
print(f'我是小猫{cat},我的id是{id(cat)}',cat,cat.name)
cat.drink()
