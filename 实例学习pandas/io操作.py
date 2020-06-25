# 导入相关库
import numpy as np
import pandas as pd
from io import StringIO

pd.read_csv("user_info.csv")


pd.read_csv("user_info.csv", index_col="name")

# 除了可以从文件中读取，我们还可以从 StringIO 对象中读取
data="name,age,birth,sex\nTom,18.0,2000-02-10,\nBob,30.0,1988-10-17,male"
print(data)
pd.read_csv(StringIO(data))
data = "name|age|birth|sex~Tom|18.0|2000-02-10|~Bob|30.0|1988-10-17|male"
pd.read_csv(StringIO(data), sep="|", lineterminator="~")