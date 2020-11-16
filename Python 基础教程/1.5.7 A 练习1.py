# 1.有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和。
from functools import reduce
# A 构建list
a = 2
b = 1
l = [a/b]
for i in range(1,20):
    a,b = a+b,a
    l.append(a/b)
print(l)
print(reduce(lambda x,y:x+y,l))






