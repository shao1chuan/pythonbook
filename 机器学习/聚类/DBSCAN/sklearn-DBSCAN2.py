import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
x1, y1 = datasets.make_circles(n_samples=2000, factor=0.5, noise=0.05)
x2, y2 = datasets.make_blobs(n_samples=1000, centers=[[1.2,1.2]], cluster_std=[[.1]])
#合并数据
x = np.concatenate((x1, x2))
plt.scatter(x[:, 0], x[:, 1], marker='o')
plt.show()
#KMeans
from sklearn.cluster import KMeans
y_pred = KMeans(n_clusters=3).fit_predict(x)
plt.scatter(x[:, 0], x[:, 1], c=y_pred)
plt.show()
# DBSCAN  无参数
from sklearn.cluster import DBSCAN
# 查看默认参数快捷键ctrl+p
y_pred = DBSCAN().fit_predict(x)
plt.scatter(x[:, 0], x[:, 1], c=y_pred)
plt.show()
# DBSCAN  有参数1
y_pred = DBSCAN(eps = 0.2).fit_predict(x)
plt.scatter(x[:, 0], x[:, 1], c=y_pred)
plt.show()
# DBSCAN  有参数2
y_pred = DBSCAN(eps = 0.2, min_samples=50).fit_predict(x)
plt.scatter(x[:, 0], x[:, 1], c=y_pred)
plt.show()

