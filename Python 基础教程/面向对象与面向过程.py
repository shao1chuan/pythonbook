
def CarInfo(type,price):
    print ("the car's type %s,price:%d"%(type,price))

print('函数方式（面向过程）')
CarInfo('passat',250000)
CarInfo('ford',280000)


class Car:
    def __init__(self,type,price):
        self.type = type
        self.price = price

    def printCarInfo(self):
        print ("the car's Info in class:type %s,price:%d"%(self.type,self.price))
print('面向对象')
carOne = Car('passat',250000)
carTwo = Car('ford',250000)
carOne.printCarInfo()
carTwo.printCarInfo()