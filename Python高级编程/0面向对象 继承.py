class A:
    def __init__(self):
        print('init A')
    def hahaha(self):
        print(' A')

class B(A):
    def __init__(self):
        print('init B')
    def hahaha(self):
        super().hahaha()
        #super(B,self).hahaha()
        # A.hahaha(self)
        print('B')

# a = A()
b = B()
b.hahaha()
# super(B,b).hahaha()

