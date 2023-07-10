from dash import html
import dash_bootstrap_components as dbc

home_page = dbc.Container([
    html.H1('About this App', className='mt-3'),
    html.Hr(className="my-2"),
    html.H5('Motivation'),
    html.P("In the public realm, our access to spatial data is limited to shot coordinates. "
           "But what about spatial data looking at pass coordinates on assists? "
           "Passing is such an integral part of the game and it’s what makes the game so beautiful to watch. "
           "So how can we visualize passing location data? Can we create any interesting player insights using "
           "this data the way shot charts do with shot coordinate data?"
    ),
    html.H5('About The Data Source'),
    html.P(["Thanks to Darryl Blackport, the currently available shot tracking dataset has been made "
            "accessible on his site at ",
            html.A("tracking.pbpstats.com", href="https://tracking.pbpstats.com"),
            ". That dataset was then filtered for all assisted shots and so "
            "I built a separate Python tool to manually track the pass origin "
            "and endpoint by watching film from the Video URL that the dataset pairs each shot with. Please "
            "feel free to read more about the tracking application and process by clicking here. "
            "The manual hand-tracking process was done for 13 players for various parts or most/all of the 2020-21 and 2021-22 NBA Regular Season. "
            "Data is available for the following players: Bam Adebayo, Chris Paul, Darius Garland, Dejounte Murray, Draymond Green, Ja Morant, James Harden, Jordan Poole, "
            "Julius Randle, LaMelo Ball, LeBron James, Nikola Jokic, Trae Young, totaling to 5004 manually tracked data points. "
            ]),
    html.H5('Will more shots be manually tracked?'),
    html.P("Probably not, since it's very time consuming; but, if time permits later down the line or if my desire to do so returns, " 
           "there are plans to track the following players: Doncic, Lebron, Jokic, and Haliburton. "
           "Originally, this project was done out of pure curiosity and inspiration in order to develop scouting reports, "
           "perform my own personal passing studies on players, "
           "and also learn how to work with sports data and tech. "
           "If you're interested in contributing or tracking, please let me know and I'd be happy to discuss further. Feel free to also let me know if you have "
           "any ideas to improve this project. "
           ),
    html.H5('GitHub Code'),
    html.P([
        'Interested in looking at the code for this web-application? ',
        html.A("Click here to view the source code!", href="https://github.com/lukarh/assist-tracking-app-v2"),
    ]),
    html.H5('Developed By:'),
    html.P("Lukar Huang (lwhuang@alumni.cmu.edu)"),
])