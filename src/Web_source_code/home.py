from dash import html
from Nav_bar import create_navbar

nav = create_navbar()

header = html.H3('Here is Home')

def create_page_home():
    layout = html.Div([
        nav,
        header,
    ])
    return layout