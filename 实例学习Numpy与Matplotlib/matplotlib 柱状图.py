import matplotlib.pyplot as plt
import numpy as np

k = 10
x = np.arange(k)
y = np.random.rand(k)
plt.bar(x, y) # 画出 x 和 y 的柱状图

# 增加数值
for x, y in zip(x, y):
    plt.text(x, y , '%.2f' % y, ha='center', va='bottom')

plt.show()