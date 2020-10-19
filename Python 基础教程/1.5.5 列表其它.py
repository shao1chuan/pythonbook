a_num = [0.01,"zhangsan",[1,2,3]]
a_num+=[2]
print(a_num)
print(a_num*2)
print("使用列表的pop()方法删除并返回指定（默认为最后一个）位置上的元素，如果给定的索引超出了列表的范围则抛出异常。")
print(a_num.pop())
print(a_num.pop(1))
print(a_num)

# 删除首次出现的指定元素，如果列表中不存在要删除的元素，则抛出异常
x = [1,2,2,3,4]
x.remove(2)
print(x)


a_list = list("Hello")
print(a_list)

a_list.append('w')
print(a_list)

a_list.insert(1,2)
print(a_list)

# 统计指定元素在列表对象中出现的次数。
x =[1,2,3,3,4,5]
print(x.count(3))
print(3 in x)