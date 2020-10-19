value = [1, 2, 3, 4, 5]
key = ['a', 'b', 'c', 'd', 'e']

# 以给定内容为键，创建值为空的字典
dic = dict.fromkeys(key)
print(dic)

# 使用dict()根据给定的键、值创建字典
dic = dict(name = 'aa',age = 23)
print (dic)

# zip创建字典
dic = dict(zip(key, value))
print(dic)

# 读取字典内容
print(dic.get('a'),dic['a'])

# 字典中定义其它类型数据
dic['a']= []
dic['a'].append(12)
dic['a'].append(13)

print(dic.get('a'),dic)

# 遍历字典
print('遍历字典'.center(50,'*'))
for i in dic.items():
    print (i)
for i,j in zip(dic.keys(),dic.values()):
    print(i,dic[i],j)



# 增加新元素  与更新 与删除
print('增加新元素'.center(50,'*'))
dic.setdefault('dd',12)
print(dic)
dic['cc']=22
print(dic)
dic.update({'dd':13,'ee':[11,22,33,44]})
print(dic)
dic.pop('dd')
print(dic)


# 字典popitem()方法作用是：随机返回并删除字典中的一对键和值（项）。
# 为什么是随机删除呢？因为字典是无序的，没有所谓的“最后一项”或是其它顺序。
# 在工作时如果遇到需要逐一删除项的工作，用popitem()方法效率很高。
for i in range(7):
    dic.popitem()
    print(dic)

# 有序字典
print('有序字典'.center(50,'*'))
import collections
dic = collections.OrderedDict()
dic = {'a':1,'b':2,'c':3}
print(dic)

