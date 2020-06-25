class Student(object):
    def __new__(cls,*args,**kwargs):
        print('我是new函数！')   #这是为了追踪new的执行过程
        print(type(cls))        #这是为了追踪new的执行过程
        return object.__new__(cls)  #调用父类的（object）的new方法，返回一个Student实例，这个实例传递给init的self参数

    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('我是init')

    def study(self):
        print('我爱学习！')

if __name__=='__main__':
    s=Student('张三',25)
    print(s.name)
    print(s.age)
    s.study()