# 查看文本中的数据

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
path = 'data.txt'
Data = pd.read_csv(path, header=None, names=['X1', 'X2', 'Admitted'])
print(Data.head())
print(Data.shape)
# 画出数据图像
positive = Data[Data['Admitted'] == 1]
negative = Data[Data['Admitted'] == 0]
# print(positive.head())
fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(positive['X1'], positive['X2'], s=30, c='b', marker='o', label='Admitted')
ax.scatter(negative['X1'], negative['X2'], s=30, c='r', marker='o', label='negative')
ax.legend()
ax.set_xlabel('X1 Score')
ax.set_ylabel('X2 Score')
plt.show()

# 逻辑回归各个模块
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
# sigmoids函数
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
# 模型
def model(X, theta):
    return sigmoid(np.dot(X, theta.T))
# 损耗计算
def cost(X, Y, theta):
    left = np.multiply(-Y, np.log(model(X, theta)))
    right = np.multiply(1 - Y, np.log(1 - model(X, theta)))
    return np.sum(left - right) / len(X)
# 计算梯度
def gradient(X, Y, theta):
    grad = np.zeros(theta.shape)
    error = (model(X, theta) - Y).ravel()
    for j in range(len(theta.ravel())):
        term = np.multiply(error, X[:, j])
        grad[0, j] = np.sum(term) / len(X)
    return grad
# 洗牌
def shuffleData(data):
    np.random.shuffle(data)
    cols = data.shape[1]
    X = data[:, 0:cols - 1]
    Y = data[:, cols - 1:]
    return X, Y
# 停止策略
def stopCriterion(type, value, threshold):
    if type == 'Stop_iter':
        return value > threshold
    elif type == 'Stop_cost':
        return abs(value[-1] - value[-2]) < threshold
    elif type == 'Stop_grad':
        return np.linalg.norm(value) < threshold
# 梯度下降求解
def descent(data, batchSize, stopType, thresh, alpha):
    init_time = time.time()
    i = 0  # 迭代次数
    k = 0  # batch
    theta = np.zeros([1, 3])
    X, Y = shuffleData(data)
    grad = np.zeros(theta.shape)
    costs = [cost(X, Y, theta)]
    n = data.shape[0] - batchSize
    while True:
        grad = gradient(X[k:k + batchSize], Y[k:k + batchSize], theta)
        k += batchSize
        if k > n:
            k = 0
            X, Y = shuffleData(data)
        theta = theta - alpha * grad
        costs.append(cost(X, Y, theta))
        i += 1
        if stopType == 'Stop_iter':
            value = i
        elif stopType == 'Stop_cost':
            value = costs
        elif stopType == 'Stop_grad':
            value = grad
        else:
            print('stopType 参数设置错误，请重试')
            break
        if stopCriterion(stopType, value, thresh):
            break
    return theta, i, costs, grad, time.time() - init_time
# 数据标准化
# 进行训练之前，我们还需要对数据进行标准化处理
# 增加一列为X0
Data.insert(0, 'X0', 1)
print(Data.head())
# 构建训练集X和目标变量Y
orig_data = Data.values  # 将列表转化为矩阵
print(orig_data.shape)
cols = orig_data.shape[1]
X = orig_data[:, 0:cols - 1]
Y = orig_data[:, cols - 1:cols]
# 简单实现
# 例如我们要进行随机梯度下降，我们可以通过调用一下代码段实现
theta,iter_times,costs,grad,cost_time=descent(orig_data,10,'Stop_iter',5000,0.000001)
fig,ax = plt.subplots(figsize=(10,5))
plt.plot(range(iter_times+1),costs,c='r',label='0.000001')
plt.show()
# 不同batchSize的对结果的影响
def Test_batchSize(data):
    # batchSize的大小对结果的影响
    # 三种规格也代表着是三种梯度下降策略：随机梯度下降、小批量梯度下降、批量梯度下降
    batchSize = [1, data.shape[0] // 10, data.shape[0]]
    color = ['r', 'b', 'y']
    thresh = 5000
    alpha = 0.000001
    plt.subplots(figsize=(10, 5))
    print('#' * 50)
    print()
    for size, c in zip(batchSize, color):
        theta, iter_times, costs, grad, cost_time = descent(data, size, 'Stop_iter', thresh, alpha)
        plt.plot(range(iter_times + 1), costs, c=c, label=str(size))
        print('batchSize = %3d   cost_time = %f s' % (size, cost_time))
    print()
    print('#' * 50)
    plt.xlabel('Cost')
    plt.ylabel('Iter times')
    plt.legend()
    plt.show()

    # 不同学习率对结果的影响
def Test_alpha(data):
    #学习率alpha的大小对结果的影响
    alpha=[1e-5,1e-6,1e-7,1e-8,1e-9]
    color = ['r', 'b', 'y','c','k']
    thresh = 30000
    plt.subplots(figsize=(10, 5))
    print('#' * 50)
    print()
    for a, c in zip(alpha, color):
        theta, iter_times, costs, grad, cost_time = descent(data, data.shape[0]//10, 'Stop_iter', thresh, a)
        plt.plot(range(iter_times + 1), costs, c=c, label=str(a))
        print('alpha = %9f   cost = %f ' % (a, costs[-1]))
    print()
    print('#' * 50)
    plt.ylabel('Cost')
    plt.xlabel('Iter times')
    plt.legend()
    plt.show()