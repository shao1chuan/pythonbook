
# 都变成大写
fruit = ["apple",'orange',"banana","balabala"]
print(fruit)
fruit = [x.upper() for x in fruit]
print(fruit)

#挑选出以b开头的水果
b = []
for x in fruit:
    if x.startswith("B"):
        b.append(x)
print(b)

b = [x.lower() for x in fruit if x.startswith("B")]
print(b)

