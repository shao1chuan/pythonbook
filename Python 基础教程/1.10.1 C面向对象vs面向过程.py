# 面向对象的实现方式封装性更好，已经行驶的公里数是对象内部的属性，对象自身负责管理，外部调用代码无需管理。我们随时可以调用对象的方法和属性得知对象当前的各种信息。而面向过程的方式而言，外部调用代码会“手忙脚乱”
def car(type,price):
    print(f'car的价格是 {price}, 类型是{type}')
car(12,'qqq')

class Car:
    def __init__(self,type,price):
        self.type = type
        self.price = price
        self.distance = 0
    def carinfo(self):
        print(f'car的价格是 {self.price}, 类型是{self.type},行驶了{self.distance}')
    def drive(self,distance):
        self.distance +=distance
        self.price -= 10*distance
car1 = Car('aa',2000)
car1.carinfo()
car1.drive(20)
car1.carinfo()

