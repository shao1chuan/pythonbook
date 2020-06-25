import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target
print(X,y)
X = X[y<2,:2]
y = y[y<2]
X.shape
(100, 2)
y.shape
(100,)
plt.scatter(X[y==0,0], X[y==0,1], color="red")
plt.scatter(X[y==1,0], X[y==1,1], color="blue")
plt.show()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)
import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
LogisticRegression()
log_reg.score(X_test, y_test)
log_reg.predict_proba(X_test)
log_reg.predict(X_test)
