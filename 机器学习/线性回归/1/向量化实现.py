import numpy as np
class SimpleLinearRegression2:
    def __init__(self):
        """初始化Simple Linear Regression模型"""
        self.a_ = None
        self.b_ = None
    def fit(self, x_train, y_train):
        """根据训练数据集x_train,y_train训练Simple Linear Regression模型"""
        assert x_train.ndim == 1, \
            "Simple Linear Regressor can only solve single feature training data."
        assert len(x_train) == len(y_train), \
            "the size of x_train must be equal to the size of y_train"
        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)
        self.a_ = (x_train - x_mean).dot(y_train - y_mean) / (x_train - x_mean).dot(x_train - x_mean)
        self.b_ = y_mean - self.a_ * x_mean
        return self
    def predict(self, x_predict):
        """给定待预测数据集x_predict，返回表示x_predict的结果向量"""
        assert x_predict.ndim == 1, \
            "Simple Linear Regressor can only solve single feature training data."
        assert self.a_ is not None and self.b_ is not None, \
            "must fit before predict!"
        return np.array([self._predict(x) for x in x_predict])
    def _predict(self, x_single):
        """给定单个待预测数据x_single，返回x_single的预测结果值"""
        return self.a_ * x_single + self.b_
    def __repr__(self):
        return "SimpleLinearRegression2()"

from 向量化实现 import SimpleLinearRegression2
x = np.array([1., 2., 3., 4., 5.])
y = np.array([1., 3., 2., 3., 5.])
x_predict = 6
reg2 = SimpleLinearRegression2()
reg2.fit(x, y)
reg2.predict(np.array([x_predict]))

import timeit
# timeit 模块定义了接受两个参数的 Timer 类。两个参数都是字符串。
# 第一个参数是你要计时的语句或者函数。
# 第二个参数是为第一个参数语句构建环境的导入语句。
# 从内部讲， timeit 构建起一个独立的虚拟环境， 手工地执行建立语句，然后手工地编译和执行被计时语句。
m = 1000000
big_x = np.random.random(size=m)
big_y = big_x * 2 + 3 + np.random.normal(size=m)
a = timeit.repeat('"-".join(str(n) for n in range(100))', number=10000)
a = timeit.repeat(stmt='pass', setup='pass',  number=1000000, globals=None)
timeit.timeit('reg2.fit(big_x, big_y)','import numpy as np;''from 向量化实现 import SimpleLinearRegression2;'
              'm = 1000000;''reg2 = SimpleLinearRegression2();''big_x = np.random.random(size=m);'
                                       'big_y = big_x * 完整例子 + 3 + np.random.normal(size=m)')
