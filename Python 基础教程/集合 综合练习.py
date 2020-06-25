word="I'm a boby, I'm a girl. When it is true, it is ture. that are cats, the red is red."
word=word.replace(',','').replace('.','')
word=word.split()
print(word)
print('第1种方法')
setword=set(word)
for i in setword:
    count=word.count(i)
    print(i,'出现次数：',count)
print('第2种方法')
dict = {}
for key in word:
    dict[key] = dict.get(key, 0) + 1
print(dict)
print('第3种方法')
from collections import Counter

result = Counter(dict)
print(result)
print(result.most_common(3))