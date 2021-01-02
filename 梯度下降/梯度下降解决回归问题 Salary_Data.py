# https://www.cnblogs.com/judejie/p/8999832.html

# 工作年限与收入之间的散点图
# 导入第三方模块
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# 导入数据集
# income = pd.read_csv(r'Salary_Data.csv')
# 绘制散点图
# sns.lmplot(x = 'YearsExperience', y = 'Salary', data = income, ci = None)
# 显示图形


class GD():
    def __init__(self,data,w,b, lr, nstep):
        self.data = data
        self.w = w
        self.b = b
        self.lr = lr
        self.nstep = nstep

    def loss(self,w,b):
        x,y = self.data[:, 0],self.data[:, 1]
        loss = 0
        for i in range(data.shape[0]):
            loss += (w*x[i]+b-y[i])**2
        print(f"loss {loss}")
        return loss/float(data.shape[0])

    def step_grad(self,w,b):
        x, y = self.data[:, 0], self.data[:, 1]
        w_gradient = 0
        b_gradient = 0
        for i in range(data.shape[0]):
            w_gradient += 2*(w*x[i]+b-y[i])*x[i]
            b_gradient += 2 * (w * x[i] + b - y[i])

        w_new = w - w_gradient/data.shape[0]*self.lr
        b_new = b - b_gradient /data.shape[0] * self.lr
        return w_new,b_new

    def gradientDescent(self):
        # history = np.empty( (self.nstep+1, 2) )
        error = np.zeros(self.nstep)
        w,b = self.w,self.b
        for i in range(self.nstep):
            w,b = self.step_grad(w, b)
            error[i]=self.loss(w,b)
        return w,b,error
w = 12
b =12
income = pd.read_csv(r'Salary_Data.csv')
data = np.array(income.values)
nstep = 1000
lr = 0.001
gd = GD(data,w,b,lr,nstep)
w,b,error = gd.gradientDescent()
print("w,b is :",w,b)
x = data[:,0]
y = data[:,1]
plt.scatter(x,y)
# plt.legend()
plt.plot(x, w*x+b, 'r')
plt.show()

plt.plot(np.arange(nstep), error, 'r')
plt.show()
# 回归参数w,b的值：w,b is : 11768.548124439758 10167.865862562581
