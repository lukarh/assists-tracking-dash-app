from dash import dcc 

pass_filter = dcc.RadioItems(
    id='pass-detail-filter',
    options=[
        {'label': "Pass Origin", 'value': 'pass_'},
        {'label': "Pass Target", 'value': 'pass_rec_'}
    ],
    value='pass_',
    labelStyle={"margin-right": "5px"},
    inputStyle={"margin-right": "5px"},
    style={'display': 'flex', 'flexDirection': 'row'}
)