import matplotlib.pyplot as plt
import numpy as np

x = ['北京', '上海', '深圳', '广州']
y = [60000, 58000, 50000, 52000]
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

plt.plot(x, y)
plt.show()