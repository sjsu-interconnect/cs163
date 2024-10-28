import dash
from dash import Dash, html, dash_table, dcc, Input, Output, callback, page_container
import plotly.express as px

app = Dash(__name__, use_pages=True)

app.layout = html.Div(
    [
        html.Div([
            dcc.Link(f'{page['name']}', href=page(['relative_path'])
            ) for page in dash.page_registry.values()
        ]),
        dash.page_container
    ]
)

if __name__ == '__main__':
    app.run(debug=True)