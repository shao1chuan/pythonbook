# https://www.bilibili.com/video/BV1ar4y137GD/?spm_id_from=333.337.search-card.all.click&vd_source=311a862c74a77082f872d2e1ab5d1523
import numpy as np
import matplotlib.pyplot as plt


def f(x):
      return x**2-3

def df(x):
      return 2*x
def plotf(loss):
      x = range(len(loss))
      plt.plot(x,loss)
      plt.xlabel('Iteration')
      plt.ylabel('Loss')
      plt.show()

def main():
      x = 15
      lr = 1.1
      steps = 400
      loss = []
      for i in range(steps):
            x = x-lr*df(x)
            loss.append(f(x))
            # print(loss[i])
      y = f(x)
      print(y)
      plotf(loss)



if __name__ == '__main__':
    main()

