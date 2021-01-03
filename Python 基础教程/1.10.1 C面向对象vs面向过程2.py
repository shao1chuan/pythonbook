def carI(type,price):
    print(f"the type is: {type} and the price is: {price} ")
carI('aaa',12)

def drive(now,drive):
    print(f"you drive {now+drive} miles")
drive(12,23)


class carI():
    def __init__(self,type,price):
        self.type = type
        self.price = price
        self.dis = 0
    def drive(self,dis):
        self.dis +=dis
    def showprice(self):
        self.price = self.price -self.dis*10
        return self.price

a = carI('aa',12000)
print(a.showprice())

a.drive(100)
print(a.showprice())