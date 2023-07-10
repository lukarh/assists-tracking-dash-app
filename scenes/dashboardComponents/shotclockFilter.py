from dash import dcc

shotclock_filter = dcc.RangeSlider(
    id='shotclock-filter',
    min=0, max=24,
    step=1, value=[0, 24],
    allowCross=False,
    marks={
        0: '0s', 6: '6s',
        12: '12s', 18: '18s',
        24: '24s',
    },
    updatemode='drag',
    className='dashboard-range-slider'
)