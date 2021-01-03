
import matplotlib.pyplot as plt
import numpy as np
li = [i for i in range(100)]
x = np.array(li)

y = np.sin(x)

plt.plot(x, y)
plt.show()
