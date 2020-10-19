# 集合是无序可变序列，使用一对大括号界定，元素不可重复，同一个集合中每个元素都是唯一的。
# 集合中只能包含数字、字符串、元组等不可变类型的数据，而不能包含列表、字典、集合等可变类型的数据。

cl = {1,2,3,4}
cl.add(5)
print(cl)

cl = set(range(1,15))
print(cl)

li = [i for i in range(1,10)]
li.append(1)
li.append(2)
print(li)

cl = set(li)
print(cl)

cl.update({44,55,'a'})
print(cl)
cl.remove('a')
print(cl)
