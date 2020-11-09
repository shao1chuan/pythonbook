# 概念：包就是一个文件夹，里面包含了若干py文件以及一个_init_.py文件。

# 方式一：from 包名 import 模块名
from syu import module
module.output()

# 方式二：from 包名.模块名 import 函数名
from syu.module import output
output()

# 方式三 ：import 包名.模块名
import syu.module as tt
tt.output()

# 方式四：from 包名 import *
# 前提是：将 init.py 文件中写入all变量(写入方式同模块导入的写入方式) 。 变量当中写入哪个模块则导入哪个模块，不写则什么都不导入 使用时：模块名.函数名() _init_.py
from syu import *
module.output()

# 方式五：import 包名
# 前提是：在包里面的init.py 文件里写入 from . import 模块名 init.py里面导入哪个模块 通过本方式就能使用哪个模块
# from . import module
import syu
syu.module.output()

