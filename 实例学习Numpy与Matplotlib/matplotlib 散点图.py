import matplotlib.pyplot as plt
import numpy as np

k = 500
x = np.random.rand(k)
y = np.random.rand(k)
size = np.random.rand(k) * 50 # 生成每个点的大小
colour = np.arctan2(x, y) # 生成每个点的颜色大小
plt.scatter(x, y, s=size, c=colour)
plt.colorbar() # 添加颜色栏

plt.show()