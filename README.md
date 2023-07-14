# assist-tracking-dash-app-v2

## Motivation

In the public realm, our access to spatial data is limited to shot coordinates. But what about spatial data looking at pass coordinates on assists? Passing is such an integral part of the game and [it’s what makes the game so beautiful to watch](https://www.youtube.com/watch?v=NsBGF1fjXvY&ab_channel=EvinGualberto). So how can we visualize passing location data? Can we create any interesting player insights using this data the way shot charts do with shot coordinate data?

## Achievements
- Featured on Dave Gibbon's, Sr. Director of Plotly, [Top 500 Real World Plotly & Dash Web-Applications](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A6993654939717689344/?commentUrn=urn%3Ali%3Acomment%3A%28ugcPost%3A6993654864748707840%2C6993659640815259648%29&dashCommentUrn=urn%3Ali%3Afsd%5Fcomment%3A%286993659640815259648%2Curn%3Ali%3AugcPost%3A6993654864748707840%29&midToken=AQE7AcWiE982Tw&midSig=22w2_pD5bN2Ww1&trk=eml-email_notification_single_mentioned_you_in_this_01-notifications-1-hero%7Ecard%7Efeed&trkEmail=eml-email_notification_single_mentioned_you_in_this_01-notifications-1-hero%7Ecard%7Efeed-null-9t7xw6%7Ela02emup%7Evh-null-voyagerOffline). You can find the application live on their [website](https://plotly.com/examples/sports-analytics/).
- Presented the project to former Bucks Analytics Manager, Ashley Brio, and showcased it in an interview with Maksim Horowitz, Director of Basketball Strategy & Analytics, of the Atlanta Hawks

## Languages, Tools, and Libraries/Packages
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white) ![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

## What's New? Future plans?

Version 2.0.0 of the Assist Tracking Web Application built on the Plotly Dash Framework brings in a new and refreshing UI experience with newly tracked data points for 5 players during the 2021-22 NBA Season, providing data insights to now 13 total players! After gaining a bit more experience with coding, I decided to revisit this project and give it a brand new overhaul. The web application has also reformed its codebase to conform itself to the industry standard so that it's scalable in the future and easy to work with. In the previous version, which can be found [here](https://github.com/lukarh/assist-tracking-app), the 2500+ lines of code was written in a singular .py file, which made it incredibly hard to navigate, edit, and develop- however, version 2.0.0 organizes the code in separate folders and files for various scenes and components used across the web-application, making the developer experience a smoother one. In the future, if time permits or if inspiration sparks, new features, data, and pages will be considered!

Here's a list of what's new and fixed:
- Application load time has been reduced significantly
- A brand new refreshing UI experience with a consistent and bright color theme
- Data insights to 5 new players!
- Added a datatable and sankey diagram for further data insights on the live dashboard
- Removed redundant code logic that used up unneccessary memory when the user is engaged with the application
- Fixed bug showing dates incorrectly on a scatter point's tooltip
- Dynamic SQL queries, previously all data filtering was done through pandas after querying the entire database
- Restructured a monolithic codebase comprising a single 2500+ line .py file into a modularized and industry-standard format

## Feel free to visit the live website!

[Click here to view the website](https://tracking-dashboard-app.herokuapp.com/dashboard)

## Development

- Code: Python
- Framework: Dash (A Python Framework)
- Libraries: SQLAlchemy, Plotly, Pandas, NumPy, Dash, Numpy, Dash Bootstrap Components, Dash Core Components
- Database: PostgreSQL via Heroku
- Deployment: Heroku

#### Useful Links
- [Dash DAQ](https://dash.plotly.com/dash-daq)
- [Dash Framework](https://plotly.com/dash/)
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)

## Deployment
In a terminal at this directory, run the following command to install all necessary libraries / packages:

```pip install -r requirements.txt```

To test the app locally, run the following command:

```python main.py```

Deploy the App to Heroku, use the [tutorial that outlines the instructions here](https://drive.google.com/file/d/1kowjMGKN6rbxh9n-5q1cP3BkcZ2yOAvo/view).

**NOTE: This Public Repository does not have access to the SQL database key, so you can't access the data to test the web-application locally properly.**

## Overview of Changes

#### Live Dashboard for Player Reports | A Before and After

The Interactive Dashboard builds a player report showing their directional tendencies, hotspots on the floor, flow diagrams of outcomes, and preferred timing for passes during assist plays based on 5000+ manually tracked data points that are stored in a PostgreSQL database. Users can apply multiple filters such as opponent team, date, shot type created, shot clock, minute left in the period, etc. and the dashboard will dynamically update accordingly.

##### After (In Version 2.0.0)

![image](https://github.com/lukarh/assist-tracking-app-v2/assets/65103724/d53aeb8b-a1e9-45d2-b838-1452c700db67)

![image](https://github.com/lukarh/assist-tracking-app-v2/assets/65103724/1dc8c168-feaf-4be8-a18d-52937237d76d)


##### Before (In Version 1.0.0)

![dashboard-ui](https://user-images.githubusercontent.com/65103724/163692815-85a7d1e1-f601-417f-801c-277c355b471f.png)
