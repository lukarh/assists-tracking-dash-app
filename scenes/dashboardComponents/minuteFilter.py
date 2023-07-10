from dash import dcc

minute_filter = dcc.RangeSlider(
    id='time-filter',
    min=0,
    max=720,
    step=1,
    value=[0, 720],
    allowCross=False,
    marks={
        0: '0:00',
        180: '3:00',
        360: '6:00',
        540: '9:00',
        720: '12:00',
    },
    updatemode='drag',
    className='dashboard-range-slider'
)