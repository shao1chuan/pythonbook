import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2 * np.pi, 50)

ax1 = plt.subplot(2, 1, 1) # （行，列，活跃区）
plt.plot(x, np.sin(x), 'r')

ax2 = plt.subplot(2, 3, 4)
plt.plot(x, 2 * np.sin(x), 'g')

ax3 = plt.subplot(2, 3, 5, sharey=ax2)
plt.plot(x, np.cos(x), 'b')

ax4 = plt.subplot(2, 3, 6, sharey=ax2)
plt.plot(x, 2 * np.cos(x), 'y')

plt.show()