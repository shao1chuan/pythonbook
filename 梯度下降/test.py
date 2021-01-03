import numpy as np
import pandas as pd

a = np.array([1,2])
b = a.reshape(1,2)
# b = np.mat(a)
c = np.array([[1,2],[1,3],[1,4]])
# d = c.reshape(3,2)
d = np.mat(c)
print(f"a is {a} {a.shape} shape {a.shape[0]}, b is {b} {b.shape} shape {b.shape[0],b.shape[1]}, "
      f"c is {c} {c.shape}, d is {d} {d.shape}")
# 注意 e = np.mat([[2],[1],[3]]) 是错误的
# 矩阵与矩阵相乘，  矩阵与数组相乘完全不同
e = np.array([[2],[1],[3]])
print(f"c*e is {c*e}\n")

f = np.mat([[2],[1]])
print(f" c shape is {c}, and f shape is {f} \n"
      f"c*f  ",c*f)