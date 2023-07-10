import numpy as np
import plotly.graph_objects as go

def draw_plotly_court(fig, fig_width=500, fig_height=870, margins=10, lwidth=3,
                      show_title=True, labelticks=True, show_axis=True,
                      glayer='below', bg_color='white'):
    # From: https://community.plot.ly/t/arc-shape-with-path/7205/5
    def ellipse_arc(x_center=0.0, y_center=0.0, a=10.5, b=10.5,
                    start_angle=0.0, end_angle=2 * np.pi, N=200,
                    closed=False, opposite=False):
        t = np.linspace(start_angle, end_angle, N)
        x = x_center + a * np.cos(t)
        if opposite:
            y = y_center + b * np.sin(-t)
        else:
            y = y_center + b * np.sin(t)
        path = f'M {x[0]}, {y[0]}'
        for k in range(1, len(t)):
            path += f'L{x[k]}, {y[k]}'
        if closed:
            path += ' Z'
        return path

    ####################################################################
    ############################ dimensions ############################
    #  half-court -52.5 <= y <= 417.5, full-court -52.5 <= y <= 887.5  #
    ####################################################################
    fig.update_layout(height=870,
                      template='plotly_dark')

    # Set axes ranges
    fig.update_xaxes(range=[-250 - margins, 250 + margins],
                     visible=show_title)
    fig.update_yaxes(range=[-52.5 - margins, 887.5 + margins],
                     visible=show_title)

    threept_break_y = 89.47765084
    three_line_col = "#000000"
    main_line_col = "#000000"
    fig.update_layout(
        # Line Horizontal
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        yaxis=dict(
            scaleanchor="x",
            scaleratio=1,
            showgrid=False,
            zeroline=False,
            showline=False,
            ticks='',
            fixedrange=True,
            visible=show_axis,
            showticklabels=labelticks,
        ),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            ticks='',
            fixedrange=True,
            visible=show_axis,
            showticklabels=labelticks,
        ),
        yaxis2=dict(
            scaleanchor="x2",
            showgrid=False,
            zeroline=False,
            showline=False,
            ticks='',
            fixedrange=True,
            visible=show_axis,
            showticklabels=labelticks,
            range=[-52.5 - margins, 887.5 + margins]
        ),
        xaxis2=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            ticks='',
            fixedrange=True,
            visible=show_axis,
            showticklabels=labelticks,
            range=[-250 - margins, 250 + margins]
        ),
        showlegend=False,
        shapes=[
            # court border
            dict(
                type="rect", x0=-250, y0=-52.5, x1=250, y1=887.5,
                line=dict(color=main_line_col, width=lwidth),
                # fillcolor='#333333',
                layer=glayer
            ),
            # half-court line
            dict(
                type="line", x0=-250, y0=417.5, x1=250, y1=417.5,
                line=dict(color=main_line_col, width=lwidth),
                layer=glayer
            ),
            # back-court outer ft-lines
            dict(
                type="line", x0=-80, y0=697.5, x1=-80, y1=887.5,
                line=dict(color=main_line_col, width=lwidth),
                layer=glayer
            ),
            dict(
                type="line", x0=80, y0=697.5, x1=80, y1=887.5,
                line=dict(color=main_line_col, width=lwidth),
                layer=glayer
            ),
            # back-court inner ft-lines
            dict(
                type="line", x0=-60, y0=697.5, x1=-60, y1=887.5,
                line=dict(color=main_line_col, width=lwidth),
                layer=glayer
            ),
            dict(
                type="line", x0=60, y0=697.5, x1=60, y1=887.5,
                line=dict(color=main_line_col, width=lwidth),
                layer=glayer
            ),
            # front-court outer ft-lines
            dict(
                type="line", x0=-80, y0=-52.5, x1=-80, y1=137.5,
                line=dict(color=main_line_col, width=lwidth),
                layer=glayer
            ),
            dict(
                type="line", x0=80, y0=-52.5, x1=80, y1=137.5,
                line=dict(color=main_line_col, width=lwidth),
                layer=glayer
            ),
            # front-court inner ft-lines
            dict(
                type="line", x0=-60, y0=-52.5, x1=-60, y1=137.5,
                line=dict(color=main_line_col, width=lwidth),
                layer=glayer
            ),
            dict(
                type="line", x0=60, y0=-52.5, x1=60, y1=137.5,
                line=dict(color=main_line_col, width=lwidth),
                layer=glayer
            ),
            # back-court ft-circle
            dict(
                type="circle", x0=-60, y0=637.5, x1=60, y1=757.5, xref="x", yref="y",
                line=dict(color=main_line_col, width=lwidth),
                # fillcolor='#dddddd',
                layer=glayer
            ),
            # front-court ft-circle
            dict(
                type="circle", x0=-60, y0=77.5, x1=60, y1=197.5, xref="x", yref="y",
                line=dict(color=main_line_col, width=lwidth),
                # fillcolor='#dddddd',
                layer=glayer
            ),
            # back-court ft-line
            dict(
                type="line", x0=-80, y0=697.5, x1=80, y1=697.5,
                line=dict(color=main_line_col, width=lwidth),
                layer=glayer
            ),
            # front-court ft-line
            dict(
                type="line", x0=-80, y0=137.5, x1=80, y1=137.5,
                line=dict(color=main_line_col, width=lwidth),
                layer=glayer
            ),
            # back-court basket
            dict(
                type="circle", x0=-7.5, y0=827.5, x1=7.5, y1=842.5, xref="x", yref="y",
                line=dict(color="#ec7607", width=lwidth),
            ),
            dict(
                type="rect", x0=-2, y0=842.25, x1=2, y1=847.25,
                line=dict(color="#ec7607", width=lwidth),
                fillcolor='#ec7607',
            ),
            dict(
                type="line", x0=-30, y0=847.5, x1=30, y1=847.5,
                line=dict(color="#ec7607", width=lwidth),
            ),
            # front-court basket
            dict(
                type="circle", x0=-7.5, y0=-7.5, x1=7.5, y1=7.5, xref="x", yref="y",
                line=dict(color="#ec7607", width=lwidth),
            ),
            dict(
                type="rect", x0=-2, y0=-7.25, x1=2, y1=-12.5,
                line=dict(color="#ec7607", width=lwidth),
                fillcolor='#ec7607',
            ),
            dict(
                type="line", x0=-30, y0=-12.5, x1=30, y1=-12.5,
                line=dict(color="#ec7607", width=lwidth),
            ),
            # back-court charge circle
            dict(type="path",
                 path=ellipse_arc(y_center=835, a=40, b=40,
                                  start_angle=0, end_angle=np.pi, opposite=True),
                 line=dict(color=main_line_col, width=lwidth), layer=glayer),
            # front-court charge circle
            dict(type="path",
                 path=ellipse_arc(a=40, b=40, start_angle=0, end_angle=np.pi),
                 line=dict(color=main_line_col, width=lwidth), layer=glayer),
            # back-court 3pt line
            dict(type="path",
                 path=ellipse_arc(y_center=835, a=237.5, b=237.5, start_angle=np.pi - \
                                                                              0.386283101, end_angle=0.386283101,
                                  opposite=True),
                 line=dict(color=main_line_col, width=lwidth), layer=glayer),
            # front-court 3pt line
            dict(type="path",
                 path=ellipse_arc(
                     a=237.5, b=237.5, start_angle=0.386283101, end_angle=np.pi - 0.386283101),
                 line=dict(color=main_line_col, width=lwidth), layer=glayer),
            # back-court corner three lines
            dict(
                type="line", x0=-220, y0=835 - threept_break_y, x1=-220, y1=887.5,
                line=dict(color=three_line_col, width=lwidth), layer=glayer
            ),
            dict(
                type="line", x0=220, y0=835 - threept_break_y, x1=220, y1=887.5,
                line=dict(color=three_line_col, width=lwidth), layer=glayer
            ),
            # front-court corner three lines
            dict(
                type="line", x0=-220, y0=-52.5, x1=-220, y1=threept_break_y,
                line=dict(color=three_line_col, width=lwidth), layer=glayer
            ),
            dict(
                type="line", x0=220, y0=-52.5, x1=220, y1=threept_break_y,
                line=dict(color=three_line_col, width=lwidth), layer=glayer
            ),
            # back-court tick marks
            dict(
                type="line", x0=-250, y0=607.5, x1=-220, y1=607.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            dict(
                type="line", x0=250, y0=607.5, x1=220, y1=607.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            # front-court tick marks
            dict(
                type="line", x0=-250, y0=227.5, x1=-220, y1=227.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            dict(
                type="line", x0=250, y0=227.5, x1=220, y1=227.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            # front-court free-throw tick marks
            dict(
                type="line", x0=-90, y0=17.5, x1=-80, y1=17.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            dict(
                type="line", x0=-90, y0=27.5, x1=-80, y1=27.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            dict(
                type="line", x0=-90, y0=57.5, x1=-80, y1=57.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            dict(
                type="line", x0=-90, y0=87.5, x1=-80, y1=87.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            dict(
                type="line", x0=90, y0=17.5, x1=80, y1=17.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            dict(
                type="line", x0=90, y0=27.5, x1=80, y1=27.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            dict(
                type="line", x0=90, y0=57.5, x1=80, y1=57.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            dict(
                type="line", x0=90, y0=87.5, x1=80, y1=87.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            # back-court free-throw tick marks
            dict(
                type="line", x0=-90, y0=817.5, x1=-80, y1=817.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            dict(
                type="line", x0=-90, y0=807.5, x1=-80, y1=807.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            dict(
                type="line", x0=-90, y0=777.5, x1=-80, y1=777.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            dict(
                type="line", x0=-90, y0=747.5, x1=-80, y1=747.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            dict(
                type="line", x0=90, y0=817.5, x1=80, y1=817.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            dict(
                type="line", x0=90, y0=807.5, x1=80, y1=807.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            dict(
                type="line", x0=90, y0=777.5, x1=80, y1=777.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            dict(
                type="line", x0=90, y0=747.5, x1=80, y1=747.5,
                line=dict(color=main_line_col, width=lwidth), layer=glayer
            ),
            # half-court outer circle
            dict(type="path",
                 path=ellipse_arc(y_center=417.5, a=60, b=60,
                                  start_angle=0, end_angle=2 * np.pi),
                 line=dict(color=main_line_col, width=lwidth), layer=glayer),
            # half-court inner circle
            dict(type="path",
                 path=ellipse_arc(y_center=417.5, a=25, b=25,
                                  start_angle=0, end_angle=2 * np.pi),
                 line=dict(color=main_line_col, width=lwidth), layer=glayer),
        ]
    )
    return True