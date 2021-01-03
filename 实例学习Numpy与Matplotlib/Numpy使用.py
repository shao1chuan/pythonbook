import  numpy as np
a1 = np.array([i for i in range(10)])
a2 = np.zeros(10)
a3 = np.ones(10)
a4 = np.ones((3,5))
a5 = np.full((3,5),123)
a6 = np.arange(0,10,2)
# 0到10之间 插入15个元素
a7 = np.linspace(0,10,15)
# random
a8 = np.random.randint(0,10,size=(3,5),dtype=int)
a9 = np.random.random((3,5))
# 参数loc(float)：正态分布的均值，对应着这个分布的中心。
# 参数scale(float)：正态分布的标准差
# 参数size(int 或者整数元组)：输出矩阵的shape，默认为None
a10 = np.random.normal(0,10,(3,5))

# seed( ) 是用于指定随机数生成时所用算法开始的整数值，
# 代码中每执行一次都使用了相同的随机数种子28，所以生成的随机数是相同的。
np.random.seed(12)
a11 = np.random.random((3,5))
np.random.seed(12)
a12 = np.random.random((3,5))

a13 = np.ndarray((4,2),dtype='f')
l = [1,2,3,4]
a14 = np.array(l)
print(f"a1 = {a1}   "
      f"a2 = {a2}   "
      f"a3 = {a3}   "
      f"a4 = {a4}   "
      f"a5 = {a5}   "
      f"a6 = {a6}   "
      f"a7 = {a7}   "
f"a8 = {a8}   "
f"a9 = {a9}   "
f"a10 = {a10}   "
f"a11 = {a11}   "
f"a12 = {a12}   "
f"a13 = {a13}   "
f"a14 = {a14}   "
      )

a = np.array([2,3,1])
b = np.array([1,2,1])
print(f"a15 = {(a*b).sum()}  a len = {len(a)}")