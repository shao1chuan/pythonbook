# python sklearn模型中random_state参数的意义
# random_state 相当于随机数种子random.seed() 。random_state 与 random seed 作用是相同的。
# 1 随机数种子代码演示：在1-100中取10个随机数
# 第一段和第二段代码完全相同，都没有设置 random seed。它每次取的结果就不同，它的随机数种子与当前系统时间有关。
import random
print([random.randint(1,100) for _ in range(10)])
print([random.randint(1,100) for _ in range(10)])
print(random.seed(1),[random.randint(1,100) for _ in range(10)])
print(random.seed(1),[random.randint(1,100) for _ in range(10)])
# 如果你在需要设置随机数种子的地方都设置好，那么当别人重新运行你的代码的时候就能得到完全一样的结果，复现和你一样的过程。
# random_state参数：
# 例如：在sklearn可以随机分割训练集和测试集（交叉验证），只需要在代码中引入model_selection.train_test_split就可以了：
from sklearn import model_selection
x_train, x_test, y_train,y_test=model_selection.train_test_split(x,y,test_size=0.2,random_state=0)
# 这里的random_state就是为了保证程序每次运行都分割一样的训练集和测试集。否则，同样的算法模型在不同的训练集和测试集上的效果不一样。
