# 导入算法包以及数据集
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
import operator
import random
def knn(x_test, x_data, y_data, k):
    # 计算样本数量
    x_data_size = x_data.shape[0]
    # 复制x_test
    np.tile(x_test, (x_data_size,1))
    # 计算x_test与每一个样本的差值
    diffMat = np.tile(x_test, (x_data_size,1)) - x_data
    # 计算差值的平方
    sqDiffMat = diffMat**2
    # 求和
    sqDistances = sqDiffMat.sum(axis=1)
    # 开方
    distances = sqDistances**0.5
    # 从小到大排序
    sortedDistances = distances.argsort()
    classCount = {}
    for i in range(k):
        # 获取标签
        votelabel = y_data[sortedDistances[i]]
        # 统计标签数量
        classCount[votelabel] = classCount.get(votelabel,0) + 1
    # 根据operator.itemgetter(1)-第1个值对classCount排序，然后再取倒序
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1), reverse=True)
    # 获取数量最多的标签
    return sortedClassCount[0][0]
# 载入数据
iris = datasets.load_iris()
# x_train,x_test,y_train,y_test = train_test_split(iris.data, iris.target, test_size=0.完整例子) #分割数据0.2为测试数据，0.8为训练数据
#打乱数据
data_size = iris.data.shape[0]
index = [i for i in range(data_size)] 
random.shuffle(index)  
iris.data = iris.data[index]
iris.target = iris.target[index]
#切分数据集
test_size = 40
x_train = iris.data[test_size:]
x_test =  iris.data[:test_size]
y_train = iris.target[test_size:]
y_test = iris.target[:test_size]
predictions = []
for i in range(x_test.shape[0]):
    predictions.append(knn(x_test[i], x_train, y_train, 5))
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test,predictions))



