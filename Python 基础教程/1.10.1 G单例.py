# 也就是说，先创建一个实例对象，之后不管创建多少个，返回的永远都是第一个实例对象的内存地址。可以这样实现：

# 重写new方法很固定，返回值必须是这个
# 这样就避免了创建多份。
# 创建第一个实例的时候，_instance是None，那么会分配空间创建实例。
# 此时的类属性已经被修改，_instance不再为None
# 那么当之后实例属性被创建的时候，由于_instance不为None。
# 则返回第一个实例对象的引用，即内存地址。
# 这样就应用了单例模式。
class A():
    _instance = None
    def __new__(cls,*args,**kwargs):
        if A._instance == None:
            A._instance = super().__new__(cls)
        return A._instance


a1 = A()
print(id(a1))
a2 = A()
print(id(a2))