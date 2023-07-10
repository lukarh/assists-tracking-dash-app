from dash import html, dcc
import dash_bootstrap_components as dbc

pass_direction_dropdown = html.Div([
    dbc.DropdownMenu([
        dcc.Checklist(
            id='pass-direction-filter',
            options=[
                {'label': 'N', 'value': 'N'},
                {'label': 'NEN', 'value': 'NEN'},
                {'label': 'NE', 'value': 'NE'},
                {'label': 'ENE', 'value': 'ENE'},
                {'label': 'E', 'value': 'E'},
                {'label': 'ESE', 'value': 'ESE'},
                {'label': 'SE', 'value': 'SE'},
                {'label': 'SES', 'value': 'SES'},
                {'label': 'S', 'value': 'S'},
                {'label': 'SWS', 'value': 'SWS'},
                {'label': 'SW', 'value': 'SW'},
                {'label': 'WSW', 'value': 'WSW'},
                {'label': 'W', 'value': 'W'},
                {'label': 'WNW', 'value': 'WNW'},
                {'label': 'NW', 'value': 'NW'},
                {'label': 'NWN', 'value': 'NWN'},
            ],
            value=['N','NEN','NE','ENE','E','ESE','SE','SES',
                   'S','SWS','SW','WSW','W','WNW','NW','NWN'],
            labelStyle={'display': 'block'},
            inputStyle={"margin-right": "5px"},
            style={"overflow-y": "scroll", "height": "200px"},
            className='ml-1'
        ),
    ],
        id='pass-direction-dropdown',
        direction="up",
        label="All Pass Directions Selected",
        color="black",
        className='mb-1',
        toggle_style={'width': '100%'},
        style={'borderColor': 'black'}
    )],
)