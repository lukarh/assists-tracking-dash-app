from dash import html, dcc, dash_table
from dash_table import FormatTemplate

from datetime import date, datetime

import dash_daq as daq
import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objects as go

############################################################################################

from .dashboardComponents.playerImage import player_image
from .dashboardComponents.playerDropdown import player_dropdown
from .dashboardComponents.dateFilter import date_filter
from .dashboardComponents.shotclockFilter import shotclock_filter
from .dashboardComponents.minuteFilter import minute_filter
from .dashboardComponents.passFilter import pass_filter
from .dashboardComponents.shottypeDropdown import shottype_dropdown
from .dashboardComponents.csDropdown import cs_dropdown
from .dashboardComponents.periodDropdown import period_dropdown
from .dashboardComponents.passTargetsDropdown import pass_targets_dropdown
from .dashboardComponents.possTypeDropdown import possession_dropdown
from .dashboardComponents.teamDropdown import team_dropdown
from .dashboardComponents.passDirectionDropdown import pass_direction_dropdown

############################################################################################

from .utils.drawPlotlyCourts import draw_plotly_court

############################################################################################

# create plotly figure, draw court, and create container for the court figure
display_fig = go.Figure()
draw_plotly_court(display_fig, show_title=False, labelticks=False, show_axis=False,
                  glayer='above', bg_color='white', margins=0)
display_graph = dcc.Graph(
    id='display-graph',
    figure=display_fig,
    config={'staticPlot': False,
            'scrollZoom': False,
            },
)

# create plotly figure polar bar graphs, set initial values of theming and colors, and create container for the graphs
dist_fig = px.bar_polar(template="ggplot2",
                        color_discrete_sequence=['#67001f', '#bb2a34', '#e58368', '#fbceb6', '#f7f7f7',
                                                 '#c1ddec', '#6bacd1', '#2a71b2', '#053061'],
                        )

shottype_fig = px.bar_polar(template="ggplot2",
                            color_discrete_sequence=['#67001f', '#bb2a34', '#e58368', '#fbceb6', '#f7f7f7',
                                                     '#c1ddec', '#6bacd1', '#2a71b2', '#053061'],
                            )

rose_plot = dcc.Graph(
    id='rose-plot',
    figure=dist_fig,
    config={'staticPlot': False,
            'scrollZoom': False},
)

# create plotly figure line plot, set initial values of theming and colors, and create container for the line plot

line_fig = go.Figure()
line_fig.update_layout(
        font_color='black',
        plot_bgcolor='white',
        title='When in the Shotclock does %s find opportunities for assists?' % '(Insert Player Name)',
)

line_plot = dcc.Graph(
    id='line-plot',
    figure=line_fig,
    config={'staticPlot': False,
            'scrollZoom': False}
)

# create plotly figure sankey plot, set initial values of theming and colors, and create container for the sankey plot
sankey_fig = go.Figure()
sankey_fig.update_layout(
        font_color='black',
        plot_bgcolor='white',
        title='Who does %s connect with the most for assists?' % '(Insert Player Name)',
)

sankey_plot = dcc.Graph(
    id='sankey-plot',
    figure=line_fig,
    config={'staticPlot': False,
            'scrollZoom': False}
)

dashboard_page = dbc.Container([
    dcc.Store(id='player-options', storage_type='memory', data=[]),
    dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Video Playback of Chosen Assist",
                                           id='modal-title'
                                           )
                            ),
            html.Center([
                html.Video(
                    id='video-playback-modal',
                    controls=True,
                    src='',
                    loop='loop',
                    autoPlay=False,
                    width='100%',
                    height='100%'
                ),
            ]),
        ],
        id="video-modal",
        size="xl",
        is_open=False,
    ),
    dbc.Row([
        #########################################
        #### FIRST COLUMN OF DASHBOARD PAGE ####
        dbc.Col([
            html.H4("Pick A Passer",
                    className='mt-2 text-center',
                    style={'font=size': '14px'}),
            html.Hr(className="my-2"),
            player_image,
            player_dropdown,
            html.H5("Select Filters:", className='mt-2 text-center'),
            html.Hr(className="my-2"),
            pass_filter,
            html.P("Date Filter:", className='mt-2 mb-1 text-left'),
            date_filter,
            html.P("Time Range on Shotclock:", className='mt-2 mb-2 text-left'),
            shotclock_filter,
            html.P("Time Range in Quarter:", className='mt-2 mb-2 text-left'),
            minute_filter,
            html.P("Game Detail Filters:", className='mt-2 mb-1 text-left'),
            period_dropdown[0],
            shottype_dropdown,
            team_dropdown,
            pass_targets_dropdown,
            pass_direction_dropdown,
            cs_dropdown,
            possession_dropdown,
        ],
            width=2,
            className='ml-0 mr-0',
        ),
        #########################################

        #########################################
        #### SECOND COLUMN OF DASHBOARD PAGE ####
        dbc.Col([
            html.Div([
                display_graph,
            ])
        ],
            width=3,
            style={'margin-right': '0px',
                   'margin-left': '0px'
                   },
        ),
        #########################################

        #########################################
        #### THIRD COLUMN OF DASHBOARD PAGE ####
        dbc.Col([
            rose_plot,
            line_plot,
        ],
            width=5,
            style={'margin-right': '0px',
                   'margin-left': '0px'
                   },
        ),
        #########################################

        #########################################
        #### FOURTH COLUMN OF DASHBOARD PAGE ####
        dbc.Col([
            html.H5("How do I interpret these visuals?",
                    className='mt-3 text-center', style={'fontWeight': 'bold', 'fontSize': '18px'}),
            html.Hr(className="my-2"),
            html.P("1. Contour Court Heatmap of Assists", style={'fontWeight': 'bold'}, className='mb-1'),
            html.P("This contour map shows density contours on the court for where a player frequently passes the ball "
                   "from or to. The darker the color, the more frequently the player finds themselves having success getting an assist at. ", 
                   style={'fontSize': '14px'}, className='mb-0'
                   ),
            html.P("2. Rose Plot of Passing Tendencies", style={'fontWeight': 'bold'}, className='mb-1'),
            html.P([
                "A rose plot, inspired by ",
                html.A("wind roses used in meteorology", href="https://www.climate.gov/maps-data/dataset/wind-roses-charts-and-tabular-data"),
                ", express a player's directional passing tendencies on assist plays with the frame of reference being the hoop due South. "
                "Every assist is associated with a vector that indicates where the pass was thrown initially and caught. "
                "The magnitude of each 'rose' is determined by the number of vectors/passes in that direction. "
                ], style={'fontSize': '14px'}, className='mb-0'),
            html.P("3. Line Plot Comparison of Shotclock", style={'fontWeight': 'bold'}, className='mb-1'),
            html.P("The line plot compares how X player finds opportunities for assists during the shotclock versus other players.", 
                   style={'fontSize': '14px'}, className='mb-0'),
            html.P("4. Sankey Flow Diagram of Assists", style={'fontWeight': 'bold'}, className='mb-1'),
            html.P(
                "The Sankey Flow Diagram gives a macro-overview for how all of X player's assists is distributed "
                "amongst his teammates and the shot-type generated.", 
                style={'fontSize': '14px'}, className='mb-0'
            ),
            html.Hr(className="my-2"),
            html.P(
                "Graph Options",
                className='text-center'
            ),
            daq.ToggleSwitch(id='rose-toggle',
                             label='Rose Plot by Pass Distance',
                             labelPosition='top',
                             className='mb-2',
                             value = True,
                             ),
            daq.BooleanSwitch(id='tooltips-toggle', on=True,
                              label='Tooltips are On',
                              labelPosition='top',
                              className='mb-2',
                              color='green',
                              ),
            html.Hr(className="my-2"),
            dbc.Button("Show Video of Play",
                       id='open-modal-btn',
                       style={'width': '100%'},
                       ),
            dbc.Tooltip(
                "Click on a Scatter Point on the Court before clicking this button to view video of the play. ",
                target="open-modal-btn",
                placement="top"
            ),
            html.Hr(className="my-2",
                    style={'color': 'black'}),
        ],
            width=2,
            style={'margin-right': '0px',
                   'margin-left': '0px',},
        ),
        #########################################
    ]),
    dbc.Row([
        dbc.Col([
            sankey_plot
        ], 
        width=6
        ),
        dbc.Col([
            html.H5("Assist Stat Breakdown by Player and Type",
                    className='mt-4 mb-4 text-center'),
            dash_table.DataTable(
                id='assist-shottypes-table',
                columns=[
                    dict( id='Player', name='Player' ),
                    dict( id='No. Tracked Asts', name='No. Tracked Asts' ),
                    dict( id='% of Rim Asts', name='% of Rim Asts', type='numeric', format=FormatTemplate.percentage(1) ),
                    dict( id='% of Short Midrange Asts', name='% of Short Midrange Asts', type='numeric', format=FormatTemplate.percentage(1) ),
                    dict( id='% of Long Midrange Asts', name='% of Long Midrange Asts', type='numeric', format=FormatTemplate.percentage(1) ),
                    dict( id='% of Corner 3 Asts', name='% of Corner 3 Asts', type='numeric', format=FormatTemplate.percentage(1) ),
                    dict( id='% of Arc 3 Asts', name='% of Arc 3 Asts', type='numeric', format=FormatTemplate.percentage(1) ),
                    dict( id='% of High EV Asts', name='% of High EV Asts', type='numeric', format=FormatTemplate.percentage(1) ),
                    dict( id='% of Asts thrown from the Paint', name='% of Asts thrown from the Paint', type='numeric', format=FormatTemplate.percentage(1) )
                ],
                style_cell={
                    "fontFamily": "Ubuntu", 
                    "fontSize": "12px", 
                    "width": "75px",
                    "whiteSpace": "nowrap",
                    "textAlign": "center",
                    "border": 'none' 
                },
                style_header={
                    "height": "50px",
                    "whiteSpace": "normal",
                    "backgroundColor": "rgb(245,245,245)",
                    "fontWeight": "bold"
                },
                style_data_conditional=[
                    {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': 'rgb(250,250,250)',
                    }
                ],
                style_table={'border': 'none'},
                cell_selectable=False,
                sort_action='native'
            )
        ], 
        width=6,
        style={'paddingRight': '5rem'}
        )
    ])
], fluid=True)
