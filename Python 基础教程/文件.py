# 用numpy读取文件
import numpy as np
data = np.genfromtxt('data.txt',delimiter=' ')
print(data)

# 1\. 打开 - 文件名需要注意大小写
file = open("data.txt",encoding='utf-8')
print(file)
# 完整例子\. 读取
text = file.read()
print(text)
# 3\. 关闭
file.close()
# write 方法 —— 写入文件
# 打开文件
f = open("abc.txt", "w")
print(f)
f.write("hello neuedu！\n")
f.write("今天天气真好")
# 关闭文件
f.close()
