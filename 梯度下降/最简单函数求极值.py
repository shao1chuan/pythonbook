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
      lr = 0.1
      steps = 40
      loss = []
      for i in range(steps):
            x = x-lr*df(x)
            loss.append(f(x))
      print(loss[i])
      # y = f(x)
      # print(y)
      plotf(loss)



if __name__ == '__main__':
    main()

