from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import json

fig = px.line(
    x=["a","b","c"], y=[1,3,2], # replace with your own data source
    title="sample figure", height=325
)

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Displaying figure structure as JSON'),
    dcc.Graph(id="graph", figure=fig),
    dcc.Clipboard(target_id="structure"),
    html.Pre(
        id='structure',
        style={
            'border': 'thin lightgrey solid',
            'overflowY': 'scroll',
            'height': '275px'
        }
    ),
])


@app.callback(
    Output("structure", "children"),
    Input("graph", "figure"))
def display_structure(fig_json):
    return json.dumps(fig_json, indent=2)


app.run_server(debug=True)