# DataFrame 是一个带有索引的二维数据结构，每列可以有自己的名字，并且可以有不同的数据类型。
# 你可以把它想象成一个 excel 表格或者数据库中的一张表，DataFrame 是最常用的 Pandas 对象。

import numpy as np
import pandas as pd

index = pd.Index(data=["Tom", "Bob", "Mary", "James"], name="name")

data = {
    "age": [18, 30, 25, 40],
    "city": ["BeiJing", "ShangHai", "GuangZhou", "ShenZhen"]
}

user_info = pd.DataFrame(data=data, index=index)
print(user_info)
# 先构建一个二维数组，然后再生成一个列名称列表。
data = [[18, "BeiJing"],
        [30, "ShangHai"],
        [25, "GuangZhou"],
        [40, "ShenZhen"]]
columns = ["age", "city"]

user_info = pd.DataFrame(data=data, index=index, columns=columns)
print(user_info)

# 访问行

print(user_info.loc["Tom"],user_info.iloc[1:3],user_info["age"])