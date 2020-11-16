# 列表推导式

x = [[1,2,3], [4,5,6], [7,8,9]]
y = [num for i in x for num in i]
print(f"y = [num for i in x for num in i] :{y}")
y = []
for i in x:
    for num in i:
        y.append(num)
print(y)
# 过滤不符合条件的元素 从列表中选择符合条件的元素组成新的列表
print('过滤不符合条件的元素 从列表中选择符合条件的元素组成新的列表'.center(50,'*'))
x = [-1,-4,6,7.5,-2.3,9,-11]
y = [i for i in x if i>0]
print(y)

x = [[x, y] for x in range(3) for y in range(3)]
print("[(x, y) for x in range(3) for y in range(3)]:  ",x)
x = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print("[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]:  ",x)





