class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        print("init")

    def __call__(self, friend):
        print ('My name is %s...' % self.name)
        print ('My friend is %s...' % friend)

p = Person('Bob', 'male')
p('Tim')

class Fib(object):
    def __init__(self):
        pass
    def __call__(self,num):
        a,b = 0,1;
        self.l=[]

        for i in range (num):
            self.l.append(a)
            a,b= b,a+b
        return self.l
    def __str__(self):
        return str(self.l)


f = Fib()
print(f(10))