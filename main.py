import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

from itertools import product
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

import os
from dotenv import load_dotenv

import dash
import dash_bootstrap_components as dbc

from dash import html, dcc, callback_context
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State

############################################################################################

from scenes.home import home_page
from scenes.dashboard import dashboard_page, display_fig, rose_plot

from components.globalComponents.navigationbar import navigation_bar

############################################################################################

from scenes.utils.drawPlotlyCourts import draw_plotly_court

############################################################################################

distances = ['0-10 ft.', '10-20 ft.', '20-30 ft.', '30-40 ft.',
             '40-50 ft.', '50-60 ft.', '60-70 ft.', '70-80 ft.', '80-90 ft.']
shottypes = ['AtRim', 'ShortMidRange', 'LongMidRange',
             'Arc3', 'Corner3']
directions = ['N', 'NEN', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SES',
              'S', 'SWS', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NWN']

############################################################################################

load_dotenv()

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.UNITED],
                suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}],
                )
server = app.server

server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# server.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
server.config["SQLALCHEMY_DATABASE_URI"] = os.environ["HEROKU_POSTGRESQL_ORANGE_URL"]

db = SQLAlchemy(server)

#############################################################################################

content = html.Div(id='page-content', children=[home_page])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navigation_bar,
    content
])

@app.callback(
    Output(component_id='page-content', component_property='children'),
    Input(component_id='url', component_property='pathname')
)
def render_page_content(pathname):
    if pathname == '/home':
        return home_page
    elif pathname == '/dashboard':
        return dashboard_page
    else:
        return html.Div(
            dbc.Container(
                [
                    html.H1("404: Not found", className="text-danger"),
                    html.Hr(),
                    html.P(f"The pathname {pathname} was not recognised..."),
                ],
                fluid=True,
                className="py-3",
            ),
            className="p-3 bg-light rounded-3",
        )

######################################################################################
############################ Dashboard Callback Functions ############################
######################################################################################

@app.callback(
    Output(component_id='player-image', component_property='src'),
    Input(component_id='player-select', component_property='value')
)
def update_image(pid):
    return 'https://cdn.nba.com/headshots/nba/latest/1040x760/%d.png' % pid

@app.callback(
    Output(component_id='player-select', component_property='options'),
    Input(component_id='player-options', component_property='data'),
)
def update_player_options(player_options):
    return player_options

@app.callback(
    Output(component_id='player-options', component_property='data'),
    Input(component_id='player-options', component_property='data'),
)
def get_player_options(data):
    players_df = pd.read_sql_query("SELECT DISTINCT assistplayerid, assist_player FROM nbatrackingdata", con=db.engine)
    players_df = players_df.rename(columns={'assist_player': 'label','assistplayerid': 'value'})
    players_df = players_df[['label', 'value']].sort_values('label').reset_index(drop=True)
    player_options = players_df.to_dict('records')

    return player_options

@app.callback(
    # Output(component_id='stored-player-data', component_property='data'),
    Output(component_id='opp-team-filter', component_property='options'),
    Output(component_id='opp-team-filter', component_property='value'),
    Output(component_id='pass-target-filter', component_property='options'),
    Output(component_id='pass-target-filter', component_property='value'),
    Input(component_id='player-select', component_property='value')
)
def update_player_data(pid):
    player_df = pd.read_sql_query("SELECT * FROM nbatrackingdata WHERE assistplayerid = %s" % (pid), con=db.engine)

    teamids_df = pd.DataFrame(player_df.groupby(['defense_team_id','opponent']).size(
    ).reset_index().rename(columns={0: 'count',
                                    'opponent': 'label',
                                    'defense_team_id': 'value'}))

    teamids_df = teamids_df[['label', 'value']].sort_values('label').reset_index(drop=True)
    team_options = teamids_df.to_dict('records')

    targets_df = pd.DataFrame(player_df.groupby(['playerid', 'player']).size(
    ).reset_index().rename(columns={0: 'count',
                                    'player': 'label',
                                    'playerid': 'value'}))
    targets_df = targets_df[['label', 'value']].sort_values('label').reset_index(drop=True)
    target_options = targets_df.to_dict('records')

    return team_options, [team['value'] for team in team_options], target_options, [player['value'] for player in target_options] #player_df.to_dict('records'),

########################### Update Dropdown Label Functions ###########################

@app.callback(
    Output(component_id='quarter-dropdown', component_property='label'),
    Input(component_id='quarter-filter', component_property='value'),
)
def update_period_dropdown_label(period_filter):
    if len(period_filter) == 4:
        return 'All Quarters Selected'
    elif len(period_filter) == 0:
        return 'No Quarters Selected'
    else:
        return '%d Quarters Selected' % len(period_filter)
    
@app.callback(
    Output(component_id='shottype-dropdown', component_property='label'),
    Input(component_id='shottype-filter', component_property='value')
)
def update_shottype_dropdown(shottype_filter):
    if len(shottype_filter) == 5:
        return 'All Shot Types Selected'
    else:
        return '%d of 5 Shot Types Selected' % len(shottype_filter)

@app.callback(
    Output(component_id='opp-team-dropdown', component_property='label'),
    Input(component_id='opp-team-filter', component_property='value'),
    State(component_id='opp-team-filter', component_property='options')
)
def update_team_dropdown_label(opp_team_filter, team_options):
    return '%d of %d Teams Selected' % (len(opp_team_filter), len(team_options))
    
@app.callback(
    Output(component_id='pass-target-dropdown', component_property='label'),
    Input(component_id='pass-target-filter', component_property='value'),
    State(component_id='pass-target-filter', component_property='options')
)
def update_pass_target_dropdown_label(pass_target_filter, target_options):
    return '%d of %d Pass Targets Selected' % (len(pass_target_filter), len(target_options))

@app.callback(
    Output(component_id='pass-direction-dropdown', component_property='label'),
    Input(component_id='pass-direction-filter', component_property='value'),
    Input(component_id='pass-direction-filter', component_property='options')
)
def update_pass_direction_dropdown_label(pass_direction_filter, directions_options):
    return '%d of %d Pass Directions Selected' % (len(pass_direction_filter), len(directions_options))

@app.callback(
    Output(component_id='cs-dropdown', component_property='label'),
    Input(component_id='cs-filter', component_property='value'),
)
def update_catchshoot_dropdown_label(csshot_filter):
    if len(csshot_filter) == 2:
        return 'All Catch & Shoot Types Selected'
    elif csshot_filter == ['CS']:
        return 'Catch & Shoot Shots Selected'
    elif csshot_filter == ['NoCS']:
        return 'Non-Catch & Shoot Shots Selected'
    else: 
        return 'No Catch&Shoot Type Selected'

@app.callback(
    Output(component_id='possession-dropdown', component_property='label'),
    Input(component_id='possession-filter', component_property='value'),
)
def update_possession_dropdown_label(possession_filter):
    return "%d of 20 Possession Types Selected" % len(possession_filter)

####################################################################################
############################### COURT HEATMAP FIGURE ###############################
####################################################################################

@app.callback(
    Output(component_id='display-graph', component_property='figure'),
    Output(component_id='rose-plot', component_property='figure'),
    # Input(component_id='stored-player-data', component_property='data'),
    Input(component_id='pass-detail-filter', component_property='value'),
    # Input(component_id='display-graph', component_property='clickData'),
    Input(component_id='tooltips-toggle', component_property='on'),
    Input(component_id='rose-toggle', component_property='value'),
    Input(component_id='shotclock-filter', component_property='value'),
    Input(component_id='time-filter', component_property='value'),
    Input(component_id='pass-target-filter', component_property='value'),
    Input(component_id='shottype-filter', component_property='value'),
    Input(component_id='opp-team-filter', component_property='value'),
    Input(component_id='cs-filter', component_property='value'),
    Input(component_id='quarter-filter', component_property='value'),
    Input(component_id='possession-filter', component_property='value'),
    Input(component_id='pass-direction-filter', component_property='value'),
    Input(component_id='date-filter', component_property='start_date'),
    Input(component_id='date-filter', component_property='end_date'),
    Input(component_id="player-select", component_property="value"),
)
def update_display_graph(pass_detail, isTooltips_on, rosetype_toggle, 
                        shotclock_filter, time_filter, target_filter,
                        shottype_filter, opp_team_filter, ncs_filter, quarter_filter,
                        possession_filter, direction_filter, start_date, end_date, pid):
    def calc_vector_pts(x1, x2, y1, y2):
        m = (y2 - y1) / (x2 - x1)
        b = y1 - (m * x1)
        x = np.linspace(x1, x2, 250)
        y = m * x + b
        return x, y
    
    def create_sql_query():
        query = "SELECT * FROM nbatrackingdata WHERE assistplayerid = %s" % (pid)

        query += " AND pass_shotclock BETWEEN %d AND %d" % (shotclock_filter[0], shotclock_filter[1])

        opponents_str = ', '.join(["'%s'" % opp for opp in opp_team_filter])
        query += " AND defense_team_id IN (%s)" % opponents_str

        shottype_str = ', '.join(["'%s'" % shottype for shottype in shottype_filter])
        query += " AND shottype IN (%s)" % shottype_str

        quarter_str = ', '.join(["'%s'" % period for period in quarter_filter])
        query += " AND period IN (%s)" % quarter_str

        targets_str = ', '.join(["'%s'" % target for target in target_filter])
        query += " AND playerid IN (%s)" % targets_str

        possession_str = ', '.join(["'%s'" % possessiontype for possessiontype in possession_filter])
        query += " AND possession_start_type IN (%s)" % possession_str

        direction_str = ', '.join(["'%s'" % direction for direction in direction_filter])
        query += " AND direction IN (%s)" % direction_str
        
        if len(ncs_filter) == 1:
            query += " AND catch_and_shoot = %s" % ncs_filter[0]
        elif len(ncs_filter) == 0:
            query += " AND catch_and_shoot != True AND catch_and_shoot != False"

        return query
    
    def filter_date_and_time(player_df):
        player_df['date'] = pd.to_datetime(player_df['date'])
        player_df['time'] = player_df['time'].str.split(':').apply(lambda x: int(x[0]) * 60 + int(x[1]))
        filtered_df = player_df[(player_df['date'] > start_date) & (player_df['date'] <= end_date)]
        filtered_df = filtered_df[filtered_df['time'].between(time_filter[0], time_filter[1], inclusive='both')]
        filtered_df['time'] = pd.to_datetime(filtered_df["time"], unit='s').dt.strftime("%M:%S")
        filtered_df['date'] = filtered_df['date'].astype(str)
        
        return filtered_df
    
    def update_court_figure(display_fig, df):
        display_fig.data = [] 
        display_fig.add_trace(go.Histogram2dContour( 
            x=df['%sx' % pass_detail].to_list(),
            y=df['%sy' % pass_detail].to_list(),
            colorscale=['rgb(255, 255, 255)'] + px.colors.sequential.Magma[1:][::-1],
            xaxis='x2',
            yaxis='y2',
            showscale=False,
            line=dict(width=0),
            hoverinfo='none'
        ))
        display_fig.add_trace(go.Scatter(
            x=df['%sx' % pass_detail].to_list(),
            y=df['%sy' % pass_detail].to_list(),
            xaxis='x2',
            yaxis='y2',
            mode='markers',
            marker=dict(
                symbol='x',
                color='black',
                size=4
            ),
            name='Pass Origin' if pass_detail == 'pass_' else 'Pass Target',
            hoverinfo='none',
        ))

        tooltips_data = np.stack((df['shottype'], df['player'],
                                        df['period'], df['time'], df['date'],
                                        df['possession_start_type'], df['pass_distance'],
                                        df['pass_x'], df['pass_y'],
                                        df['pass_rec_x'], df['pass_rec_y'],
                                        df['assist_player'], df['team'],
                                        df['opponent'], df['video_url'],
                                        ), axis=-1)
        ##########################################################################################
        ######################### HOW TO ADD ANNOTATIONS TO SCATTER PLOT #########################
        # https://chart-studio.plotly.com/~empet/15366/customdata-for-a-few-plotly-chart-types/#/#
        ##########################################################################################
        display_fig.update_traces(
            customdata=tooltips_data,
            selector=dict(type='scatter'),
            hovertemplate="<b>Date:</b> %{customdata[4]}<br>" +
                            "<b>Time:</b> Q%{customdata[2]} | %{customdata[3]} left in the Quarter<br>" +
                            "<b>Player Assisted:</b> %{customdata[1]}<br>" +
                            "<b>Shot Type Created:</b> %{customdata[0]}<br>" +
                            "<b>Pass Distance:</b> %{customdata[6]} ft.<br>" +
                            "<b>Possession Start Type:</b> %{customdata[5]}<br>" if isTooltips_on else None
                            )
        return display_fig
    
    def process_data_for_rose_plot(df):
        distances_df = pd.DataFrame(product(directions, distances, [0]), columns=['Direction', 'Pass Distance', 'Frequency']) 
        shottypes_df = pd.DataFrame(product(directions, shottypes, [0]), columns=['Direction', 'Shot Type', 'Frequency'])

        distcounts_df = df.groupby(['direction', 'pass_dist_range']).size().reset_index()
        distcounts_df = distcounts_df.rename({
            'direction': 'Direction', 'pass_dist_range': 'Pass Distance', 0: 'Frequency 2'
        }, axis=1)
        shotcounts_df = df.groupby(['direction', 'shottype']).size().reset_index()
        shotcounts_df = shotcounts_df.rename({
            'direction': 'Direction', 'shottype': 'Shot Type', 0: 'Frequency 2'
        }, axis=1)
        distances_df = distances_df.merge(distcounts_df, on=['Direction', 'Pass Distance', ], how='left')
        distances_df['Frequency'] = np.max(distances_df[['Frequency', 'Frequency 2']], axis=1)
        distances_df = distances_df.drop(columns=['Frequency 2'])
        shottypes_df = shottypes_df.merge(shotcounts_df, on=['Direction', 'Shot Type'], how='left')
        shottypes_df['Frequency'] = np.max(shottypes_df[['Frequency', 'Frequency 2']], axis=1)
        shottypes_df = shottypes_df.drop(columns=['Frequency 2'])
        return distances_df, shottypes_df
    
    def update_rose_plot(distances_df, shottypes_df, rosetype_toggle):
        df = shottypes_df if not rosetype_toggle else distances_df
        distances_colors = ['#67001f', '#bb2a34', '#e58368', '#fbceb6', '#f7f7f7',
                            '#c1ddec', '#6bacd1', '#2a71b2', '#053061']
        shottype_colors = ['#b7e2ab', '#6fc9a3', '#46879c', '#3e5590', '#2c2037']
        rose_fig = px.bar_polar(df, r="Frequency", theta="Direction",
                               color='Shot Type' if not rosetype_toggle else 'Pass Distance',
                               template="ggplot2",
                               color_discrete_sequence=shottype_colors if not rosetype_toggle else distances_colors,
                               title="Passing Tendencies on Assists by %s" % (
                                   'Shot Type' if not rosetype_toggle else 'Pass Distance'),
                               )
        rose_fig.update_layout(legend_title_text='Shot Type Created' if not rosetype_toggle else 'Pass Distance Range',
                               font=dict(family='Ubuntu')
                               )
        return rose_fig

    query = create_sql_query()
    df = pd.read_sql_query(query, con=db.engine)
    df = filter_date_and_time(df)

    if len(df) != 0:
        new_display_fig = update_court_figure(display_fig, df)
        distances_df, shottypes_df = process_data_for_rose_plot(df)
        new_rose_fig = update_rose_plot(distances_df, shottypes_df, rosetype_toggle)
        return new_display_fig, new_rose_fig
    
    else:
        court_fig = go.Figure()
        draw_plotly_court(court_fig, show_title=False, labelticks=False, show_axis=False,
                            glayer='above', bg_color='white', margins=0)
        return court_fig

####################################################################################
################################# LINE PLOT FIGURE #################################
#################################################################################### 

@app.callback(
    Output(component_id='line-plot', component_property='figure'),
    Input(component_id='player-select', component_property='value'),
)
def update_lineplot(pid):
    bins = [0,4,7,15,18,24]
    group_names = ['Very Late','Late','Average','Early','Very Early',]
    shotclock_ranges = ['Very Late 4-0s','Late 7-4s','Average 15-7s','Early 18-15s','Very Early 24-18s']

    # declare new figure
    new_fig = go.Figure()
    results_df = pd.read_sql_query("SELECT * FROM nbatrackingdata", con=db.engine)

    # process data logic - calculate distribution of player's assist and entire sample's assist in shotclock ranges
    results_df['pass_shotclock_range'] = pd.cut(results_df['pass_shotclock'], bins, labels=group_names)
    shotclock_df = results_df[['assist_player','pass_shotclock_range']].groupby(by=['assist_player','pass_shotclock_range'])['pass_shotclock_range'].size() \
        .unstack(fill_value=0).stack().reset_index(name='count')
    shotclock_df['per_count'] = round(shotclock_df['count'] / shotclock_df.groupby('assist_player')['count'].transform('sum'), 3)
    sample_df = shotclock_df.groupby(by=['pass_shotclock_range'])['count'].sum().reset_index(name='count')
    sample_df['per_count'] = round(sample_df['count'] / sample_df['count'].sum(), 3)
    chosen_player = results_df[results_df['assistplayerid'] == pid]['assist_player'].to_list()[0]

    # plot every player's line plot except for the current chosen player
    for player in shotclock_df['assist_player'].unique():
        player_df = shotclock_df[shotclock_df['assist_player'] == player].reset_index(drop=True)
        values = player_df['per_count'].to_list()
        if player != chosen_player:
            new_fig.add_trace(go.Scatter(x=shotclock_ranges, y=values, name=player,
                                         line=dict(color='rgb(195,195,195)', width=3, dash='dot')))

    # plot sample average of the dataset
    new_fig.add_trace(go.Scatter(x=shotclock_ranges, y=sample_df['per_count'].to_list(), name='Sample Average',
                         line=dict(color='rgb(223,80,103)', width=3, dash='dash'
                                    )))

    chosen_values = shotclock_df[shotclock_df['assist_player'] == chosen_player]['per_count'].to_list()

    # plot the selected player's line plot
    new_fig.add_trace(go.Scatter(x=shotclock_ranges, y=chosen_values,
                                 name=chosen_player, line=dict(color='rgb(233,84,32)', width=5), mode="lines+text",
                                 text=['<b>' + str(round(val * 100, 1)) + '%' + '</b>' for val in chosen_values],
                                 textposition='top center', textfont=dict(color='black', size=13)))
    
    # define line plot figure's theme and colors
    new_fig.update_layout(
        font_color='black',
        plot_bgcolor='#F8F5F0',
        title='When in the Shotclock does %s find opportunities for assists?' % chosen_player,
        title_x=0.5,
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
        ),
        yaxis=dict(
            gridcolor='white'
        ),
        font=dict(family='Ubuntu')
    )

    new_fig.update_xaxes(title='Shotclock Range', showline=False)
    new_fig.update_yaxes(title='% of Assists', tickformat='0.0%', showline=False)

    return new_fig

####################################################################################
################################ SANKEY PLOT FIGURE ################################
#################################################################################### 

@app.callback(
    Output(component_id='sankey-plot', component_property='figure'),
    Input(component_id='player-select', component_property='value'),
)
def update_lineplot(pid):
    df = pd.read_sql_query("SELECT * FROM nbatrackingdata WHERE assistplayerid = %s" % pid, con=db.engine)

    counts_by_target = df.groupby(by=['assist_player','player']).size().reset_index().rename(columns={0: 'counts'}).sort_values(by=['counts'], ascending=False)
    counts_by_target_and_shots = df.groupby(by=['assist_player','player','shottype']).size().reset_index().rename(columns={0: 'counts'}).sort_values(by=['counts'], ascending=False)

    nodes, links, link_colors = [], [], []
    player_index_map, shottype_index_map = dict(), dict()
    shottype_color_map = {
        'AtRim': '#511479',
        'ShortMidRange': '#8B2880',
        'LongMidRange': '#C63E73',
        'Arc3': '#F3685F',
        'Corner3': '#FDAC78',
    }
    
    nodes = nodes + [{'label': player} for player in df['assist_player'].unique()]
    nodes = nodes + [{'label': player} for player in counts_by_target['player'].to_list()]
    nodes = nodes + [{'label': player} for player in counts_by_target_and_shots['shottype'].unique()]

    for player, num_assists, index in zip(counts_by_target['player'].to_list(), counts_by_target['counts'].to_list(), [i for i in range(1, len(counts_by_target) + 1)]):
        links.append({'source': 0, 'target': index, 'value': num_assists})
        player_index_map[player] = index
        link_colors.append('#FBCEB6')
        
    for shottype in counts_by_target_and_shots['shottype'].unique():
        index += 1
        shottype_index_map[shottype] = index
    
    for player, shottype, num_shot_assists in zip(counts_by_target_and_shots['player'].to_list(), counts_by_target_and_shots['shottype'].to_list(), counts_by_target_and_shots['counts'].to_list()):
        links.append({'source': player_index_map[player], 'target': shottype_index_map[shottype], 'value': num_shot_assists})
        link_colors.append(shottype_color_map[shottype])

    # Create the Sankey diagram figure
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color='black', width=1.0),
            label=[node['label'] for node in nodes],
            color='rgb(233,84,32)',
        ),
        link=dict(
            source=[link['source'] for link in links],
            target=[link['target'] for link in links],
            value=[link['value'] for link in links],
            color=link_colors,
            hovertemplate="Player: %{source.label}<br>"
                        "Target: %{target.label}<br>"
                        "No. Assists: %{value:.0f}<br>",
        ),
    )])

    assist_player_name = df['assist_player'].unique()[0]

    # Customize the layout if needed
    fig.update_layout(
        title_text="Who does %s connect with the most for assists?" % assist_player_name,
        title_x=0.5,
        font=dict(
            family='Ubuntu',  # Set the font for the plot title
            size=14  # Set the font size for the plot title
        ),
        height=750
    )

    return fig

####################################################################################
################################ DATA TABLE FIGURE #################################
#################################################################################### 

@app.callback(
    Output(component_id='assist-shottypes-table', component_property='data'),
    Input(component_id='assist-shottypes-table', component_property='data'),
)
def update_input_toggle_info(data):
    df = pd.read_sql_table('nbatrackingdata', con=db.engine)

    grouped = df.groupby(['assist_player', 'shottype']).size()
    total_counts = df.groupby(['assist_player']).size()
    percentages = round(grouped / total_counts, 3)

    result = percentages.unstack(level='shottype')
    result = result.reset_index()[['assist_player','AtRim','ShortMidRange','LongMidRange','Corner3','Arc3']]

    result.columns = ['Player','% of Rim Asts','% of Short Midrange Asts','% of Long Midrange Asts','% of Corner 3 Asts','% of Arc 3 Asts']

    result['% of High EV Asts'] = round(result['% of Rim Asts'] + result['% of Corner 3 Asts'], 3)

    result_tot = df.groupby(by=['assist_player']).size().reset_index().rename(columns={'assist_player': 'Player', 0: 'No. Tracked Asts'})

    paint_df = pd.read_sql_query('SELECT * FROM nbatrackingdata WHERE pass_x BETWEEN -80 AND 80 AND pass_y BETWEEN -52.5 and 137.5', con=db.engine)
    paint_tot = paint_df.groupby(by=['assist_player']).size().reset_index().rename(columns={'assist_player': 'Player', 0: 'No. Paint Asts'})

    result = pd.merge(result, result_tot, how='left', on=['Player'])
    result = pd.merge(result, paint_tot, how='left', on=['Player'])
    result['% of Asts thrown from the Paint'] = round(result['No. Paint Asts'] / result['No. Tracked Asts'], 3)

    result = result.drop(columns=['No. Paint Asts'])

    return result.to_dict(orient='records')

####################################################################################
################################## GRAPH TOGGLES ###################################
#################################################################################### 

@app.callback(
    Output(component_id='rose-toggle', component_property='label'),
    Input(component_id='rose-toggle', component_property='value'),
)
def update_input_toggle_info(toggle_on):
    return 'Rose Plot by Pass Distance' if toggle_on else 'Rose Plot by Shot Type Created'

@app.callback(
    Output(component_id='tooltips-toggle', component_property='label'),
    Input(component_id='tooltips-toggle', component_property='on')
)
def update_track_toggle_info(tooltips_toggle):
    return 'Tooltips are On' if tooltips_toggle else 'Tooltips are Off'

####################################################################################
################################# VIDEO FUNCTIONS ##################################
#################################################################################### 

@app.callback(
    Output(component_id='video-playback-modal', component_property='src'),
    Output(component_id='modal-title', component_property='children'),
    Input(component_id='display-graph', component_property='clickData')
)
def update_video_modal(clickData):
    if clickData:
        try:
            link = clickData['points'][0]['customdata'][-1]
            player = clickData['points'][0]['customdata'][1]
            assist_player = clickData['points'][0]['customdata'][-4]
            date = clickData['points'][0]['customdata'][4]
            date = datetime.fromisoformat(date).strftime('%b %d, %Y')
            opp = clickData['points'][0]['customdata'][-2]
            team = clickData['points'][0]['customdata'][-3]
            title = "%s's assist to %s (%s vs. %s on %s)" % (assist_player, player, team, opp, date)  # [:10])
            return link, title
        except:
            return dash.no_update, dash.no_update
    return dash.no_update, dash.no_update

@app.callback(
    Output(component_id='video-modal', component_property='is_open'),
    Input(component_id='open-modal-btn', component_property='n_clicks'),
    State(component_id='video-modal', component_property='is_open'),
    State(component_id='video-playback-modal', component_property='src')
)
def open_video_modal(btn, is_open, link):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    if 'open-modal-btn' in changed_id and link != '':
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run(debug=True)
