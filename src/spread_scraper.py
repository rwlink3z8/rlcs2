# scraper to pull spreads for the 2019 season
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup, Comment
import re
import json
import time


url = """https://www.teamrankings.com/nfl-ats-picks/?range=week-{}"""

def spread_scraper(url):

    odds = []                                                                                                                                                                                                                                                                                                                                                                                                                                
    for i in range(1,18,1):
        url = url
        odds.append(pd.read_html(url.format(i))[0])

    odds = pd.concat(odds)
    odds = odds.reset_index()
    odds['spread'] = odds['TR Pick'].apply(lambda x: x.split()[-1])
    odds['team'] = odds['TR Pick'].apply(lambda x: ' '.join(x.split()[1:-1]))
    odds['opponent'] = odds['Opp/Game'].apply(lambda x: ' '.join(x.split()[1:]))
    odds['home'] = odds['Opp/Game'].apply(lambda x: ' '.join(x.split()[:1]))
    odds['home'] = odds['home'].replace(to_replace=['vs', 'at'], value=[1,0])
    odds['away'] = 1 - odds['home']
    odds['spread'] = odds['spread'].apply(lambda x: float(x))
    odds['opponent_spread'] = -1 * odds['spread']
    odds['favorite'] = odds['spread'] < 0
    odds['favorite'] = odds['favorite'].replace(to_replace=[True, False], value=[1, 0])
    odds['underdog'] = 1 - odds['favorite']
    
    td1 = {'Chicago': 'BEARS', 'NY Jets': 'JETS', 'LA Rams': 'RAMS', 'Miami': 'DOLPHINS', 'Jacksonville': 'JAGUARS',
            'Tennessee':'TITANS', 'Washington':'REDSKINS', 'Atlanta': 'FALCONS', 'Cincinnati':'BENGALS', 'LA Chargers':'CHARGERS',
            'San Francisco':'49ERS', 'Arizona':'CARDINALS','NY Giants':'GIANTS', 'Pittsburgh':'STEELERS','Houston':'TEXANS',
            'Denver':'BRONCOS', 'Tampa Bay':'BUCCANEERS','Green Bay':'PACKERS','Dallas':'COWBOYS',
            'Baltimore':'RAVENS', 'Buffalo':'BILLS', 'Indianapolis':'COLTS', 'Seattle':'SEAHAWKS',
            'Oakland':'RAIDERS','New Orleans':'SAINTS','Cleveland':'BROWNS','Detroit':'LIONS','Philadelphia':'EAGLES',
            'Kansas City':'CHIEFS','Minnesota':'VIKINGS','New England':'PATRIOTS', 'Carolina':'PANTHERS'}
    
    odds['team'] = odds['team'].replace(to_replace=td1.keys(), value=td1.values())
    odds['opponent'] = odds['opponent'].replace(to_replace=td1.keys(), value=td1.values())

    o1 = odds[['team','opponent', 'home', 'away', 'spread', 'opponent_spread']]
    o2 = odds[['opponent', 'team', 'away', 'home', 'opponent_spread', 'spread']]
    o2.columns = ['team','opponent', 'home', 'away', 'spread', 'opponent_spread']
    frames = [o1,o2]
    spread_stats = pd.concat(frames)

    return spread_stats
