
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
# 相对路径
# # 在 Windows 上，文件的路径分割符号是 '\' ，
# 在 Linux 上 是 ‘/’为了让你的代码在不同的平台上都能运行，那么你写路径的时候是写 ‘/’ 还是写 '\' 呢？
# 为了让你的代码在不同的平台上都能运行，那么你写路径的时候是写 ‘/’ 还是写 '\' 呢？
# 使用 os.sep 的话，你就不用去考虑这个了，os.sep 根据你所处的平台，自动地采用相应的分割符号
path = 'data.txt'
pdData = pd.read_csv(path, header=None, names=['Exam 1', 'Exam 2', 'Admitted'])
pdData.head()
#  可以看到学生有两门成绩，学校是通过两门成绩来决定是否录取。
# 之后我们可以利用python的绘图包通过散点图的绘制来将数据更直接的表现出来。
#  画出正例 负例的散点图
positive = pdData[pdData['Admitted'] == 1]
negative = pdData[pdData['Admitted'] == 0]
# 画图区域的长和宽
# fig代表绘图窗口（Figure），ax代表这个绘图窗口上的坐标系（axes）。后面的ax.xxx则是表示对ax坐标系进行xxx操作
# 调用subplots函数
# 指定图像分辨率、大小和长宽比例
# 创建一个800*600像素、100dpi(每英寸100点)分辨率的图形
# 返回一个画布对象和一个轴数组
# fig,axe=plt.subplots(figsize=(8,6),dpi=100)
fig, ax = plt.subplots(figsize=(10, 5))
# 画散点图
ax.scatter(positive['Exam 1'], positive['Exam 2'], s=30, c='b', marker='o', label='Admitted')
ax.scatter(negative['Exam 1'], negative['Exam 2'], s=30, c='r', marker='x', label='Not Admitted')
ax.legend()
# 设置X轴标记为Exam 1 Score
ax.set_xlabel('Exam 1 Score')
# 设置Y轴标记为Exam 1 Score
ax.set_ylabel('Exam 2 Score')
# 设置图标题
# axe.set_title("y=x**2")
# 显示绘制的图片
# plt.show()


# 画图区域的长和宽
# fig代表绘图窗口（Figure），ax代表这个绘图窗口上的坐标系（axes）。后面的ax.xxx则是表示对ax坐标系进行xxx操作
# 调用subplots函数
# 指定图像分辨率、大小和长宽比例
# 创建一个800*600像素、100dpi(每英寸100点)分辨率的图形
# 返回一个画布对象和一个轴数组
# fig,axe=plt.subplots(figsize=(8,6),dpi=100)
fig, ax = plt.subplots(figsize=(10, 5))


## The logistic regression
def sigmoid(z):
    return 1 / (1 + np.exp(-z))#注意e的指数次形式的写法
#creates a vector containing 20 equally spaced values from -10 to 10
nums = np.arange(-10,10,step=1)
fig, ax = plt.subplots(figsize=(12,4))
# ax.plot(x,y,'go--')
# 上面的例子中：g表示颜色，o表示标记，--表示线型，标记类型和线型必须放在颜色后面
ax.plot(nums,sigmoid(nums), 'r')

# 预测函数模型
def model(X, theta):
    return sigmoid(np.dot(X,theta.T))
# in a try / except structure so as not to return an error if the block si executed several times
# 给输入特征变量添加一列全1
pdData.insert(0, 'Ones', 1)
# pdData.head()
# 打印出来是原始表格里的数据
# print(pdData)
# 将数据的Pandas表示转换为可用于进一步计算的数组
# set X (training data) and y (target variable)
# 表格转换为矩阵
orig_data = pdData.values
# 打印出来是矩阵形式
pdData.head()

# 样本维度
cols = orig_data.shape[1]
X = orig_data[:,0:cols-1]
Y = orig_data[:,cols-1:cols]
# 给参数占位
theta = np.zeros([1, 3])

# 平均损失 损失函数
def cost(X, Y, theta):
    left = np.multiply(-Y, np.log(model(X, theta)))
    right = np.multiply(1 - Y, np.log(1 - model(X, theta)))
    return np.sum(left - right) / (len(X))


# 计算梯度
def gradient(X, Y, theta):
    # 进行一个占位 初始化grad
    # 一维矩阵b, b.shape 为矩阵的长度
    grad = np.zeros(theta.shape)
    # 把H(0) - y
    error = (model(X, theta) - Y).ravel()
    for j in range(len(theta.ravel())):
        term = np.multiply(error, X[:, j])
        grad[0, j] = np.sum(term) / len(X)
    return grad

# Gradient descent
# 比较3中不同梯度下降方法
STOP_ITER = 0  #
STOP_COST = 1  # 根据损失函数
STOP_GRAD = 2  # 根据梯度
def stopCriterion(type, value, threshold):
    # 设定三种不同的停止策略
    if type == STOP_ITER:
        return value > threshold
    # 最近两次损失值差别不大
    elif type == STOP_COST:
        return abs(value[-1] - value[-2]) < threshold
    elif type == STOP_GRAD:
        return np.linalg.norm(value) < threshold

import numpy.random
# 数据要进行洗牌
def shuffleData(data):
    np.random.shuffle(data)
    cols = data.shape[1]
    X = data[:, 0:cols - 1]
    y = data[:, cols-1:]
    return X, y


import time


def descent(data, theta, batchSize, stopType, thresh, alpha):
    # 梯度下降求解
    init_time = time.time()
    # 迭代次数
    i = 0
    # batch
    k = 0
    X, y = shuffleData(data)
    # 计算梯度
    grad = np.zeros(theta.shape)
    # 损失值
    costs = [cost(X, y, theta)]

    while True:
        grad = gradient(X[k: k + batchSize], y[k: k + batchSize], theta)
        # 取batch数量个数据
        k += batchSize
        # 大于总数据
        if k >= n:
            k = 0
            # 重新洗牌
            X, y = shuffleData(data)
            # 参数更新
            theta = theta - alpha * grad
            # 计算新的损失
            costs.append(cost(X, y, theta))
            i += 1

            if stopType == STOP_ITER:
                value = i
            elif stopType == STOP_COST:
                value = costs
            elif stopType == STOP_GRAD:
                value = grad
            if stopCriterion(stopType, value, thresh): break
    return theta, i - 1, costs, grad, time.time() - init_time

def runExpe(data, theta, batchSize, stopType, thresh, alpha):
#     总数据
    n = 100
    #import pdb; pdb.set_trace();
    theta, iter, costs, grad, dur = descent(data, theta, batchSize, stopType, thresh, alpha)
    name = "Original" if (data[:,1]>2).sum() > 1 else "Scaled"
    name += " data - learning rate: {} - ".format(alpha)
    if batchSize == n: strDescType = "Gradient"
    elif batchSize==1:  strDescType = "Stochastic"
    else: strDescType = "Mini-batch ({})".format(batchSize)
    name += strDescType + " descent - Stop: "
    if stopType == STOP_ITER: strStop = "{} iterations".format(thresh)
    elif stopType == STOP_COST: strStop = "costs change < {}".format(thresh)
    else: strStop = "gradient norm < {}".format(thresh)
    name += strStop
    print ("***{}\nTheta: {} - Iter: {} - Last cost: {:03.2f} - Duration: {:03.2f}s".format(
        name, theta, iter, costs[-1], dur))
    fig, ax = plt.subplots(figsize=(12,4))
    ax.plot(np.arange(len(costs)), costs, 'r')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Cost')
    ax.set_title(name.upper() + ' - Error vs. Iteration')
    return theta

# 不同的停止策略
# 设定迭代次数
#选择的梯度下降方法是基于所有样本的
n=100 # 数据总共100行
runExpe(orig_data, theta, n, STOP_ITER, thresh=5000, alpha=0.000001)
# 根据损失值停止  按照损失函数的精度
# 设定阈值 1E-6, 差不多需要110 000次迭代
runExpe(orig_data, theta, n, STOP_COST, thresh=0.000001, alpha=0.001)
# 根据梯度变化停止
# 设定阈值 0.05,差不多需要40 000次迭代
runExpe(orig_data, theta, n, STOP_GRAD, thresh=0.05, alpha=0.001)
# 有点爆炸。。。很不稳定,再来试试把学习率调小一些
# 速度快，但稳定性差，需要很小的学习率
runExpe(orig_data, theta, 1, STOP_ITER, thresh=15000, alpha=0.000002)
plt.show()
