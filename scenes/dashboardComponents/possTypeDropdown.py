from dash import html, dcc
import dash_bootstrap_components as dbc

possession_dropdown = html.Div([
    dbc.DropdownMenu([
        dcc.Checklist(
            id='possession-filter',
            options=[
                {'label': 'Off FT Miss', 'value': 'OffFTMiss'},
                {'label': 'Off FT Make', 'value': 'OffFTMake'},
                {'label': 'Off Arc3 Miss', 'value': 'OffArc3Miss'},
                {'label': 'Off Arc3 Make', 'value': 'OffArc3Make'},
                {'label': 'Off Arc3 Block', 'value': 'OffArc3Block'},
                {'label': 'Off Corner3 Miss', 'value': 'OffCorner3Miss'},
                {'label': 'Off Corner3 Make', 'value': 'OffCorner3Make'},
                {'label': 'Off Corner3 Block', 'value': 'OffCorner3Block'},
                {'label': 'Off At Rim Miss', 'value': 'OffAtRimMiss'},
                {'label': 'Off At Rim Make', 'value': 'OffAtRimMake'},
                {'label': 'Off At Rim Block', 'value': 'OffAtRimBlock'},
                {'label': 'Off Short Midrange Miss', 'value': 'OffShortMidRangeMiss'},
                {'label': 'Off Short Midrange Make', 'value': 'OffShortMidRangeMake'},
                {'label': 'Off Short Midrange Block', 'value': 'OffShortMidRangeBlock'},
                {'label': 'Off Long Midrange Miss', 'value': 'OffLongMidRangeMiss'},
                {'label': 'Off Long Midrange Make', 'value': 'OffLongMidRangeMake'},
                {'label': 'Off Long Midrange Block', 'value': 'OffLongMidRangeBlock'},
                {'label': 'Off Timeout', 'value': "OffTimeout"},
                {'label': 'Off Live Ball Turnover', 'value': 'OffLiveBallTurnover'},
                {'label': 'Off Deadball', 'value': 'OffDeadball'}
            ],
            value=['OffFTMiss', 'OffFTMake', 'OffArc3Miss', 'OffArc3Make', 'OffArc3Block',
                    'OffCorner3Miss', 'OffCorner3Make', 'OffCorner3Block',
                    'OffAtRimMiss', 'OffAtRimMake', 'OffAtRimBlock',
                    'OffShortMidRangeMiss', 'OffShortMidRangeMake', 'OffShortMidRangeBlock',
                    'OffLongMidRangeMiss', 'OffLongMidRangeMake', 'OffLongMidRangeBlock',
                    'OffTimeout', 'OffLiveBallTurnover', 'OffDeadball'],
            labelStyle={'display': 'block'},
            inputStyle={"margin-right": "5px"},
            style={"overflow-y": "scroll", "height": "200px"},
            className='ml-1'
        ),
    ],
        id='possession-dropdown',
        direction="up",
        label="All Possession-Types Selected",
        color="black",
        className='mb-1',
        toggle_style={'width': '100%'}
    )],
)