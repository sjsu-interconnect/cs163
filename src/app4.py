import dash

import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
application = app.server
# app.layout = html.Div("Hello User")
#
# if __name__ == '__main__':
#     app.run_server(debug=True)



