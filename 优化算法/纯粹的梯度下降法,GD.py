# 纯粹的梯度下降法,GD
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from AA import Function
ff = Function()

for i in range(10):
    # 绘制原来的函数
    plt.plot(ff.points_x, ff.points_y, c="b", alpha=0.5, linestyle="-")
    # 算法开始
    lr = pow(2,-i)*16
    x = -20.0
    GD_x, GD_y = [], []
    for it in range(1000):
        GD_x.append(x), GD_y.append(ff.f(x))
        dx = ff.df(x)
        x = x - lr * dx

    plt.xlim(-20, 20)
    plt.ylim(-2, 10)
    plt.plot(GD_x, GD_y, c="r", linestyle="--")
    plt.title("Gradient descent,lr=%f"%(lr))
    # plt.savefig("Gradient descent,lr=%f"%(lr) + ".png")
    plt.show()
    plt.clf()