a_dict = {'server': 'db.neuedu.com', 'database': 'mysql'}
# 使用dict()利用已有数据创建字典
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
dictionary = dict(zip(keys, values))
print(dictionary)

x = dict() #空字典
# 使用dict()根据给定的键、值创建字典
d = dict(name='Dong', age=37)
print(d)

# 以给定内容为键，创建值为空的字典
adict = dict.fromkeys(['name', 'age', 'sex'])
print(adict,adict['name'])

# 使用字典对象的items()方法可以返回字典的键、值对列表
aDict={'name':'Dong', 'sex':'male', 'age':37}

# 使用字典对象的keys()方法可以返回字典的键列表
for item in aDict.items():
    print(item)
print(aDict.keys(),aDict.values())

# 使用字典对象的setdefault()方法返回指定“键”对应的“值”，如果字典中不存在该“键”，就添加一个新元素并设置该“键”对应的“值”。
aDict ={'name' : 'Wang','sex' : 'male'}
aDict.setdefault('age','28')     #增加新元素
aDict['address'] = 'SDIBT' #增加新元素
print(aDict)

# 使用字典对象的update方法将另一个字典的键、值对添加到当前字典对象
aDict = {'age': 37, 'score': [98, 97], 'name': 'Dong', 'sex': 'male'}
print(aDict.items())
aDict.update({'a':'a','b':'b'})
print(aDict)

# 判断一个key是否在字典中
d = {'name':'tom', 'age':10, 'Tel':110}
print ('name'  in d.keys())
print ('name' in d)

# 无序字典
x = dict()
x['a'] = 3
x['b'] = 5
x['c'] = 8

# 有序字典
import collections
x = collections.OrderedDict()


# 字典pop()方法
x = {'a':1,'b':2}
x.pop('a')

