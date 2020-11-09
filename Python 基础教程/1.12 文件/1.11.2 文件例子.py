import random

f = open('data.txt', 'w+')
for i in range(100000):
    f.write(str(random.randint(1,100)) + '\n')
print(f.read())
f.close()

from collections import Counter
dict={}
f = open('data.txt', 'r+')
for i in f:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] = dict[i] + 1
d = Counter(dict)
with open('mostNum.txt', 'w+') as k:
    for i in d.most_common(10):
        k.write(f'{i[0].strip()}--------{i[1]}\n')
    k.seek(0, 0)
    print(k.read())
f.close()