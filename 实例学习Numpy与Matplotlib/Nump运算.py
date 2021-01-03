import  numpy as np
a1 = np.array([i for i in range(1,5)])
np.exp2(a1)
np.power(3, a1)
np.log10(a1)
print(f"a1 = {a1}   "
      )
a2 = a1.reshape((2,2))
a3 = a2.T
print(f"a2 = {a2}\n"
      f"a3 = {a3}\n"
      f"加法 ：a2+a3 = {a2+a3}\n"
      f"矩阵乘 a2.dot(a3) = {a2.dot(a3)}\n"
      f"乘法：a2*a3 = {a2*a3}\n"
f"矩阵的逆：np.linalg.inv(a2) = {np.linalg.inv(a2)}\n"
      f" a2.dot(np.linalg.inv(a2)) = {a2.dot(np.linalg.inv(a2))}\n"
f"矩阵的伪逆：np.linalg.pinv(a2) = {np.linalg.pinv(a2)}\n"
      )