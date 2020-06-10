import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup, Comment
import re
import json
import time



def scrape_2018_stats():
    '''
    this function pulls statistics for the 2018 NFL regular season, it should return strings, floats, and ints, if not, run the helper functions
    for time of possession and then convert into float functions from lines 127 to 139, the feature engineering function can be found on line 144

    '''
    stats_2018 = []
    for i in range(0,600,100):
        url = """https://www.pro-football-reference.com/play-index/tgl_finder.cgi?request=1&match=game&year_min=2018&year_max=2018&game_type=R&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99&temperature_gtlt=lt&c1stat=points&c1comp=gte&c2stat=pass_yds&c2comp=gte&c3stat=rush_yds&c3comp=gte&c4stat=turnovers&c4comp=gte&c5stat=fgm&c5comp=gt&c5val=1.0&order_by=game_date&offset={}"""
        stats_2018.append(pd.read_html(url.format(i))[0])
    df = pd.concat(stats_2018)

    df[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')] = df[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')].fillna(value='Home')

    df[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')] = df[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')].replace(to_replace=['N', '@'], value=['Neutral', 'Away'])

    df.columns = df.columns.to_flat_index()

    df.reset_index()

    df.drop(df[df[('Unnamed: 1_level_0', 'Tm')] == 'Tm'].index, inplace=True)

    df = df.rename(columns={('Unnamed: 0_level_0', 'Rk'):'rk', 
        ('Unnamed: 1_level_0', 'Tm'): 'team1',
        ('Unnamed: 2_level_0', 'Year'): 'year',
        ('Unnamed: 3_level_0', 'Date'): 'date',
        ('Unnamed: 4_level_0', 'Time'): 'time',
        ('Unnamed: 5_level_0', 'LTime'): 'local_time', 
        ('Unnamed: 6_level_0', 'Unnamed: 6_level_1'): 'home_away',
        ('Unnamed: 7_level_0', 'Opp'): 'team2',
        ('Unnamed: 8_level_0', 'Week'): 'Week',
        ('Unnamed: 9_level_0', 'G#'): 'Game_Number',
        ('Unnamed: 10_level_0', 'Day'): 'day',
        ('Unnamed: 11_level_0', 'Result'): 'win1?',
        ('Unnamed: 12_level_0', 'OT'): 'OT',
        ('Points', 'PF'):'points_for',
        ('Points', 'PA'): 'points_against',
        ('Points', 'PD'): 'point_diff',
        ('Points', 'PC'):'combined_pts',
        ('Passing', 'Cmp'):'completions',
        ('Passing', 'Att'):'attempts',
        ('Passing', 'Cmp%'):'comp_percent',
        ('Passing', 'Yds'):'passing_yards',
        ('Passing', 'TD'):'passing_tds',
        ('Passing', 'Int'):'INT',
        ('Passing', 'Sk'):'times_sacked',
        ('Passing', 'Yds.1'):'sack_yards_lost',
        ('Passing', 'Rate'):'qbr',
        ('Rushing', 'Att'):'rushing_attempts',
        ('Rushing', 'Yds'):'rushing_yards',
        ('Rushing', 'Y/A'):'rushing_yards_per_attempt',
        ('Rushing', 'TD'):'rushing_TD',
        ('Tot Yds & TO', 'Tot'):'total_yards',
        ('Tot Yds & TO', 'Ply'):'offensive_plays',
        ('Tot Yds & TO', 'Y/P'):'yards_per_play_offense',
        ('Tot Yds & TO', 'DPly'):'Defensive_plays',
        ('Tot Yds & TO', 'DY/P'):'yards_allowed_per_defensive_play',
        ('Tot Yds & TO', 'TO'):'turnovers_lost',
        ('Tot Yds & TO', 'ToP'):'time_of_possesion',
        ('Tot Yds & TO', 'Time'):'drop_this1',
        ('Scoring', 'TD'):'total_TD',
        ('Scoring', 'XPA'):'XPA',
        ('Scoring', 'XPM'):'XPM',
        ('Scoring', 'FGA'):'FGA',
        ('Scoring', 'FGM'):'FGM',
        ('Scoring', '2PA'):'2pa',
        ('Scoring', '2PM'):'2pm',
        ('Scoring', 'Sfty'):'sfty'})

    dfs = df[['team1','date', 'home_away','team2', 'Week', 'Game_Number', 'win1?', 
          'points_for', 'points_against','times_sacked','yards_per_play_offense',
          'yards_allowed_per_defensive_play','turnovers_lost',
           'time_of_possesion', 'total_TD', 'FGM' ]]

    stats_20181 = []
    for i in range(0,600,100):
        url1 = """https://www.pro-football-reference.com/play-index/tgl_finder.cgi?request=1&match=game&year_min=2018&year_max=2018&game_type=R&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99&temperature_gtlt=lt&c1stat=penalties_yds&c1comp=gte&c5stat=fgm&c5comp=gt&c5val=1.0&order_by=game_date&offset={}"""
        stats_20181.append(pd.read_html(url1.format(i))[0])      

    df1 = pd.concat(stats_20181)

    df1[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')] = df1[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')].fillna(value='Home')

    df1[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')] = df1[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')].replace(to_replace=['N', '@'], value=['Neutral', 'Away'])

    df1.columns = df1.columns.to_flat_index()

    df1.reset_index()  

    df1.drop(df1[df1[('Unnamed: 1_level_0', 'Tm')] == 'Tm'].index, inplace=True)

    df1 = df1.rename(columns={('Unnamed: 0_level_0', 'Rk'):'rk', 
                        ('Unnamed: 1_level_0', 'Tm'): 'team1',
                        ('Unnamed: 2_level_0', 'Year'): 'year',
                        ('Unnamed: 3_level_0', 'Date'): 'date',
                        ('Unnamed: 4_level_0', 'Time'): 'time',
                        ('Unnamed: 5_level_0', 'LTime'): 'local_time', 
                        ('Unnamed: 6_level_0', 'Unnamed: 6_level_1'): 'home_away',
                        ('Unnamed: 7_level_0', 'Opp'): 'team2',
                        ('Unnamed: 8_level_0', 'Week'): 'Week',
                        ('Unnamed: 9_level_0', 'G#'): 'Game_Number',
                        ('Unnamed: 10_level_0', 'Day'): 'day',
                        ('Unnamed: 11_level_0', 'Result'): 'win1?',
                        ('Unnamed: 12_level_0', 'OT'): 'OT',
                        ('Penalties', 'Yds'): 'penalty_yards1',
                        ('Penalties', 'OppYds'):'penalty_yards2'})

    dfs1 = df1[['team1', 'team2', 'Week', 'penalty_yards1', 'penalty_yards2']]

    dfs2 = dfs.merge(dfs1, on=['team1', 'team2','Week'], how='left')

    return dfs2


def top_ratio(text):
    return float(text.split(':')[0])/60 + float(text.split(':')[1])/3600
def time_of_possession_to_ratio(data):
    data['time_of_possesion'] = data['time_of_possesion'].apply(lambda x: top_ratio(x))
    return data



col_list = list(df.columns) # change columns to numerical columns, this as is will throw an error

def text_to_num(text):
    return float(text)

def convert_into_float(data):
    data[col_list] = data[col_list].applymap(text_to_num)
    return data


def clean_data(data):
    data['win1?'] = data['win1?'].apply(lambda x: x[0])
    data['win1?'] = data['win1?'].replace(to_replace=['W', 'L', 'T'], value=[1.0, 0.0, 0.0])
    data = data.sort_values('Week')
    data['home_away'] = data['home_away'].replace(to_replace=['Home', 'Away'], value=[1,0])
    data = data.rename(columns={'home_away':'home'})
    data = data.rename(columns={'team1':'team', 'team2':'opp', 'win1?':'win', 
                            'penalty_yards1':'penalty_yards', 
                            'penalty_yards2':'opp_penalty_yards'})
    data['loss'] = 1 - data['win']
    data['total_wins'] = data.groupby('team')['win'].cumsum()
    data['total_losses'] = data.groupby('team')['loss'].cumsum()
    data['away'] = 1 - data['home']
    return data
