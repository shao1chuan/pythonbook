import numpy as np
import pandas as pd

# Series 是一个带有 名称 和索引的一维数组
# 一个 Series 包括了 data、index 以及 name
user_age = pd.Series(data=[18, 30, 25, 40])
user_age.index = ["Tom", "Bob", "Mary", "James"]
user_age.index.name = "name"
user_age.name="user_age_info"
print(user_age)

# 构建索引
name = pd.Index(["Tom", "Bob", "Mary", "James"], name="name")
# 构建 Series
user_age = pd.Series(data=[18, 30, 25, 40], index=name, name="user_age_info")