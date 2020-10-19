value = [1, 2, 3, 4, 5]
key = ['a', 'b', 'c', 'd', 'e']

dic = {k:v for k,v in zip(key,value)}
print(dic)

dic = {k:v+1 for v,k in enumerate(key)}
print(dic)

dic = {key[i]:value[i] for i in range(len(key))}
print(dic)