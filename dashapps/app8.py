import dash_bootstrap_components as dbc
from dash import Dash, html


# https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        dbc.Row(dbc.Col(html.Div("A single column"))),
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
            ]
        ),
    ]
)


if __name__ == '__main__':
    app.run(debug=True)