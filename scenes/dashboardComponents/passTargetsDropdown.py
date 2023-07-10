from dash import html, dcc
import dash_bootstrap_components as dbc

pass_targets_dropdown = html.Div([
    dbc.DropdownMenu([
        dcc.Checklist(
            id='pass-target-filter',
            options=[],
            value=[],
            labelStyle={'display': 'block'},
            inputStyle={"margin-right": "5px"},
            style={"overflow-y": "scroll", "height": "200px"},
            className='ml-1'
        ),
    ],
        id='pass-target-dropdown',
        direction="up",
        label="All Pass Targets Selected",
        color="black",
        className='mb-1',
        toggle_style={'width': '100%'},
    )],
)