import math
class Shape:
    def __init__(self,color):
        self.color = color
    def area(self):
        return 0
    def __str__(self):
        return f'color is {self.color}'

class Circle(Shape):
    def __init__(self,color,r):
        super().__init__(color)
        self.r = r
    def area(self):
        return self.r**2*math.pi
class Retangle(Shape):
    def __init__(self,color,a,b):
        # super().__init__(color)
        self.color = color
        self.a = a
        self.b = b
    def area(self):
        return self.a*self.b/2
s = Shape('red')
c1 = Circle('green',13)
r = Retangle('green',13,22)
print(r.area())