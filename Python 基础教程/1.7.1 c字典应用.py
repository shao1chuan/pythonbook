import os
dic = {}
for name in os.listdir(os.path.join("练习")):
    dic[name] = len(dic.keys())
print(dic)