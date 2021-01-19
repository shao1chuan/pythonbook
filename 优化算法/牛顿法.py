# # 牛顿法

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from AA import Function
ff = Function()

for i in range(72):
    # 绘制原来的函数
    plt.plot(ff.points_x, ff.points_y, c="b", alpha=0.5, linestyle="-")
    # 算法开始
    alpha= pow(1.2,-i)*20
    x = -20.0
    Newton_x, Newton_y = [], []
    for it in range(1000):
        Newton_x.append(x), Newton_y.append(ff.f(x))
        g = ff.df(x)
        gg = ff.ddf(x)
        x = x - g/(gg+alpha)

    plt.xlim(-20, 20)
    plt.ylim(-2, 10)
    plt.plot(Newton_x, Newton_y, c="r", linestyle="-")
    plt.scatter(Newton_x[-1],Newton_y[-1],90,marker = "x",color="g")
    plt.title("Newton,alpha=%f"%(alpha))
    # plt.savefig("Newton,alpha=%f"%(alpha) + ".png")
    plt.show()
    plt.clf()