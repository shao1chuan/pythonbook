import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
# 创建40个点
x_data = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]
y_data = [0]*20 +[1]*20
plt.scatter(x_data[:,0],x_data[:,1],c=y_data)
plt.show()
#fit the model
model = svm.SVC(kernel='linear')
model.fit(x_data, y_data)
model.coef_
model.intercept_
# 获取分离平面
plt.scatter(x_data[:,0],x_data[:,1],c=y_data)
x_test = np.array([[-5],[5]])
d = -model.intercept_/model.coef_[0][1]
k = -model.coef_[0][0]/model.coef_[0][1]
y_test = d + k*x_test
plt.plot(x_test, y_test, 'k')
plt.show()
model.support_vectors_
# 画出通过支持向量的分界线
b1 = model.support_vectors_[0]
y_down = k*x_test + (b1[1] - k*b1[0])
b2 = model.support_vectors_[-1]
y_up = k*x_test + (b2[1] - k*b2[0])
plt.scatter(x_data[:,0],x_data[:,1],c=y_data)
x_test = np.array([[-5],[5]])
d = -model.intercept_/model.coef_[0][1]
k = -model.coef_[0][0]/model.coef_[0][1]
y_test = d + k*x_test
plt.plot(x_test, y_test, 'k')
plt.plot(x_test, y_down, 'r--')
plt.plot(x_test, y_up, 'b--')
plt.show()



