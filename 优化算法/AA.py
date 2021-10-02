#coding:utf-8
# https://mp.weixin.qq.com/s/ac-CgZj-avmPBraVvQUuBQ
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
class Function():
    def __init__(self):
        self.points_x = np.linspace(-20, 20, 1000)
        self.points_y = self.f(self.points_x)

    def f(self,x):
        return (0.15*x)**2 + np.cos(x) + np.sin(3*x)/3 + np.cos(5*x)/5 + np.sin(7*x)/7

    def df(self,x):
        return (9/200)*x - np.sin(x) -np.sin(5*x) + np.cos(3*x) + np.cos(7*x)


    def ddf(self,x):
        return (9/200) - np.cos(x) -3*np.sin(x) - 5*np.cos(5*x) -7* np.sin(7*x)




# #
# #
# # # AdaGrad
# # for i in range(15):
# #     # 绘制原来的函数
# #     plt.plot(points_x, points_y, c="b", alpha=0.5, linestyle="-")
# #     # 算法开始
# #     lr = pow(1.5,-i)*32
# #     delta = 1e-7
# #     x = -20
# #     r = 0
# #     AdaGrad_x, AdaGrad_y = [], []
# #     for it in range(1000):
# #         AdaGrad_x.append(x), AdaGrad_y.append(f(x))
# #         g = df(x)
# #         r = r + g*g # 积累平方梯度
# #         x = x - lr /(delta + np.sqrt(r)) * g
# #
# #     plt.xlim(-20, 20)
# #     plt.ylim(-2, 10)
# #     plt.plot(AdaGrad_x, AdaGrad_y, c="r", linestyle="-")
# #     plt.scatter(AdaGrad_x[-1],AdaGrad_y[-1],90,marker = "x",color="g")
# #     plt.title("AdaGrad,lr=%f"%(lr))
# #     plt.savefig("AdaGrad,lr=%f"%(lr) + ".png")
# #     plt.clf()
# #
# #
# # # RMSProp
# # for i in range(15):
# #     # 绘制原来的函数
# #     plt.plot(points_x, points_y, c="b", alpha=0.5, linestyle="-")
# #     # 算法开始
# #     lr = pow(1.5,-i)*32
# #     delta = 1e-6
# #     rou = 0.8
# #     x = -20
# #     r = 0
# #     RMSProp_x, RMSProp_y = [], []
# #     for it in range(1000):
# #         RMSProp_x.append(x), RMSProp_y.append(f(x))
# #         g = df(x)
# #         r = rou * r + (1-rou)*g*g # 积累平方梯度
# #         x = x - lr /(delta + np.sqrt(r)) * g
# #
# #     plt.xlim(-20, 20)
# #     plt.ylim(-2, 10)
# #     plt.plot(RMSProp_x, RMSProp_y, c="r", linestyle="-")
# #     plt.scatter(RMSProp_x[-1],RMSProp_y[-1],90,marker = "x",color="g")
# #     plt.title("RMSProp,lr=%f,rou=%f"%(lr,rou))
# #     plt.savefig("RMSProp,lr=%f,rou=%f"%(lr,rou) + ".png")
# #     plt.clf()
# #

# #
