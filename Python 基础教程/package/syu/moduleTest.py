# 一个.py文件就称为一个模块
# 方式一：import 模块名
import module
module.output()
# 方式二 :from 模块名 import 函数名
from module import output
output()
# 方式三: from 模块名 import *
from module import *
output()
# 方式四:from 模块名 import 函数名 as tt(自定义)
from module import output as tt
tt()



