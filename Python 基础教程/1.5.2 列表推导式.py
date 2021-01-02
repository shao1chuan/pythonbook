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


import numpy as np
x1 = [[x] for x in range(3)]
print("x1 = [[x] for x in range(3)] ",x1)
x2 = [x for x in range(3)]
print("[x2= x for x in range(3)] ",x2)
x3 = [np.random.randn(ch1) for ch1 in [4]]
print("x3 = ",x3)
x4 = [np.random.randn(ch1) for ch1 in [4,1,5]]
print("x4 = ",x4)
x5 = np.random.random((4,1))
print("x5 = ",x5)
np.random.seed(1)
x6 = [np.random.randn(ch1,ch2) for ch1,ch2 in zip([4],[1])]
print("x6 = ",x6)

w7 = [np.random.randn(ch1) for ch1 in ([4,2])]
print("w7 = ",w7)
# 注意：   ch1 的列要与 ch2 行相同

w8 = [np.random.randn(ch1, ch2) for ch1, ch2 in zip([2,3], [3,1])]
print("w8 = ",w8)
w8 = [np.random.randn(ch1, ch2) for ch1, ch2 in zip([2,3], [3,1])]
print("w8 = ",w8)




