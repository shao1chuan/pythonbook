import  numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,100,100)
np.random.seed(111)
y1 = np.random.normal(0,1,100)
# y1 = np.linalg.norm(y1,ord = 2)

plt.plot(x,y1)
plt.show()
