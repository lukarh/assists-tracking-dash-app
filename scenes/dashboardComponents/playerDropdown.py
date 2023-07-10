from dash import dcc

player_dropdown = dcc.Dropdown(
    id='player-select', multi=False, placeholder='Select Player...',
    options=[],
    searchable=True,
    clearable=False,
    value=1629636,
    persistence=True,
    className='mb-3'
)