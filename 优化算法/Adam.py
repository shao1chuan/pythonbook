# Adam
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from AA import Function
ff = Function()

for i in range(48):
    # 绘制原来的函数
    plt.plot(ff.points_x, ff.points_y, c="b", alpha=0.5, linestyle="-")
    # 算法开始
    lr = pow(1.2,-i)*2
    rou1,rou2 = 0.9,0.9  # 原来的算法中rou2=0.999，但是效果很差
    delta = 1e-8
    x = -20
    s,r = 0,0
    t = 0
    Adam_x, Adam_y = [], []
    for it in range(1000):
        Adam_x.append(x), Adam_y.append(ff.f(x))
        t += 1
        g = ff.df(x)
        s = rou1 * s + (1 - rou1)*g
        r = rou2 * r + (1 - rou2)*g*g # 积累平方梯度
        s = s/(1-pow(rou1,t))
        r = r/(1-pow(rou2,t))
        x = x - lr /(delta + np.sqrt(r)) * s

    plt.xlim(-20, 20)
    plt.ylim(-2, 10)
    plt.plot(Adam_x, Adam_y, c="r", linestyle="-")
    plt.scatter(Adam_x[-1],Adam_y[-1],90,marker = "X",color="g")
    plt.title("Adam,lr=%f"%(lr))
    # plt.savefig("Adam,lr=%f"%(lr) + ".png")
    plt.show()
    plt.clf()