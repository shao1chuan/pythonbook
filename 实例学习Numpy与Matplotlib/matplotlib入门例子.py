
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(x)

# plt.plot(x, y)
# plt.show()
# plt.plot(x, y)
# plt.plot(x, y * 2)
# plt.title("sin(x) & 2sin(x)")
# plt.show()

plt.plot(x, y, label="sin(x)")
plt.plot(x, y * 2, label="2sin(x)")
# plt.legend()
plt.legend(loc='best bbbbbbbbbb')
plt.show()