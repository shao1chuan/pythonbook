from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt
# 载入数据
data = np.genfromtxt("kmeans.txt", delimiter=" ")
# 训练模型
# eps距离阈值，min_samples核心对象在eps领域的样本数阈值
model = DBSCAN(eps=1.5, min_samples=4)
model.fit(data)
result = model.fit_predict(data)
print(result)
# 画出各个数据点，用不同颜色表示分类
mark = ['or', 'ob', 'og', 'oy', 'ok', 'om']
for i,d in enumerate(data):
    plt.plot(d[0], d[1], mark[result[i]])
plt.show()
