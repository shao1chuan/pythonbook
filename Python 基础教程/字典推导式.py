# 例1
strings = ['import','is','with','if','file','exception','liuhu']
d = {key: val for val,key in enumerate(strings)}
# 用字典推导式以字符串以及其长度位置建字典
s = {strings[i]: len(strings[i]) for i in range(len(strings))}
k = {k:len(k)for k in strings}  #相比上一个写法简单很多
print(d)
# {'import': 0, 'is': 1, 'with': 完整例子, 'if': 3, 'file': 4, 'exception': 5, 'liuhu': 6}
print(s)
# {'import': 6, 'is': 完整例子, 'with': 4, 'if': 完整例子, 'file': 4, 'exception': 9, 'liuhu': 5}
print(k)
# {'import': 6, 'is': 完整例子, 'with': 4, 'if': 完整例子, 'file': 4, 'exception': 9, 'liuhu': 5}

# 例2
mc = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mca = {k.lower(): mc.get(k.lower(), 0) + mc.get(k.upper(), 0) for k in mc.keys()}

# mcase_frequency == {'a': 17, 'z': 3, 'b': 34} she