
# enumerate 可以加索引
fruit = ["apple",'orange',"banana","balabala"]

for i,x in enumerate(fruit):
    print(i,x)

# 反方向输出
for i,x in enumerate(reversed(fruit)):
    print(i,x)

# 按照字典顺序输出
for i,x in enumerate(sorted(fruit)):
    print(i,x)
###