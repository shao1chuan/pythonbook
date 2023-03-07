
import pandas as pd

import plotly.express as px

df_demo = px.data.iris()
# print(df_demo.mean(),df_demo.max(),df_demo.quantile(0.75))

# 此外，需要介绍的是 quantile, count, idxmax 这三个函数，它们分别返回的是
# 分位数、
# 非缺失值个数、
# 最大值对应的索引

print("mena",df_demo.mean(axis=1).head())
#
df_demo = df_demo[['sepal_length','sepal_width','petal_length']]
print(df_demo.drop_duplicates(['sepal_length', 'sepal_width']))



