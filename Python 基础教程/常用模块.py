# 1.1. 时间处理模块
import time
print(time.time())


import datetime
a = datetime.datetime(year=2000, month=1, day=1, hour=12)
b = datetime.datetime(2000, 1, 1, 12, 0)
print(a,b,datetime.datetime.today(),datetime.datetime.now(),datetime.datetime.now().timestamp(),datetime.datetime.now().weekday())

# 获取当前工作目录
import sys

print(sys.path[0])
# 获取执行命令的位置
import os
print(os.getcwd())

# 路径拼接
import os

print(os.path.join('/Users/pangao', 'test.txt'))

# /Users/pangao/test.txt'

# 路径拆分
import os

print(os.path.split('/Users/pangao/test.txt'),os.path.splitext('/Users/pangao/test.txt'))

# ('/Users/pangao/', 'test.txt')

