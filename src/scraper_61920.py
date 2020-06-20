import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup, Comment
import re
import json
import time

url = """https://www.pro-football-reference.com/play-index/tgl_finder.cgi?request=1&match=game&year_min=2019&year_max=2019&game_type=E&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99&temperature_gtlt=lt&c1stat=vegas_line&c1comp=gte&c2stat=pass_yds&c2comp=gte&c3stat=points_opp&c3comp=gte&c4stat=rush_yds&c4comp=gte&c5stat=yds_per_play_offense&c5comp=gt&c5val=1.0&order_by=game_date&offset={}"""

url1 = """https://www.pro-football-reference.com/play-index/tgl_finder.cgi?request=1&match=game&year_min=2019&year_max=2019&game_type=E&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99&temperature_gtlt=lt&c1stat=vegas_line&c1comp=gte&c2stat=over_under&c2comp=gte&c3stat=pass_yds_opp&c3comp=gte&c4stat=rush_yds_opp&c4comp=gte&c5stat=tot_yds_opp&c5comp=gt&c5val=1.0&order_by=game_date&offset={}"""

url2 = """https://www.pro-football-reference.com/play-index/tgl_finder.cgi?request=1&match=game&year_min=2019&year_max=2019&game_type=E&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99&temperature_gtlt=lt&c1stat=vegas_line&c1comp=gte&c2stat=over_under&c2comp=gte&c3stat=fgm&c3comp=gte&c4stat=fgm_opp&c4comp=gte&c5stat=tot_yds_opp&c5comp=gt&c5val=1.0&order_by=game_date&offset={}"""

url3 = """https://www.pro-football-reference.com/play-index/tgl_finder.cgi?request=1&match=game&year_min=2019&year_max=2019&game_type=E&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99&temperature_gtlt=lt&c1stat=vegas_line&c1comp=gte&c2stat=pass_yds&c2comp=gte&c3stat=points_opp&c3comp=gte&c4stat=rush_yds&c4comp=gte&c5stat=penalties_yds&c5comp=gt&c5val=1.0&order_by=game_date&offset={}"""


def scrape_stats(url,url1,url2,url3):

    odds = []                                                                                                                                                                                                                                                                                                                                                                                                                                
    for i in range(0,300,100):
        url = url
        odds.append(pd.read_html(url.format(i))[0])

    df = pd.concat(odds)

    df.columns = df.columns.to_flat_index()

    df.reset_index()

    df.drop(df[df[('Unnamed: 1_level_0', 'Tm')] == 'Tm'].index, inplace=True)

    df[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')] = df[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')].fillna(value='Home') 

    df[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')] = df[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')].replace(to_replace=['N', '@'], value=['Neutral', 'Away'])  

    df = df.rename(columns={('Unnamed: 0_level_0', 'Rk'):'rk', ('Unnamed: 1_level_0', 'Tm'): 'team1', ('Unnamed: 2_level_0', 'Year'): 'year',
        ('Unnamed: 3_level_0', 'Date'): 'date', ('Unnamed: 4_level_0', 'Time'): 'time', ('Unnamed: 5_level_0', 'LTime'): 'local_time', 
        ('Unnamed: 6_level_0', 'Unnamed: 6_level_1'): 'home_away', ('Unnamed: 7_level_0', 'Opp'): 'team2',
        ('Unnamed: 8_level_0', 'Week'): 'week',('Unnamed: 9_level_0', 'G#'): 'Game_Number',('Unnamed: 10_level_0', 'Day'): 'day',
        ('Unnamed: 11_level_0', 'Result'): 'win1?',('Unnamed: 12_level_0', 'OT'): 'OT',('Points', 'PF'): 'points_1',('Points', 'PA'): 'points_2',
        ('Points', 'PD'): 'point_differential',('Points', 'PC'): 'combined_points',('Vegas', 'Spread'): 'spread',
        ('Vegas', 'vs. Line'): 'team1_covered_spread?',('Vegas', 'Over/Under'): 'over_under',('Vegas', 'OU Result'): 'over_under_result?',
        ('Passing', 'Cmp'): 'pass_completions1',('Passing', 'Att'): 'pass_attempts1',('Passing', 'Cmp%'): 'completion_percentage1',
        ('Passing', 'Yds'): 'passing_yards1',('Passing', 'TD'): 'passing_touchdowns1',('Passing', 'Int'): 'interceptions1',
        ('Passing', 'Sk'): 'times_sacked1',('Passing', 'Yds.1'): 'sack_yards_lost1',('Passing', 'Rate'): 'qbr1',
        ('Rushing', 'Att'): 'rushing_attempts1',('Rushing', 'Yds'): 'rushing_yards1',('Rushing', 'Y/A'): 'rushing_yards_per_attempt1',
        ('Rushing', 'TD'): 'rushing_touchdowns1',('Tot Yds & TO', 'Tot'): 'total_yards1',('Tot Yds & TO', 'Ply'): 'offensive_plays1',
        ('Tot Yds & TO', 'Y/P'): 'yards_per_play_offense1',('Tot Yds & TO', 'DPly'): 'defensive_plays1',('Tot Yds & TO', 'DY/P'): 'yards_allowed_per_defensive_play1',
        ('Tot Yds & TO', 'TO'): 'turnovers_lost1',('Tot Yds & TO', 'ToP'): 'time_of_possession1',('Tot Yds & TO', 'Time'): 'game_duration'})


    odds1 = []                                                                                                                                                                                                                                                                                                                                                                                                                                        
    for i in range(0,300,100):
        url = url1
        odds1.append(pd.read_html(url1.format(i))[0])

    df1 = pd.concat(odds1)

    df1.drop(df1[df1[('Unnamed: 1_level_0', 'Tm')] == 'Tm'].index, inplace=True)

    df1[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')] = df1[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')].fillna(value='Home')

    df1[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')] = df1[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')].replace(to_replace=['N', '@'], value=['Neutral', 'Away'])

    df1.columns = df1.columns.to_flat_index()

    df1.reset_index()

    df1 = df1.rename(columns={('Unnamed: 0_level_0', 'Rk'):'rk', ('Unnamed: 1_level_0', 'Tm'): 'team1',('Unnamed: 2_level_0', 'Year'): 'year',
        ('Unnamed: 3_level_0', 'Date'): 'date',('Unnamed: 4_level_0', 'Time'): 'time',('Unnamed: 5_level_0', 'LTime'): 'local_time', 
        ('Unnamed: 6_level_0', 'Unnamed: 6_level_1'): 'home_away',('Unnamed: 7_level_0', 'Opp'): 'team2',('Unnamed: 8_level_0', 'Week'): 'week',
        ('Unnamed: 9_level_0', 'G#'): 'Game_Number',('Unnamed: 10_level_0', 'Day'): 'day',('Unnamed: 11_level_0', 'Result'): 'win1?',
        ('Unnamed: 12_level_0', 'OT'): 'OT',('Vegas', 'Spread'): 'spread',('Vegas', 'vs. Line'): 'team1_covered_spread?',
        ('Vegas', 'Over/Under'): 'over_under',('Vegas', 'OU Result'): 'over_under_result?',('Passing', 'Cmp'): 'pass_completions2',
        ('Passing', 'Att'): 'pass_attempts2',('Passing', 'Cmp%'): 'completion_percentage2',('Passing', 'Yds'): 'passing_yards2',
        ('Passing', 'TD'): 'passing_touchdowns2',('Passing', 'Int'): 'interceptions2',('Passing', 'Sk'): 'times_sacked2',
        ('Passing', 'Yds.1'): 'sack_yards_lost2',('Passing', 'Rate'): 'qbr2',('Rushing', 'Att'): 'rushing_attempts2',
        ('Rushing', 'Yds'): 'rushing_yards2',('Rushing', 'Y/A'): 'rushing_yards_per_attempt2',('Rushing', 'TD'): 'rushing_touchdowns2',
        ('Opp Tot Yds & TO', 'Tot'):'total_yards2',('Opp Tot Yds & TO', 'TO'):'turnovers2'})

    odds2 = []                                                                                                                                                                                                                                                                                                                                                                                                                                
    for i in range(0,300,100):
        url = url2
        odds2.append(pd.read_html(url2.format(i))[0])

    df3 = pd.concat(odds2)

    df3[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')] = df3[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')].fillna(value='Home') 

    df3[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')] = df3[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')].replace(to_replace=['N', '@'], value=['Neutral', 'Away'])  

    df3.columns = df3.columns.to_flat_index()

    df3.reset_index()

    df3.drop(df3[df3[('Unnamed: 1_level_0', 'Tm')] == 'Tm'].index, inplace=True)

    df3 = df3.rename(columns={('Unnamed: 0_level_0', 'Rk'):'rk', ('Unnamed: 1_level_0', 'Tm'): 'team1',('Unnamed: 2_level_0', 'Year'): 'year',
        ('Unnamed: 3_level_0', 'Date'): 'date',('Unnamed: 4_level_0', 'Time'): 'time',('Unnamed: 5_level_0', 'LTime'): 'local_time', 
        ('Unnamed: 6_level_0', 'Unnamed: 6_level_1'): 'home_away',('Unnamed: 7_level_0', 'Opp'): 'team2',('Unnamed: 8_level_0', 'Week'): 'week',
        ('Unnamed: 9_level_0', 'G#'): 'Game_Number',('Unnamed: 10_level_0', 'Day'): 'day',('Unnamed: 11_level_0', 'Result'): 'win1?',
        ('Unnamed: 12_level_0', 'OT'): 'OT',('Vegas', 'Spread'): 'spread',('Vegas', 'vs. Line'): 'team1_covered_spread?',
        ('Vegas', 'Over/Under'): 'over_under',('Vegas', 'OU Result'): 'over_under_result?',('Scoring', 'TD'):'Total_TD1',
        ('Scoring', 'XPA'): 'XPA_1',('Scoring', 'XPM'): 'XPM_1',('Scoring', 'FGA'): 'FGA1',
        ('Scoring', 'FGM'): 'FGM1',('Scoring', '2PA'): '2PA1',('Scoring', '2PM'): '2PM2',
        ('Scoring', 'Sfty'): 'Sfty1',('Opp. Scoring', 'TD'): 'Total_TD2',('Opp. Scoring', 'XPA'): 'XPA2',
        ('Opp. Scoring', 'XPM'): 'XPM2',('Opp. Scoring', 'Att'): 'FGA2',('Opp. Scoring', 'Md'): 'FGM2',
        ('Opp. Scoring', 'Sfty'): 'Sfty2'})

    df4 = df3[['team1','year','date','time','local_time', 'home_away','team2','week','Game_Number',
            'day','win1?','OT','Total_TD1','XPA_1','XPM_1','FGA1', 'FGM1', '2PA1', '2PM2', 'Sfty1', 'Total_TD2', 'XPA2', 'XPM2', 'FGA2', 'FGM2', 'Sfty2']]

    df = df.drop(columns=['rk', 'year', 'local_time', 'day', 'game_duration'])

    df1 = df1.drop(columns=['rk', 'year', 'local_time', 'date','time', 'week', 'home_away', 'day','win1?', 'OT',
                        'spread', 'team1_covered_spread?', 'over_under','over_under_result?'])

    
    merge1 = df.merge(df1, on=['team1', 'team2', 'Game_Number'], how='left')

    merge1['week'] = merge1['week'].apply(lambda x: int(x))
    merge1['Game_Number'] = merge1['Game_Number'].apply(lambda x: int(x))



    penalties = []                                                                                                                                                                                                                                                                                                                                                                                                                           
    for i in range(0,300,100):
        url = url3
        penalties.append(pd.read_html(url3.format(i))[0])

    p_df = pd.concat(penalties)

    p_df[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')] = p_df[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')].fillna(value='Home') 

    p_df[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')] = p_df[('Unnamed: 6_level_0', 'Unnamed: 6_level_1')].replace(to_replace=['N', '@'], value=['Neutral', 'Away'])  

    p_df.columns = p_df.columns.to_flat_index()

    p_df.reset_index()

    p_df.drop(p_df[p_df[('Unnamed: 1_level_0', 'Tm')] == 'Tm'].index, inplace=True)

    p_df = p_df.rename(columns={('Unnamed: 1_level_0', 'Tm'): 'team1', ('Unnamed: 7_level_0', 'Opp'): 'team2', ('Unnamed: 8_level_0', 'Week'): 'week',
                                ('Unnamed: 9_level_0', 'G#'): 'Game_Number',('Penalties', 'Yds'): 'penalty_yards1',('Penalties', 'OppYds'): 'penalty_yards2'})


    new = p_df[['team1', 'team2', 'week', 'Game_Number', 'penalty_yards1', 'penalty_yards2']]

    new['week'] = new['week'].apply(lambda x: int(x))
    new['Game_Number'] = new['Game_Number'].apply(lambda x: int(x))

    merge2 = merge1.merge(new, on=['team1', 'team2', 'week', 'Game_Number'], how='left')


    new1 = df4[['team1','team2', 'week', 'Game_Number', 'Total_TD1', 'XPA_1','XPM_1', 'FGA1','FGM1', 
                'Sfty1', 'Total_TD2', 'XPA2','XPM2', 'FGA2', 'FGM2', 'Sfty2']]



    new1['week'] = new1['week'].apply(lambda x: int(x))
    new1['Game_Number'] = new1['Game_Number'].apply(lambda x: int(x))

    merge3 = merge2.merge(new1, on=['team1', 'team2', 'week', 'Game_Number'], how='left')

    m = merge3.copy()

    m['win1?'] = m['win1?'].apply(lambda x: x.split()[0]) 

    m['win1?'] = m['win1?'].replace(to_replace=['L', 'W', 'T'], value=[-1,1,0])

    m.replace(to_replace=['under', 'over', 'push'], value = [-1,1,0], inplace=True)

    m = m.fillna(value=0)

    m['OT'] = m['OT'].replace(to_replace='OT', value=1)

    m['team1_covered_spread?'] = m['team1_covered_spread?'].replace(to_replace=['not covered', 'covered', ], value = [0,1])

    return m



# 62 columns to floats because math
col_list = ['week', 'Game_Number',
       'win1?', 'OT', 'points_1', 'points_2', 'point_differential',
       'combined_points', 'spread', 'team1_covered_spread?', 'over_under',
       'over_under_result?', 'pass_completions1', 'pass_attempts1',
       'completion_percentage1', 'passing_yards1', 'passing_touchdowns1',
       'interceptions1', 'times_sacked1', 'sack_yards_lost1', 'qbr1',
       'rushing_attempts1', 'rushing_yards1', 'rushing_yards_per_attempt1',
       'rushing_touchdowns1', 'total_yards1', 'offensive_plays1',
       'yards_per_play_offense1', 'defensive_plays1',
       'yards_allowed_per_defensive_play1', 'turnovers_lost1', 
        'pass_completions2', 'pass_attempts2',
       'completion_percentage2', 'passing_yards2', 'passing_touchdowns2',
       'interceptions2', 'times_sacked2', 'sack_yards_lost2', 'qbr2',
       'rushing_attempts2', 'rushing_yards2', 'rushing_yards_per_attempt2',
       'rushing_touchdowns2', 'total_yards2', 'turnovers2', 'penalty_yards1',
       'penalty_yards2', 'Total_TD1', 'XPA_1', 'XPM_1', 'FGA1', 'FGM1', 
       'Sfty1', 'Total_TD2', 'XPA2', 'XPM2', 'FGA2', 'FGM2', 'Sfty2' ]

def text_to_num(text):
    return float(text)

def convert_into_float(data):
    data[col_list] = data[col_list].applymap(text_to_num)
    return data

# Time_of_possesion1 - returns a string like 'mm:ss'
# write a function to normalize time of possession to a ratio from 0 to 1
def top_ratio(text):
    return float(text.split(':')[0])/60 + float(text.split(':')[1])/3600
def time_of_possession_to_ratio(data):
    #converts time of possession into a ratio from 0 to 1
    data['time_of_possession1'] = data['time_of_possession1'].apply(lambda x: top_ratio(x))
    return data

m = time_of_possession_to_ratio(m)

def clean_data(data):
    # cleaner function and feature engineering to normalize statistics
    data['time_of_possession2'] = 1 - data['time_of_possession1']
    data['team2_covered_spread?'] = 1.0 - data['team1_covered_spread?']
    data['offensive_plays2'] = data['defensive_plays1']
    data['yards_per_play_offense2'] = data['total_yards2'] / data['offensive_plays2']
    data['defensive_plays2'] = data['offensive_plays1']
    data['yards_allowed_per_defensive_play2'] = data['total_yards1']/ data['defensive_plays2']
    data['passing_yards_per_attempt1'] = data[ 'passing_yards1'] / data['pass_attempts1']
    data['passing_yards_per_attempt2'] = data[ 'passing_yards2'] / data['pass_attempts2']
    data['home_away'] = data['home_away'].replace(to_replace=['Neutral', 'Away', 'Home'], 
                                       value=[0,-1,1])
    data['win2?'] = data['win1?'] * -1
    data['team2_covered_spread?'] = 1 - data['team1_covered_spread?']
    data['game_id'] = range(0,267)
    data = data.rename(columns={'home_away':'home_away1'})
    data['home_away2'] = data['home_away1'] * -1
    return data

def format_data(data):
    # this function reformats the dataframe so each team for each game has it's own row of data, they are linked together by the column game_id
    t1 = data[['team1', 'home_away1', 'team2', 'week', 'Game_Number', 'win1?', 'OT', 'points_1',
        'points_2', 'combined_points','spread', 'team1_covered_spread?', 'over_under',
        'over_under_result?', 'pass_completions1', 'pass_attempts1',
        'completion_percentage1', 'passing_yards1', 'passing_touchdowns1',
        'interceptions1', 'times_sacked1', 'sack_yards_lost1', 'qbr1', 'rushing_attempts1',
        'rushing_yards1', 'rushing_yards_per_attempt1', 'rushing_touchdowns1', 'total_yards1',
        'offensive_plays1','yards_per_play_offense1','defensive_plays1','yards_allowed_per_defensive_play1',
        'turnovers_lost1','time_of_possession1','penalty_yards1','Total_TD1','XPA_1','XPM_1','FGA1',
        'FGM1','Sfty1','passing_yards_per_attempt1','game_id']]

    t2 = data[['team2','home_away2','team1','week','Game_Number','win2?','OT','points_2',
        'points_1','combined_points','spread','team2_covered_spread?','over_under',
        'over_under_result?','pass_completions2','pass_attempts2','completion_percentage2',
        'passing_yards2','passing_touchdowns2','interceptions2','times_sacked2','sack_yards_lost2',
        'qbr2','rushing_attempts2','rushing_yards2','rushing_yards_per_attempt2',
        'rushing_touchdowns2','total_yards2','offensive_plays2','yards_per_play_offense2',
        'defensive_plays2','yards_allowed_per_defensive_play2','turnovers2','time_of_possession2',
        'penalty_yards2','Total_TD2','XPA2','XPM2','FGA2','FGM2','Sfty2',
        'passing_yards_per_attempt2', 'game_id']]

    t1a = t1.copy()
    t2a = t2.copy()


    t1a.columns=['team','home_away','opponent','week','game number','win?','OT','points_for','points_against',
            'combined_points','spread','covered_spread?','over_under','over_under_result?','pass_completions',
            'pass_attempts','completion_percentage','passing_yards','passing_touchdowns','interceptions','times_sacked',
            'sack_yards_lost','qbr','rushing_attempts','rushing_yards','rushing_yards_per_attempt','rushing_touchdowns',
            'total_yards','offensive_plays','yards_per_play_offense','defensive_plays','yards_allowed_per_defensive_play',
            'turnovers','time_of_possession','penalty_yards','Total_TD','XPA','XPM','FGA','FGM','Sfty',
            'passing_yards_per_attempt','game_id']

    t2a.columns=['team','home_away','opponent','week','game number','win?','OT','points_for','points_against',
            'combined_points','spread','covered_spread?','over_under','over_under_result?','pass_completions',
            'pass_attempts','completion_percentage','passing_yards','passing_touchdowns','interceptions','times_sacked',
            'sack_yards_lost','qbr','rushing_attempts','rushing_yards','rushing_yards_per_attempt','rushing_touchdowns',
            'total_yards','offensive_plays','yards_per_play_offense','defensive_plays','yards_allowed_per_defensive_play',
            'turnovers','time_of_possession','penalty_yards','Total_TD','XPA','XPM','FGA','FGM','Sfty',
            'passing_yards_per_attempt','game_id']

    frames = [t1a, t2a]
    game_stats = pd.concat(frames)
    return game_stats


def feature_engineer_data(data):
    data['win?'] = data['win?'].replace(to_replace=[-1.,  1.,  0.], value=[0,1,0])
    data['week'] = data['week'].apply(lambda x: int(x))
    data= data.sort_values(by=['week', 'team'])
    data['total_wins'] = data.groupby('team')['win?'].cumsum()

    data['tie'] = data['points_for'] == data['points_against']
    data['loss'] = data['points_against'] > data['points_for']

    data['tie'] = data['tie'].replace(to_replace=[False, True], value=[0,1])
    data['loss'] = data['loss'].replace(to_replace=[False, True], value=[0,1])

    data['total_losses'] = data.groupby('team')['loss'].cumsum()
    data['total_ties'] = data.groupby('team')['tie'].cumsum()

    td2 = {'ARI':'CARDINALS', 'ATL':'FALCONS', 'BAL':'RAVENS', 'BUF':'BILLS', 'CAR':'PANTHERS', 'CHI':'BEARS', 'CIN':'BENGALS', 
        'CLE':'BROWNS', 'DAL':'COWBOYS', 'DEN':'BRONCOS', 'DET':'LIONS', 'GNB':'PACKERS', 'HOU':'TEXANS', 'IND':'COLTS', 
        'JAX':'JAGUARS', 'KAN':'CHIEFS', 'LAC':'CHARGERS', 'LAR': 'RAMS', 'MIA': 'DOLPHINS', 'MIN':'VIKINGS', 
        'NOR':'SAINTS', 'NWE':'PATRIOTS', 'NYG':'GIANTS', 'NYJ':'JETS', 'OAK':'RAIDERS', 'PHI':'EAGLES', 'PIT':'STEELERS',
        'SEA':'SEAHAWKS', 'SFO':'49ERS', 'TAM':'BUCCANEERS', 'TEN':'TITANS', 'WAS':'REDSKINS'}

    data['team'] = data['team'].replace(to_replace=td2.keys(), value=td2.values())
    data['opponent'] = data['opponent'].replace(to_replace=td2.keys(), value=td2.values())

    return data