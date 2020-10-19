# 插入
print('插入'*15)
x = [1,2,3]
print(x)
x = x+ [4]
x.append(5)
print(x)
x.insert(3,'w')
x.extend(['a','b'])
print(x*3)

# 删除
print("删除"*15)
y = ["a","b","c","d",'e','f']
del y[2]
print(y)
y.pop(0)
print(y)
y.remove('f')
print(y)

# 列表元素访问与计数
print("列表元素访问与计数"*5)
x =[1,2,3,3,4,5]
print(x.count(3),x.index(2))

# 列表排序
print("列表排序"*10)
x = [1,2,4,5,6,34,22,55,22,11,24,56,78]
import random as r
r.shuffle(x)
print(x)
x.reverse()
print("reverse",x)
x.sort(reverse = True)
print('sort ',x)
# 使用内置函数sorted对列表进行排序并返回新列表，不对原列表做任何修改。
sorted(x)
reversed(x)

# 打包
print("打包"*10)
a = [1,2,3]
b = [4,5,6]
print(list(zip(a,b)))

# 枚举
print("枚举"*10)
for item in enumerate('abcdef'):
    print(item)

# 遍历列表的三种方式
print("遍历列表的三种方式"*10)
a = ['a','b','c','d','e','f']
for i in a:
    print(i)
for i in range(len(a)):
    print(i,a[i])
for i,ele in enumerate(a):
    print(i,ele)









