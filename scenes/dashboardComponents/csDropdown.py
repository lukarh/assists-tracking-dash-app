from dash import html, dcc
import dash_bootstrap_components as dbc

cs_dropdown = html.Div([
    dbc.DropdownMenu([
        dcc.Checklist(
            id='cs-filter',
            options=[
                {'label': 'Catch and Shoot', 'value': True},
                {'label': 'Non-Catch and Shoot', 'value': False},
            ],
            value=[True, False],
            labelStyle={'display': 'block'},
            inputStyle={"margin-right": "5px"},
            className='ml-1'
        ),
    ],
        id='cs-dropdown',
        direction="up",
        label='C&S and Non-C&S Shots Selected',
        color="black",
        className='mb-1',
        style={'width': '100%'},
        toggle_style={'width': '100%'}
    )],
)