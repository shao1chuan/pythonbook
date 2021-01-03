class Person():
    hight = 13
    def __init__(self,age,sex,hight):
        self.age = age
        self.sex = sex
        # self.hight = hight
    def display(self):
        print(f"person is displaying :{self.sex},{self.age},{self.hight},{Person.hight}")

p1 = Person(12,'girl',14)
p1.display()
print(f"person1 is run :{p1.sex},{p1.age},{p1.hight},{Person.hight}")
