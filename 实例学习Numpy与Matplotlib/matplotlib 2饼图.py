# 导入第三方模块
import matplotlib.pyplot as plt

# 构造数据
edu = [0.2515,0.3724,0.3336,0.0368,0.0057]
labels = ['中专','大专','本科','硕士','其他']

# 绘制饼图
plt.pie(x = edu, # 绘图数据
           labels=labels, # 添加教育水平标签
          autopct='%.1f%%' # 设置百分比的格式，这里保留一位小数
       )
# 显示图形
plt.show()
