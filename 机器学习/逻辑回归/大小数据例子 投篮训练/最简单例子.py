import numpy as np
from sklearn.metrics import accuracy_score
# step 1 构造sigmoid函数(根据(0)式)
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
# step 2 构造预测函数(根据(1)式)
def model(X, theta):
    return sigmoid(np.dot(X, theta.T))
# step 3 构造损失函数(根据(1)式)
def cost(X, y, theta):
    left = np.multiply(-y, np.log(model(X, theta)))
    #print(left.shape)
    right = np.multiply(1 - y, np.log(1 - model(X, theta)))
    #print(right.shape)
    return np.sum(left - right) / (len(X))
# step 4 求出\theta的梯度方向(根据(13)式)
def gradient(X, y, theta):
    grad = np.zeros(theta.shape)
    error = (model(X, theta) - y).ravel()
    for j in range(len(theta.ravel())):
        term = np.multiply(error, X[:, j])
        grad[0, j] = np.sum(term) / len(X)
    return grad
# step 5 运用梯度下降方法求得最优解(根据(14式))
def descent(data, theta,y,thresh,alpha):
    #梯度下降求解
    i = 0 # 迭代次数
    costs = [cost(data, y, theta)] # 损失值
    while True:
        grad = gradient(data, y, theta)
        theta = theta - alpha*grad # 参数更新
        costs.append(cost(data, y, theta)) # 计算新的损失
        i += 1
        if i>thresh: break
    return theta, i-1, costs, grad
# step6 代入数据,进行运算
data=np.array([[1,34.623660,78.024693],[1,30.286711,43.894998],[1,35.847409,72.902198],
[1,60.182599,86.308552],[1,79.032736,75.344376]])
y=np.array([0,0,0,1,1]).reshape(-1,1)
theta=np.array([[0.5,0.5,0]])
theta, iter, costs, grad= descent(data, theta,y, 100, 0.00001)
