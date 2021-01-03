import math
import numpy as np
import matplotlib.pyplot as plt

def f(r):
    g = 9*np.tan(r)+9*np.tan(3/4*np.pi-r)
    return g

def drawfig(f):

    x = np.linspace(1.01/4*np.pi,0.99/2*np.pi,100)
    y = f(x)
    # print(y)
    plt.plot(x,y)
    plt.show()

def grad(r):
    g = 9.0/(np.cos(r)**2) - 9.0/(np.cos(3/4*np.pi-r)**2)
    return g

def gradientDescent(f,r0, eta, nstep):
    r_history = np.zeros(nstep+1)
    f_history = np.zeros(nstep+1)
    r_history[0] = r0
    f_history[0] = f(r0)
    r = r0
    for i in range(1,nstep+1):
        r = r - eta * grad(r)
        r_history[i] = r
        f_history[i] = f(r)
        print(f"r is :{r}   f(r) is {f(r)}")
    return r_history,f_history
# print(f(1/3*np.pi))
drawfig(f)
x,y = gradientDescent(f, 1.22/4*np.pi, 0.0001*np.pi, 10000)
plt.plot(x,y)
plt.show()


