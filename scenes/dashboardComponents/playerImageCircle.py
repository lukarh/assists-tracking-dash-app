from dash import html

player_image_circle = html.Center(
    html.Img(
        src='https://cdn.nba.com/headshots/nba/latest/1040x760/%d.png',
        id='player-image-circle',
        width='60%'),
        style={
                    'width': '200px',
                    'height': '200px',
                    'border-radius': '50%',
                    'border': '2px solid #000000',
                },
)