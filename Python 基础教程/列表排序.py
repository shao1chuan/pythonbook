aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
import random
random.shuffle(aList)                              #随机降序

print(aList)
aList.sort()                                              #默认是升序排序
aList.sort(reverse = True)                       #降序排序
print(aList)


# 返回可迭代的zip对象
aList = [1, 2, 3]
bList = [4, 5, 6]
cList = zip(aList, bList)
print(list(cList))

# enumerate()
for item in enumerate('abcdef'):
    print(item)

# 遍历列表的三种方式
a = ['a','b','c','d','e','f']
for i in a:
    print(i)
for i in range(len(a)):
    print(i,a[i])
for i,ele in enumerate(a):
    print("0000000   ",i,ele)

# 列表推导式
lis = [i for i in range(100)]
print(lis)

# 使用列表推导式实现嵌套列表的平铺
vec = [[1,2,3], [4,5,6], [7,8,9]]
lis = [num for elem in vec for num in elem]
print ("1111111111  ",lis)

# 过滤不符合条件的元素 从列表中选择符合条件的元素组成新的列表
aList = [-1,-4,6,7.5,-2.3,9,-11]
lis =  [i for i in aList if i>0]
print ("2222222222  ",lis)