#Standings scraper from ESPN. Default standings view
#is by conference. This script populates an array with
# team name, wins, losses, win pct., GB, home record,
#road record, division record, conf record, ppg, opp ppg,
#point diff, win streak, and L10.

import urllib2
from bs4 import BeautifulSoup
import datetime as dt

#default standings view is by Conference

now = dt.datetime.now()

url = 'http://espn.go.com/nba/standings'

soup = BeautifulSoup(urllib2.urlopen(url).read(), "html.parser")
rows = soup.select('.standings-row')

for row in rows:
    #initialize team array
    team = []

    row_soup = BeautifulSoup(str(row), "html.parser")

    #get team name
    team.append(row_soup.select('.team-names')[0].string)

    #get stats
    team_info = row_soup.find_all(style="white-space:no-wrap;")
    iter_team_info = iter(team_info)
    for info in iter_team_info:
        team.append(info.string)

    print team
    #store standings data
    date = now
    team_name = team[0].split(" ")[-1]
    wins = team[1]
    losses = team[2]
    pct = team[3]
    gb = team[4]
    home_wins = team[5].split('-')[0]
    home_losses = team[5].split('-')[1]
    road_wins = team[6].split('-')[0]
    road_losses = team[6].split('-')[1]
    division_wins = team[7].split('-')[0]
    division_losses = team[7].split('-')[1]
    conference_wins = team[8].split('-')[0]
    conference_losses = team[8].split('-')[1]
    ppg = team[9]
    opp_ppg = team[10]
    pt_diff = team[11]
    #string out the W/L from streak info
    if team[12][0] == "L":
        win_streak = "-" + team[12][1:]
    else:
        win_streak = team[12][1:]
    last_10_wins = team[13].split('-')[0]
    last_10_losses = team[13].split('-')[1]

    #save standing
    print date, team_name, wins, losses, pct, gb, home_wins, home_losses, road_wins,
    road_losses, division_wins, division_losses, conference_wins, conference_losses,
    ppg, opp_ppg, pt_diff, win_streak, last_10_wins, last_10_losses
