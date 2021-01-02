import  numpy as np
a = np.array([[1,2,3],[3,2,1]])
b = np.array([[1,2],[2,1],[3,1]])
aa,bb = np.array([[1,2,3],[1,1,1]]),np.array([[3,2,1],[1,1,1]])
# 二维数组的点积
a1 = np.dot(a,b)
a11 = np.matmul(a,b)
a111 = np.matmul(aa,bb.T)
print(f"a1 = {a1} a11 = {a11} a111 = {a111}")

# 二维数组的乘积
a2 = a*0.5
a22 = a*a
a222 = a*(a[:,0].reshape(2,1))
a2222 = a*(a[0,:].reshape(1,-1))
print(f"a2 = {a2}, "
      f"a22 = {a22},\n"
      f"a222 = {a222}\n,"
      f"a2222 = {a2222}\n,"
      f"a2 sum = {a2[:,0].sum()}")

# a22 = a*(b[0].reshape(-1).T)
# print(f"a22 a*b = {a22}")

# 二维数组的行

c = np.arange(16).reshape(4,-1)
# 二维数组的对角线元素
a3 = np.diag(c)
print(f"a3 = {a3}")
# 以元素为对角线产生二维数组
a4 = np.diag(a3)
print(f"a4 = {a4}")
# 特征根与特征向量
a5 = np.linalg.eig(c)
print(f"a5 = {a5}")

# 线性方程组求解 ax=b
a = np.array([[1,2,3],[2,3,1],[3,2,1]])
b = np.array([24,39,26])
x = np.linalg.solve(a,b)
print(f"x = {x}")

# 范数的计算
c = np.arange(1,3).reshape(-1)
a6 = np.linalg.norm(c,ord = 2)
print(f"c = {c}, a6 = {a6}")

a7 = np.zeros((3,4))
print(f"a7 = {a7}")
a8 = np.eye(2,3)
print(f"a8 = {a8}")
a9 = np.ones((3,3))
print(f"a9 = {a9}")
# 矩阵主对角线元素之和
a10 = np.trace(a9)
print(f"a10 = {a10}")
# 两个数组内积

# 矩阵a的列 必须与 矩阵b的行相同
a111 = np.array([[1,2,3],[1,1,1]])
b111 = np.array([[3,2,1],[1,1,1]])
c111 = np.array([[1],[2]])
a11 = np.inner(a111,b111)
a12 = np.dot(a111,b111.T)
# 两个数组对应元素相乘
b11 = a111*b111
print(f"b11 = {b11}")
b112 = np.multiply(a111,b111)
print(f"b112 = {b112}")
b12 = a111*2
print(f"b12 = {b12}")
b13 = a111*c111
print(f"b13 = {b13}")
# 以下四种一样
a13 = np.mat(a111)@np.mat(b111.T)
a14 = np.mat(a111)*np.mat(b111.T)
a15 = np.dot(np.mat(a111),np.mat(b111.T))
a16 = np.inner(np.mat(a111),np.mat(b111))
print(f"a11 = {a11}")
print(f"a12 = {a12}")
print(f"a13 = {a13}")
print(f"a14 = {a14}")
print(f"a15 = {a15}")
print(f"a16 = {a16}")

a17 = np.zeros((3,2))
print(f"a17 = {a17}")

a18 = np.empty((3,2))
print(f"a18 = {a18}")

a19 = np.array([1,1])
a18[1]= a19
print(a18)
