import  numpy as np
# 可以由元组创建 ， 也可由列表创建
a = np.array(((1,2,3,4,5),(6,7,8,9,10),(11,12,13,14,15),(22,33,44,55,66)))
print(f"a = {a}")
a1 = a[np.ix_([0,2,3],[1,2])]
print(f"a1 = {a1}")
a2 = a[1,2]
print(f"a2 = {a2}")
a3 = a[0:2,:]
print(f"a3 = {a3}")
#  数组改变形状
a4 = a.reshape(2,10)
print(f"a4 = {a4}")
a5 = a.ravel()
print(f"a5 = {a5}")
a6 = a.ravel()
print(f"a6 = {a6}")
a7 = a.reshape(-1)
print(f"a7 = {a7}")

a8 = np.vstack([a7,a6])
print(f"a8 = {a8}")

a9 = np.hstack([a7,a6])
print(f"a9 = {a9}")

a = np.array(((1,2,3,4,5),(6,7,8,9,10),(11,12,13,14,15),(22,33,44,55,66)))
b = np.array(((22,33,44,55,66),(6,7,8,9,10),(11,12,13,14,15),(1,2,3,4,5)))

a10 = a[a==b]
print(f"a10 = {a10}")

a11 = np.where(a>10,100,a)
print(f"a11 = {a11}")

a12 = np.where(a>10,100,-100)
print(f"a12 = {a12}")
