from dash import html, dcc
import dash_bootstrap_components as dbc

period_dropdown = html.Div([
    dbc.DropdownMenu([
        dcc.Checklist(
            id='quarter-filter',
            options=[
                {'label': '1st Quarter', 'value': 1},
                {'label': '2nd Quarter', 'value': 2},
                {'label': '3rd Quarter', 'value': 3},
                {'label': '4th Quarter', 'value': 4},
            ],
            value=[1, 2, 3, 4],
            labelStyle={'display': 'block'},
            inputStyle={"margin-right": "5px"},
            className='ml-1'
        ),
    ],
        id='quarter-dropdown',
        direction="up",
        label="All Period Filters Selected",
        color="black",
        className='mb-1 d-block',
        toggle_style={'width': '100%'}
    )],
),