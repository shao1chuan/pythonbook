# 动量 + 梯度下降法

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from AA import Function
ff = Function()
for i in range(10):
    # 绘制原来的函数
    plt.plot(ff.points_x, ff.points_y, c="b", alpha=0.5, linestyle="-")
    # 算法开始
    lr = 0.002
    m = 1 - pow(0.5,i)
    x = -20
    v = 1.0
    GDM_x, GDM_y = [], []
    for it in range(1000):
        GDM_x.append(x), GDM_y.append(ff.f(x))
        v = m * v - lr * ff.df(x)
        x = x + v

    plt.xlim(-20, 20)
    plt.ylim(-2, 10)
    plt.plot(GDM_x, GDM_y, c="r", linestyle="-")
    plt.scatter(GDM_x[-1],GDM_y[-1],90,marker = "x",color="g")
    plt.title("Gradient descent + momentum,lr=%f,m=%f"%(lr,m))
    # plt.savefig("Gradient descent + momentum,lr=%f,m=%f"%(lr,m) + ".png")
    plt.show()
    plt.clf()