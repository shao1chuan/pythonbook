from skimage import io
from sklearn.cluster import KMeans
import numpy as np

image = io.imread('test.jpg')

io.imshow(image)
io.show()

rows = image.shape[0]
cols = image.shape[1]

image = image.reshape(image.shape[0]*image.shape[1],3)
kmeans = KMeans(n_clusters=256, n_init=10,max_iter=200)
kmeans.fit(image)
print(kmeans.labels_)

clusters = np.asarray(kmeans.cluster_centers_,dtype=np.uint8)
labels = np.asarray(kmeans.labels_,dtype=np.uint8)
labels = labels.reshape(rows,cols)

print(clusters.shape)
io.imsave('after.jpg',labels)