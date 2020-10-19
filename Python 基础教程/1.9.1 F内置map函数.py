# map()函数接收两个参数，一个是函数，
# 一个是Iterable，map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回

# 例1 求列表[1,2,3,4,5,6,7,8,9],返回一个n*n 的列表

#一般解决方案
li = [1,2,3,4,5,6,7,8,9]
for ind,val in enumerate(li):
    li[ind] = val * val
print(li)
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 高级解决方案
li = [1,2,3,4,5,6,7,8,9]
print(list(map(lambda x:x*x,li)))
# [1, 4, 9, 16, 25, 36, 49, 64, 81]


#接受一个list并利用reduce()求积
from functools import reduce
li = [1,2,3,4,5,6,7,8,9]
print(reduce(lambda x,y:x * y,li))
# 结果=1*2*3*4*5*6*7*8*9 = 362880

# 在一个list中，删掉偶数，只保留奇数
li = [1, 2, 4, 5, 6, 9, 10, 15]
print(list(filter(lambda x:x % 2==1,li)))  # [1, 5, 9, 15]

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
li = list(range(1, 200))
print(list(filter(lambda x:int(str(x))==int(str(x)[::-1]),li)))

# 对列表按照绝对值进行排序
li= [-21, -12, 5, 9, 36]
print(sorted(li, key = lambda x:abs(x)))
# [5, 9, -12, -21, 36]

# 把下面单词以首字母排序
li = ['bad', 'about', 'Zoo', 'Credit']
print(sorted(li, key = lambda x : x[0]))
# 输出['Credit', 'Zoo', 'about', 'bad']
"""
对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
"""

# 假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序
print(sorted(L, key = lambda x : x[0]))
# 输出[('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]

# 再按成绩从高到低排序
print(sorted(L, key = lambda x : x[1], reverse=True))
# 输出[('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]