from dash import Dash, html, dash_table, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

df = pd.read_csv('/Users/eddie/cs163/src/Data/CPI_Processed_data.csv')
app = Dash()

app.layout = html.Div(
    [
        html.H1('Hello Dash', style={'textAlign': 'center', 'fontWeight': 'bold', 'fontSize': '20px', 'color': 'red', 'font-family': 'Arial'}),
        html.Div([
            # html.P('Hello my guys!'),
            # html.P('Dash converts Python classes into HTML'),
            # dash_table.DataTable(data=df.to_dict('records'), page_size=10),
            # dcc.Graph(figure=fig),
            # dcc.Graph(figure=fig2),
            dcc.RadioItems(
                options=[
                    {'label': 'CPI', 'value': 'CPI'},
                    {'label': 'Rate of Change', 'value': 'rate_of_change'}],
                id='control-radioitems',
                value='CPI',
                inline=True),
            dcc.Graph(figure={}, id='control-graph')
        ])
    ]
)

## Decorator
@app.callback(
    Output(component_id='control-graph', component_property='figure'),
    Input(component_id='control-radioitems', component_property='value')
)
def update_graph(column):
    fig = fig = px.line(df, x='date', y=column, title='Timeseries of CPI Monthly', labels={'date': 'Year'})
    return fig

if __name__ == '__main__':
    app.run(debug=True)