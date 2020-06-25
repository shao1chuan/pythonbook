# 文件重命名
import os
os.rename('test.txt', 'test.py')    #重命名
# 删除文件
import os

os.remove('test.txt')    #删除
# 复制文件
import shutil

shutil.copyfile('test.txt', 'test.py')

# 遍历文件夹下的文件
import os

for filename in os.listdir('/'):
    print(filename)