from dash import html, dcc
import dash_bootstrap_components as dbc

shottype_dropdown = html.Div([
    dbc.DropdownMenu([
        dcc.Checklist(
            id='shottype-filter',
            options=[
                {'label': 'Arc 3', 'value': 'Arc3'},
                {'label': 'Corner 3', 'value': 'Corner3'},
                {'label': 'Short Midrange', 'value': 'ShortMidRange'},
                {'label': 'Long Midrange', 'value': 'LongMidRange'},
                {'label': 'Rim', 'value': 'AtRim'}
            ],
            value=['Arc3', 'Corner3', 'ShortMidRange',
                    'LongMidRange', 'AtRim'],
            labelStyle={'display': 'block'},
            inputStyle={"margin-right": "5px"},
            className='ml-1'
        ),
    ],
        id='shottype-dropdown',
        direction="up",
        label="All Shot Types Selected",
        color="black",
        className='mb-1 mb-1 mw-100',
        style={'width': '100%'},
        toggle_style={'width': '100%'}
    )],
)

