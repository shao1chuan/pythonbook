import pandas as pd
import plotly.express as px

df = pd.read_csv("p.csv")

fig = px.line(df, x="x", y="y", color="type", title="A Plotly Express Figure")
# If you print the figure, you'll see that it's just a regular figure with data and layout
# print(fig)

fig.show()