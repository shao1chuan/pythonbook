word="I'm a boby, I'm a girl. When it is true, it is ture. that are cats, the red is red."
word = word.replace('.','').replace(',','')
li = word.split()
print(li)

# 第一种方法：
key = set(li)
value = [0 for i in range(len(key))]
dic = {k:v for k,v in zip(key,value)}
print(dic)

for i in dic:
    for j in li:
        if i == j:
            dic[i]+=1
            continue
print(dic)

# 第二种方法：
s =set(li)
for i in s:
    count=word.count(i)
    print(i,'出现次数：',count)

# 第三种方法：
dict = {}
for key in li:
    dict[key] = dict.get(key,0) + 1
print(dic)
