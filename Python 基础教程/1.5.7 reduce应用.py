from functools import reduce

lst=[1,2,3,4]
print(reduce(lambda x,y: x*y+1, lst))

#计算过程如下:
# 这个式子只有两个参数,没有初始化值,那么就取列表前2项,通过lambda函数计算结果
#1*2+1=3,
#上面计算的结果在与列表第三个元素通过lambda函数计算
# 3*3+1=10
#上面计算的结果在与列表第四个元素通过lambda函数计算
# 10*4+1=41

from functools import reduce
lst=[1,2,3,4]
print(reduce(lambda x,y: x+y, lst,5))

# 5是初始值,也可以理解为第三个参数
# 计算呢过程
# -->5+1=6
# -->6+2=8
# -->8+3=11
# -->11+4=15





x = int(input("输入5位正整数"))
print(list(str(x)))


23456
