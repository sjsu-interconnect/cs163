import dash_bootstrap_components as dbc

def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label='Menu',
                children=[
                    dbc.DropdownMenuItem("Home", href="/"),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem('Proposals', href="/proposals"),
                    dbc.DropdownMenuItem('Data Processing', href="/processing")
                ]
            )
        ],
        brand="Home",
        brand_href="/",
        sticky='top',
        color="dark",
        dark=True
    )
    return navbar