import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="A Plotly Express Figure")
# If you print the figure, you'll see that it's just a regular figure with data and layout
# print(fig)

fig.show()