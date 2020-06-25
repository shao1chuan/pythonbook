# 集合的创建
a_set = set(range(8,14))
#自动去除重复
b_set = set([0, 1, 2, 3, 0, 1, 2, 3, 7, 8])
#空集合
c_set = set()

# 集合元素的增加与删除
s = {1,2,3}
s.add(3)
s.update({3,4,5})
s.remove(3)
print(s)

# 集合操作
a_set = set([8, 9, 10, 11, 12, 13])
b_set = {0, 1, 2, 3, 7, 8}
# 并集
print(a_set | b_set,a_set.union(b_set) )
#交集
print(a_set & b_set,a_set.intersection(b_set) )
#差集
print(a_set.difference(b_set),a_set - b_set)

# 测试是否为子集
x = {1, 2, 3}
y = {1, 2, 5}
z = {1, 2, 3, 4}
print(x.issubset(y),x.issubset(z))

# 使用集合快速提取序列中单一元素
import random
listRandom = [random.choice(range(500)) for i in range(100)]
noRepeat = []
for i in listRandom :
    if i not in noRepeat :
        noRepeat.append(i)
print(len(listRandom),len(noRepeat))
newSet = set(listRandom)

# 集合推导式
s = {x.strip() for x in ('  he  ', 'she    ', '    I')}
print(s)