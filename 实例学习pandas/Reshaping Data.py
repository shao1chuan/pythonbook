import  pandas as pd

df = pd.DataFrame(
{"x" : [0],
"y" : [1],
 "type": "positionHuman"}
)

df1 = pd.DataFrame(
{"x" : [2],
"y" : [3],
 "type": "positionLion1"}
)
df = pd.concat([df,df1],axis=1)
print(df)
# df = df.pivot(columns='x', values='x')
# df = pd.melt(df)
# print("pivot",df)

