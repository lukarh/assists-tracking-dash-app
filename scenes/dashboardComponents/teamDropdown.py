from dash import html, dcc
import dash_bootstrap_components as dbc

team_dropdown = html.Div([
    dbc.DropdownMenu([
        dcc.Checklist(
            id='opp-team-filter',
            value=[],
            persistence=True,
            labelStyle={'display': 'block', },
            inputStyle={"margin-right": "5px", },
            style={"overflow-y": "scroll", "height": "200px",
                    "width": "100%"},
            className='ml-1',
        ),
    ],
        id='opp-team-dropdown',
        direction="up",
        label="30 of 30 Teams Selected",
        color="black",
        className='mb-1',
        toggle_style={'width': '100%'},
        style={'width': '100%'}
    )],
    style={'width': '100%'}
)