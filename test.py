
# -*- coding: utf-8 -*-
import sympy
import numpy as np
import math
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import matplotlib.pyplot as plt
import matplotlib

# 解决无法显示中文问题，fname是加载字体路径，根据自身pc实际确定，具体请百度
# zhfont1 = matplotlib.font_manager.FontProperties(fname='/System/Library/Fonts/Hiragino Sans GB W3.ttc')

# 随机产生3个参考节点坐标
maxy = 1000
maxx = 1000
cx = maxx * np.random.rand(3)
cy = maxy * np.random.rand(3)
dot1 = plot(cx, cy, 'k^')

# 生成盲节点，以及其与参考节点欧式距离
mtx = maxx * np.random.rand()
mty = maxy * np.random.rand()
# plt.hold('on')
dot2 = plot(mtx, mty, 'go')
da = math.sqrt(np.square(mtx - cx[0]) + np.square(mty - cy[0]))
db = math.sqrt(np.square(mtx - cx[1]) + np.square(mty - cy[1]))
dc = math.sqrt(np.square(mtx - cx[2]) + np.square(mty - cy[2]))


# 计算定位坐标
def triposition(xa, ya, da, xb, yb, db, xc, yc, dc):
    x, y = sympy.symbols('x y')
    f1 = 2 * x * (xa - xc) + np.square(xc) - np.square(xa) + 2 * y * (ya - yc) + np.square(yc) - np.square(ya) - (
                np.square(dc) - np.square(da))
    f2 = 2 * x * (xb - xc) + np.square(xc) - np.square(xb) + 2 * y * (yb - yc) + np.square(yc) - np.square(yb) - (
                np.square(dc) - np.square(db))
    result = sympy.solve([f1, f2], [x, y])
    locx, locy = result[x], result[y]
    return [locx, locy]


# 解算得到定位节点坐标
[locx, locy] = triposition(cx[0], cy[0], da, cx[1], cy[1], db, cx[2], cy[2], dc)
# plt.hold('on')
dot3 = plot(locx, locy, 'r*')

# 显示脚注
x = [[locx, cx[0]], [locx, cx[1]], [locx, cx[2]]]
y = [[locy, cy[0]], [locy, cy[1]], [locy, cy[2]]]
for i in range(len(x)):
    plt.plot(x[i], y[i], linestyle='--', color='g')
plt.title('Three point locate')
plt.legend(['Ref', '盲节点', 'Locate'], loc='lower right')
plt.show()
derror = math.sqrt(np.square(locx - mtx) + np.square(locy - mty))
print(derror)