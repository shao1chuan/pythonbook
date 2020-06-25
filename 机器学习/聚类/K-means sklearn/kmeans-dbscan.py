import pandas as pd
beer = pd.read_csv('data.txt', sep=' ')
X = beer[["calories","sodium","alcohol","cost"]]
print(f'beer: {beer}, X:{X}')
# ## K-means算法实现 clustering
from sklearn.cluster import KMeans
km = KMeans(n_clusters=3).fit(X)
km2 = KMeans(n_clusters=2).fit(X)
print(f'labels: {km.labels_}')

beer['cluster'] = km.labels_
beer['cluster2'] = km2.labels_
beer.sort_values('cluster')

from pandas.plotting import scatter_matrix
# get_ipython().run_line_magic('matplotlib', 'inline')
cluster_centers = km.cluster_centers_
cluster_centers_2 = km2.cluster_centers_
beer.groupby("cluster").mean()
beer.groupby("cluster2").mean()
centers = beer.groupby("cluster").mean().reset_index()

# get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 14

import numpy as np
colors = np.array(['red', 'green', 'blue', 'yellow'])

plt.scatter(beer["calories"], beer["alcohol"],c=colors[beer["cluster"]])
plt.scatter(centers.calories, centers.alcohol, linewidths=3, marker='+', s=300, c='black')
plt.xlabel("Calories")
plt.ylabel("Alcohol")

scatter_matrix(beer[["calories","sodium","alcohol","cost"]],s=100, alpha=1, c=colors[beer["cluster"]], figsize=(10,10))
plt.suptitle("With 3 centroids initialized")

scatter_matrix(beer[["calories","sodium","alcohol","cost"]],s=100, alpha=1, c=colors[beer["cluster2"]], figsize=(10,10))
plt.suptitle("With 完整例子 centroids initialized")

plt.show()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
km = KMeans(n_clusters=3).fit(X_scaled)
beer["scaled_cluster"] = km.labels_
beer.sort_values("scaled_cluster")
beer.groupby("scaled_cluster").mean()
pd.plotting.scatter_matrix(X, c=colors[beer.scaled_cluster], alpha=1, figsize=(10,10), s=100)


# ## 聚类评估：轮廓系数（Silhouette Coefficient ）
# 
# <img src="1.png" alt="FAO" width="490">
# 
# - 计算样本i到同簇其他样本的平均距离ai。ai 越小，说明样本i越应该被聚类到该簇。将ai 称为样本i的簇内不相似度。
# - 计算样本i到其他某簇Cj 的所有样本的平均距离bij，称为样本i与簇Cj 的不相似度。定义为样本i的簇间不相似度：bi =min{bi1, bi2, ..., bik}
# 
# 
# * si接近1，则说明样本i聚类合理
# * si接近-1，则说明样本i更应该分类到另外的簇
# * 若si 近似为0，则说明样本i在两个簇的边界上。

from sklearn import metrics
score_scaled = metrics.silhouette_score(X,beer.scaled_cluster)
score = metrics.silhouette_score(X,beer.cluster)
print(score_scaled, score)

scores = []
for k in range(2,20):
    labels = KMeans(n_clusters=k).fit(X).labels_
    score = metrics.silhouette_score(X, labels)
    scores.append(score)
plt.plot(list(range(2,20)), scores)
plt.xlabel("Number of Clusters Initialized")
plt.ylabel("Sihouette Score")


# ##  DBSCAN clustering

from sklearn.cluster import DBSCAN
db = DBSCAN(eps=10, min_samples=2).fit(X)

labels = db.labels_
beer['cluster_db'] = labels
beer.sort_values('cluster_db')

beer.groupby('cluster_db').mean()

pd.plotting.scatter_matrix(X, c=colors[beer.cluster_db], figsize=(10,10), s=100)
