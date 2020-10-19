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

