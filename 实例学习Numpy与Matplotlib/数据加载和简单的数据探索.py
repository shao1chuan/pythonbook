import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import datasets


# 加载数据集load_xxx
iris = datasets.load_iris()
# 是一个字典
iris.keys()
# dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names'])
# 数据文档
print(iris.DESCR)
print(iris.data,iris.data.shape,iris.target,iris.target_names)

# 所有的行，取前两列
X = iris.data[:,:2]
# X[:,0]这样可以取出第0列
plt.scatter(X[:,0],X[:,1])
plt.show()

y = iris.target
# marker 是形状
for i,colors,marker in [(0,"red","o"),(1,"blue","+"),(2,"green","x")]:
    plt.scatter(X[y==i,0],X[y==i,1],color=colors,marker=marker)
plt.show()

# 使用另外两个维度
X = iris.data[:,2:]
# marker 是形状
for i,colors,marker in [(0,"red","o"),(1,"blue","+"),(2,"green","x")]:
    plt.scatter(X[y==i,0],X[y==i,1],color=colors,marker=marker)
plt.show()