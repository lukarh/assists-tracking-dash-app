from dash import dcc
from datetime import date, datetime

date_filter = dcc.DatePickerRange(
    id='date-filter',
    display_format='MMM Do, Y',
    min_date_allowed=date(2020, 12, 1),
    max_date_allowed=date(2030, 7, 1),
    initial_visible_month=date(2020, 12, 1),
    start_date=date(2020, 12, 1),
    end_date=date(2030, 7, 1)
)