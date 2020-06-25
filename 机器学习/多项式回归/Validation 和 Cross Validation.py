import numpy as np
from sklearn import datasets
digits = datasets.load_digits()
X = digits.data
y = digits.target
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=666)
from sklearn.neighbors import KNeighborsClassifier
best_k, best_p, best_score = 0, 0, 0
# k为k近邻中的寻找k个最近元素
for k in range(2, 11):
# p为明科夫斯基距离的p
    for p in range(1, 6):
        knn_clf = KNeighborsClassifier(weights="distance", n_neighbors=k, p=p)
        knn_clf.fit(X_train, y_train)
        score = knn_clf.score(X_test, y_test)
        if score > best_score:
            best_k, best_p, best_score = k, p, score
print("Best K =", best_k)
print("Best P =", best_p)
print("Best Score =", best_score)

# 使用sklearn提供的交叉验证
from sklearn.model_selection import cross_val_score
knn_clf = KNeighborsClassifier()
# 返回的是一个数组，有三个元素，说明cross_val_score方法默认将我们的数据集分成了三份
# 这三份数据集进行交叉验证后产生了这三个结果
# cv默认为3，可以修改改参数，修改修改不同分数的数据集
cross_val_score(knn_clf,X_train,y_train,cv=3)
best_k, best_p, best_score = 0, 0, 0
for k in range(2, 11):
    for p in range(1, 6):
        knn_clf = KNeighborsClassifier(weights="distance", n_neighbors=k, p=p)
        scores = cross_val_score(knn_clf, X_train, y_train)
        score = np.mean(scores)
        if score > best_score:
            best_k, best_p, best_score = k, p, score
print("Best K =", best_k)
print("Best P =", best_p)
print("Best Score =", best_score)

knn_clf = KNeighborsClassifier(weights='distance',n_neighbors=2,p=2)
# 用我们找到的k和p。来对X_train,y_train整体fit一下，来看他对X_test,y_test的测试结果
knn_clf.fit(X_train,y_train)
# 注意这个X_test,y_test在交叉验证过程中是完全没有用过的，也就是说我们这样得出的结果是可信的
knn_clf.score(X_test,y_test)