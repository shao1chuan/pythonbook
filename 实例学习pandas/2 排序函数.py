
import pandas as pd

df = pd.read_csv('..\data\learn_pandas.csv')
df_demo = df[['Grade', 'Name', 'Height','Weight']].set_index(['Grade','Name'])
a1 = df_demo.sort_values('Height').head()
print(a1)

