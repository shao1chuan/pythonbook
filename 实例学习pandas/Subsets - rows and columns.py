import plotly.express as px

df = px.data.iris()
print(df.head(10))

# df = px.data.wind()
# print(df.head(10))
#
# df = px.data.carshare()
# print(df.head(10))
# fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="A Plotly Express Figure")
# # If you print the figure, you'll see that it's just a regular figure with data and layout
# # print(fig)
#
# fig.show()

# print(df.iloc[10:20])
# print(df.sample(frac=0.01))
# print(df.nlargest(10,'sepal_width'))
# print(df.loc[df['sepal_width'] > 3, ['sepal_width', 'petal_length']])
print(df.iat[1, 3])
