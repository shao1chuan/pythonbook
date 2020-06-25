class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()  # Call parent spam()

class C:
    def __init__(self):
        self.x = 0

class D(C):
    def __init__(self):
        super().__init__()
        self.y = 1
d = D()
print(d.y)

class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')