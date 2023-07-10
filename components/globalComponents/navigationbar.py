from dash import html
import dash_bootstrap_components as dbc

navigation_bar = html.Div(
    dbc.NavbarSimple([
        # dbc.Button("About This App", id="open-offcanvas", n_clicks=0),
        dbc.NavLink('About This App', href='/home', active='exact', id='home-navlink'),
        # dbc.NavLink('Create User', href='/create', active='exact', id='create-navlink'),
        # dbc.NavLink("Track Plays", href="/tracking", id='track-navlink'
                    # ),
        dbc.NavLink("Interactive Dashboard", href="/dashboard", active='exact', id='dashboard-'
                    ),
        # dbc.Button("Logout", href='/login', id='logout-btn', disabled=True, outline=False)
    ],
        dark=True,
        color='primary',
        brand='Tracking Assists App',
        brand_href='#',
        className='py-lg-0',
    )
)