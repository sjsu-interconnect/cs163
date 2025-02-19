from dash import Dash, html

app = Dash()

app.layout = html.Div([
    html.H1('Hello Dash'),
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
    ])
])

if __name__ == '__main__':
    app.run(debug=True)
