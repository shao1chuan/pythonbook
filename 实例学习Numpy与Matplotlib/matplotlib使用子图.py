
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2 * np.pi, 50)
ax1 = plt.subplot(2, 2, 1) # （行，列，活跃区）
plt.title('111111111')
plt.plot(x, np.sin(x), 'r',label="sin(x)")
plt.legend(loc='best')
ax2 = plt.subplot(2, 2, 2, sharey=ax1) # 与 ax1 共享y轴
plt.plot(x, 2 * np.sin(x), 'g',label="sin(x)")
plt.legend(loc='best')
ax3 = plt.subplot(2, 2, 3)
plt.plot(x, np.cos(x), 'b',label="sin(x)")
plt.legend(loc='best')
ax4 = plt.subplot(2, 2, 4, sharey=ax3) # 与 ax3 共享y轴
plt.plot(x, 2 * np.cos(x), 'y',label="sin(x)")
plt.legend(loc='best')
plt.show()