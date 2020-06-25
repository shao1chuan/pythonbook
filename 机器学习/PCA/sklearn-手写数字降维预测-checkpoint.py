from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from sklearn import decomposition
import matplotlib.pyplot as plt
digits = load_digits()#载入数据
x_data = digits.data #数据
y_data = digits.target #标签
x_train,x_test,y_train,y_test = train_test_split(x_data,y_data) #分割数据1/4为测试数据，3/4为训练数据
mlp = MLPClassifier(hidden_layer_sizes=(100,50) ,max_iter=500)
mlp.fit(x_train,y_train )
predictions = mlp.predict(x_test)
print(classification_report(predictions, y_test))
print(confusion_matrix(predictions, y_test))
pca = decomposition.PCA()
pca.fit(x_data)
# 方差
pca.explained_variance_
# 方差占比
pca.explained_variance_ratio_
variance = []
for i in range(len(pca.explained_variance_ratio_)):
    variance.append(sum(pca.explained_variance_ratio_[:i+1]))
plt.plot(range(1,len(pca.explained_variance_ratio_)+1), variance)
plt.show()
pca = decomposition.PCA(whiten=True,n_components=0.8)
pca.fit(x_data)
pca.explained_variance_ratio_
x_train_pca = pca.transform(x_train)
mlp = MLPClassifier(hidden_layer_sizes=(100,50) ,max_iter=500)
mlp.fit(x_train_pca,y_train )
x_test_pca = pca.transform(x_test)
predictions = mlp.predict(x_test_pca)
print(classification_report(predictions, y_test))
print(confusion_matrix(predictions, y_test))