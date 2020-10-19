# 3.有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），
# 凡报到3的人退出圈子，问最后留下的是原来第几号的那位。

list = [i for i in range(1,200)]
print(list)

while True:
    list.pop(2)
    before = list[:2]
    list = list[2:]
    list.extend(before)
    if list.__len__()<=2:
        break
print(list)