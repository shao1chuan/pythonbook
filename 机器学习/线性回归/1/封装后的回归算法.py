import numpy as np
import matplotlib.pyplot as plt
class SimpleLinearRegression1:
    def __init__(self):
        """初始化Simple Linear Regression 模型"""
        self.a_ = None
        self.b_ = None
    def fit(self, x_train, y_train):
        #根据训练集x_train，y_train 训练Simple Linear Regression 模型
        ## 求均值
        x_mean = x_train.mean()
        y_mean = y_train.mean()
        ## 分子
        num = 0.0
        ## 分母
        d = 0.0
        ## 计算分子分母
        for x_i, y_i in zip(x_train, y_train):
            num += (x_i-x_mean)*(y_i-y_mean)
            d += (x_i-x_mean) ** 2
        ## 计算参数a和b
        self.a_ = num/d
        self.b_ = y_mean - self.a_ * x_mean
        return self
    def predict(self, x_predict):
        #给定待预测集x_predict，返回x_predict对应的预测结果值"""
        return np.array([self._predict(x) for x in x_predict])
    def _predict(self, x_single):
#给定单个待预测数据x_single，返回x_single对应的预测结果值"""
        return self.a_*x_single+self.b_
    def __repr__(self):
        return "SimpleLinearRegression1()"
from 封装后的回归算法 import SimpleLinearRegression1
reg1 = SimpleLinearRegression1()
x = np.array([1., 2., 3., 4., 5.])
y = np.array([1., 3., 2., 3., 5.])
x_predict = 6
reg1.fit(x, y)
reg1.predict(np.array([x_predict]))
# reg1.a_
# reg1.b_
y_hat1 = reg1.predict(x)
plt.scatter(x, y)
plt.plot(x, y_hat1, color='r')
plt.axis([0, 6, 0, 6])
plt.show()