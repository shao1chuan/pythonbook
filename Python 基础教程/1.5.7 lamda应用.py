# https://blog.csdn.net/zjuxsl/article/details/77104382
# 一、lambda函数也叫匿名函数，即，函数没有具体的名称。先来看一个最简单例子：

def f(x):
  return x**2
print(f(4))
# Python中使用lambda的话，写成这样
g = lambda x : x**2
print (g(4))

# lambda语句中，冒号前是参数，可以有多个，用逗号隔开，冒号右边的返回值。
# lambda语句构建的其实是一个函数对象
from functools import reduce
reduce(lambda x,y:x+y, [1,2,3]) #6
reduce(lambda x,y:x * y, [1,2,4]) #8
reduce(lambda x,y: x and y, [True,False,True]) #False

def f(x, y):
  return x + y
reduce(lambda x, y: f(x, y), [1, 2, 3])  # 6






