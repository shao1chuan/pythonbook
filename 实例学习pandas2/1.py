import pandas as pd

chipo = pd.read_csv("chipotle.tsv", sep = '\t')
print(chipo.head(10),chipo.shape[1])

c = chipo[['item_name','quantity']].groupby(['item_name'],as_index=False).agg({'quantity':sum})

c.sort_values(['quantity'],ascending=False,inplace=True)

c.head()

