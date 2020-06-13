
from scraper_1 import scrape_stats, top_ratio, time_of_possession_to_ratio, text_to_num, convert_into_float, clean_data
# do not yet run the following 7 lines of code as of 6/13/20
url2 = """https://www.pro-football-reference.com/play-index/tgl_finder.cgi?request=1&match=game&year_min=2019&year_max=2019&game_type=R&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99&temperature_gtlt=lt&c1stat=points&c1comp=gte&c2stat=pass_yds&c2comp=gte&c3stat=rush_yds&c3comp=gte&c4stat=turnovers&c4comp=gte&c5stat=fgm&c5comp=gt&c5val=1.0&order_by=game_date&offset={}"""

url3 = """https://www.pro-football-reference.com/play-index/tgl_finder.cgi?request=1&match=game&year_min=2019&year_max=2019&game_type=R&game_num_min=0&game_num_max=99&week_num_min=0&week_num_max=99&temperature_gtlt=lt&c1stat=penalties_yds&c1comp=gte&c5stat=fgm&c5comp=gt&c5val=1.0&order_by=game_date&offset={}"""

df = scrape_stats(url2, url3)

df = time_of_possession_to_ratio(df)
df = convert_into_float(df)
df = clean_data(df)

# working from cs2take2.ipynb pull that stats file from previous capstone, fix the scraper_1 file to clean this up

df = pd.read_csv('backup_stats5312020.csv')

### now set the data up to build the training and testing sets, the model will at first be trained on the weeks 1 through 4 of the NFL season,
# then it will be tested on week5, the training set will build to 6 games, to account for teams having bye weeks from weeks 5-12 in the season

# pull each individual week of the season for the testing set

week_5 = df[df['week']== 5 ].fillna(value=0) # 2 teams have bye weeks, 15 games, 30 teams play
week_6 = df[df['week']== 6 ].fillna(value=0) # 4 teams bye, 14 games, 28 teams
week_7 = df[df['week']== 7 ].fillna(value=0) # 4 teams bye, 14 games, 28 teams
week_8 = df[df['week']== 8 ].fillna(value=0) # 2 teams bye, 15 games, 30 teams
week_9 = df[df['week']== 9 ].fillna(value=0) # 4 teams bye, 14 games, 28 teams
week_10 = df[df['week']== 10 ].fillna(value=0) # 6 teams bye, 13 games, 26 teams
week_11 = df[df['week']== 11 ].fillna(value=0) # 4 teams bye, 14 games, 28 teams
week_12 = df[df['week']== 12 ].fillna(value=0) # 4 teams bye, 14 games, 28 teams
week_13 = df[df['week']== 13 ].fillna(value=0)
week_14 = df[df['week']== 14 ].fillna(value=0)
week_15 = df[df['week']== 15 ].fillna(value=0)
week_16 = df[df['week']== 16 ].fillna(value=0)
week_17 = df[df['week']== 17 ].fillna(value=0)



# now build the training set, 9 weeks of staggered by weeks from weeks 4 through 12, I wanted to account for this by starting the model seeing 
# 4 prior weeks, build up to 6, and hold it constant. This should be back tested against other seasons to see if it should drop back down to
# 4 games by the end of the season.

w1_4 = df[df['week']<=4].fillna(value=0) # first 4 weeks of the season 0 teams have bye weeks 1-3, 16 games each week, 15 games week 4
w1_5 = df[df['week']<=5].fillna(value=0) 
w1_6 = df[df['week']<=6].fillna(value=0) 
w2_7 = df[df['week'].between(2,7)].fillna(value=0) 
w3_8 = df[df['week'].between(3,8)].fillna(value=0)
w4_9 = df[df['week'].between(4,9)].fillna(value=0)
w5_10 = df[df['week'].between(5,10)].fillna(value=0)
w6_11 = df[df['week'].between(6,11)].fillna(value=0)
w7_12 = df[df['week'].between(7,12)].fillna(value=0)
w8_13 = df[df['week'].between(8,13)].fillna(value=0)
w9_14 = df[df['week'].between(9,14)].fillna(value=0)
w10_15 = df[df['week'].between(10,15)].fillna(value=0)
w11_16 = df[df['week'].between(11,16)].fillna(value=0)

# name them for consistency
w5_train = w1_4
w6_train = w1_5
w7_train = w1_6
w8_train = w2_7
w9_train = w3_8
w10_train = w4_9
w11_train = w5_10
w12_train = w6_11
w13_train = w7_12
w14_train = w8_13
w15_train = w9_14
w16_train = w10_15
w17_train = w11_16

# to account for unseen games, use the average from each training set as X_test, the following will rebuild the dataframes
# with the naming convention avgs5, avgs6 where the number represents the week it will be used for for the testing set

ta = []
teams = list(week_5['team'].unique())
for team in teams:
    avg = w5_train[w5_train['team']==team].mean()
    ta.append(avg)
avgs5 = pd.concat(ta, keys=w5_train['team'].unique())
avgs5 = avgs5.unstack(level=-1)

ta = []
teams = list(week_6['team'].unique())
for team in teams:
    avg = w6_train[w6_train['team']==team].mean()
    ta.append(avg)
avgs6 = pd.concat(ta, keys=w6_train['team'].unique())
avgs6 = avgs6.unstack(level=-1)

ta = []
teams = list(week_7['team'].unique())
for team in teams:
    avg = w7_train[w7_train['team']==team].mean()
    ta.append(avg)
avgs7 = pd.concat(ta, keys=w7_train['team'].unique())
avgs7 = avgs7.unstack(level=-1)

ta = []
teams = list(week_8['team'].unique())
for team in teams:
    avg = w8_train[w8_train['team']==team].mean()
    ta.append(avg)
avgs8 = pd.concat(ta, keys=w8_train['team'].unique())
avgs8 = avgs8.unstack(level=-1)

ta = []
teams = list(week_9['team'].unique())
for team in teams:
    avg = w9_train[w9_train['team']==team].mean()
    ta.append(avg)
avgs9 = pd.concat(ta, keys=w9_train['team'].unique())
avgs9 = avgs9.unstack(level=-1)

ta = []
teams = list(week_10['team'].unique())
for team in teams:
    avg = w10_train[w10_train['team']==team].mean()
    ta.append(avg)
avgs10 = pd.concat(ta, keys=w10_train['team'].unique())
avgs10 = avgs10.unstack(level=-1)

ta = []
teams = list(week_11['team'].unique())
for team in teams:
    avg = w11_train[w11_train['team']==team].mean()
    ta.append(avg)
avgs11 = pd.concat(ta, keys=w11_train['team'].unique())
avgs11 = avgs11.unstack(level=-1)

ta = []
teams = list(week_12['team'].unique())
for team in teams:
    avg = w12_train[w12_train['team']==team].mean()
    ta.append(avg)
avgs12 = pd.concat(ta, keys=w12_train['team'].unique())
avgs12 = avgs12.unstack(level=-1)

ta = []
teams = list(week_13['team'].unique())
for team in teams:
    avg = w13_train[w13_train['team']==team].mean()
    ta.append(avg)
avgs13 = pd.concat(ta, keys=w13_train['team'].unique())
avgs13 = avgs13.unstack(level=-1)

ta = []
teams = list(week_14['team'].unique())
for team in teams:
    avg = w14_train[w14_train['team']==team].mean()
    ta.append(avg)
avgs14 = pd.concat(ta, keys=w14_train['team'].unique())
avgs14 = avgs14.unstack(level=-1)

ta = []
teams = list(week_15['team'].unique())
for team in teams:
    avg = w15_train[w15_train['team']==team].mean()
    ta.append(avg)
avgs15 = pd.concat(ta, keys=w15_train['team'].unique())
avgs15 = avgs15.unstack(level=-1)

ta = []
teams = list(week_16['team'].unique())
for team in teams:
    avg = w16_train[w16_train['team']==team].mean()
    ta.append(avg)
avgs16 = pd.concat(ta, keys=w16_train['team'].unique())
avgs16 = avgs16.unstack(level=-1)

ta = []
teams = list(week_17['team'].unique())
for team in teams:
    avg = w17_train[w17_train['team']==team].mean()
    ta.append(avg)
avgs17 = pd.concat(ta, keys=w17_train['team'].unique())
avgs17 = avgs17.unstack(level=-1)



### the following are set up to train and test for money lines, to predict winning, can uncomment spreads and get rid of wins to change that ####

y_train_w5 = w5_train['win?']
#y_train_w5 = w5_train['covered_spread?']
X_train_w5 = w5_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_test_w5 = week_5['win?']
#y_test_w5 = week_5['covered_spread?']
X_test_w5 = avgs5[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_train_w6 = w6_train['win?']
#y_train_w6 = w6_train['covered_spread?']
X_train_w6 = w6_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_test_w6 = week_6['win?']
#y_test_w6 = week_6['covered_spread?']
X_test_w6 = avgs6[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_train_w7 = w7_train['win?']
#y_train_w7 = w7_train['covered_spread?']
X_train_w7 = w7_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_test_w7 = week_7['win?']
#y_test_w7 = week_7['covered_spread?']
X_test_w7 = avgs7[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_train_w8 = w8_train['win?']
#y_train_w8 = w8_train['covered_spread?']
X_train_w8 = w8_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_test_w8 = week_8['win?']
#y_test_w8 = week_8['covered_spread?']
X_test_w8 = avgs8[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_train_w9 = w9_train['win?']
#y_train_w9 = w9_train['covered_spread?']
X_train_w9 = w9_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_test_w9 = week_9['win?']
#y_test_w9 = week_9['covered_spread?']
X_test_w9 = avgs9[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_train_w10 = w10_train['win?']
#y_train_w10 = w10_train['covered_spread?']
X_train_w10 = w10_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_test_w10 = week_10['win?']
#y_test_w10 = week_10['covered_spread?']
X_test_w10 = avgs10[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_train_w11 = w11_train['win?']
#y_train_w11 = w11_train['covered_spread?']
X_train_w11 = w11_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_test_w11 = week_11['win?']
#y_test_w11 = week_11['covered_spread?']
X_test_w11 = avgs11[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_train_w12 = w12_train['win?']
#y_train_w12 = w12_train['covered_spread?']
X_train_w12 = w12_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_test_w12 = week_12['win?']
#y_test_w12 = week_12['covered_spread?']
X_test_w12 = avgs12[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_train_w13 = w13_train['win?']
#y_train_w13 = w13_train['covered_spread?']
X_train_w13 = w13_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_test_w13 = week_13['win?']
#y_test_w13 = week_13['covered_spread?']
X_test_w13 = avgs13[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_train_w14 = w14_train['win?']
#y_train_w14 = w14_train['covered_spread?']
X_train_w14 = w14_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_test_w14 = week_14['win?']
#y_test_w14 = week_14['covered_spread?']
X_test_w14 = avgs14[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_train_w15 = w15_train['win?']
#y_train_w15 = w15_train['covered_spread?']
X_train_w15 = w15_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_test_w15 = week_15['win?']
#y_test_w15 = week_15['covered_spread?']
X_test_w15 = avgs15[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_train_w16 = w16_train['win?']
#y_train_w16 = w16_train['covered_spread?']
X_train_w16 = w16_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_test_w16 = week_16['win?']
#y_test_w16 = week_16['covered_spread?']
X_test_w16 = avgs16[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_train_w17 = w17_train['win?']
#y_train_w17 = w17_train['covered_spread?']
X_train_w17 = w17_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

y_test_w17 = week_17['win?']
#y_test_w17 = week_17['covered_spread?']
X_test_w17 = avgs17[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

############################################################################################
############################################################################################
#y_train_w4 = w4_train['win?']
y_train_w4 = w4_train['covered_spread?']
X_train_w4 = w4_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM',
                       'points_for', 'points_against']]

#y_test_w4 = week_4['win?']
y_test_w4 = week_4['covered_spread?']
X_test_w4 = avgs4[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_train_w5 = w5_train['win?']
y_train_w5 = w5_train['covered_spread?']
X_train_w5 = w5_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_test_w5 = week_5['win?']
y_test_w5 = week_5['covered_spread?']
X_test_w5 = avgs5[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_train_w6 = w6_train['win?']
y_train_w6 = w6_train['covered_spread?']
X_train_w6 = w6_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_test_w6 = week_6['win?']
y_test_w6 = week_6['covered_spread?']
X_test_w6 = avgs6[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_train_w7 = w7_train['win?']
y_train_w7 = w7_train['covered_spread?']
X_train_w7 = w7_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_test_w7 = week_7['win?']
y_test_w7 = week_7['covered_spread?']
X_test_w7 = avgs7[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_train_w8 = w8_train['win?']
y_train_w8 = w8_train['covered_spread?']
X_train_w8 = w8_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_test_w8 = week_8['win?']
y_test_w8 = week_8['covered_spread?']
X_test_w8 = avgs8[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_train_w9 = w9_train['win?']
y_train_w9 = w9_train['covered_spread?']
X_train_w9 = w9_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_test_w9 = week_9['win?']
y_test_w9 = week_9['covered_spread?']
X_test_w9 = avgs9[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_train_w10 = w10_train['win?']
y_train_w10 = w10_train['covered_spread?']
X_train_w10 = w10_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_test_w10 = week_10['win?']
y_test_w10 = week_10['covered_spread?']
X_test_w10 = avgs10[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_train_w11 = w11_train['win?']
y_train_w11 = w11_train['covered_spread?']
X_train_w11 = w11_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_test_w11 = week_11['win?']
y_test_w11 = week_11['covered_spread?']
X_test_w11 = avgs11[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_train_w12 = w12_train['win?']
y_train_w12 = w12_train['covered_spread?']
X_train_w12 = w12_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_test_w12 = week_12['win?']
y_test_w12 = week_12['covered_spread?']
X_test_w12 = avgs12[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_train_w13 = w13_train['win?']
y_train_w13 = w13_train['covered_spread?']
X_train_w13 = w13_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_test_w13 = week_13['win?']
y_test_w13 = week_13['covered_spread?']
X_test_w13 = avgs13[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_train_w14 = w14_train['win?']
y_train_w14 = w14_train['covered_spread?']
X_train_w14 = w14_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_test_w14 = week_14['win?']
y_test_w14 = week_14['covered_spread?']
X_test_w14 = avgs14[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_train_w15 = w15_train['win?']
y_train_w15 = w15_train['covered_spread?']
X_train_w15 = w15_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_test_w15 = week_15['win?']
y_test_w15 = week_15['covered_spread?']
X_test_w15 = avgs15[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_train_w16 = w16_train['win?']
y_train_w16 = w16_train['covered_spread?']
X_train_w16 = w16_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_test_w16 = week_16['win?']
y_test_w16 = week_16['covered_spread?']
X_test_w16 = avgs16[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_train_w17 = w17_train['win?']
y_train_w17 = w17_train['covered_spread?']
X_train_w17 = w17_train[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]

#y_test_w17 = week_17['win?']
y_test_w17 = week_17['covered_spread?']
X_test_w17 = avgs17[['home', 'away', 'yards_per_play_offense', 
                 'yards_allowed_per_defensive_play', 'turnovers_lost',
                 'times_sacked', 'total_wins', 'total_losses', 'spread', 
                 'favorite', 'underdog', 'time_of_possession','penalty_yards','FGM','points_for', 'points_against']]







model4 = GradientBoostingClassifier(learning_rate=0.125, n_estimators=200 )
model4.fit(X_train_w4, y_train_w4)

model5 = GradientBoostingClassifier(learning_rate=0.125, n_estimators=200)
model5.fit(X_train_w5, y_train_w5)

model6 = GradientBoostingClassifier(learning_rate=0.125, n_estimators=200)
model6.fit(X_train_w6, y_train_w6)

model7 = GradientBoostingClassifier(learning_rate=0.125, n_estimators=200)
model7.fit(X_train_w7, y_train_w7)

model8 = GradientBoostingClassifier(learning_rate=0.125, n_estimators=200)
model8.fit(X_train_w8, y_train_w8)

model9 = GradientBoostingClassifier(learning_rate=0.125, n_estimators=200)
model9.fit(X_train_w9, y_train_w9)

model10 = GradientBoostingClassifier(learning_rate=0.125, n_estimators=200)
model10.fit(X_train_w10, y_train_w10)

model11 = GradientBoostingClassifier(learning_rate=0.125, n_estimators=200)
model11.fit(X_train_w11, y_train_w11)

model12 = GradientBoostingClassifier(learning_rate=0.125, n_estimators=200)
model12.fit(X_train_w12, y_train_w12)

model13 = GradientBoostingClassifier(learning_rate=0.125, n_estimators=200)
model13.fit(X_train_w13, y_train_w13)

model14 = GradientBoostingClassifier(learning_rate=0.125, n_estimators=200)
model14.fit(X_train_w14, y_train_w14)

model15 = GradientBoostingClassifier(learning_rate=0.125, n_estimators=200)
model15.fit(X_train_w15, y_train_w15)

model16 = GradientBoostingClassifier(learning_rate=0.125, n_estimators=200)
model16.fit(X_train_w16, y_train_w16)

model17 = GradientBoostingClassifier(learning_rate=0.125, n_estimators=200)
model17.fit(X_train_w17, y_train_w17)



####### use this code for the win, go to line 539 to use for spread #####

targa5 = model5.predict_proba(X_test_w5)[:,1:]
ta5 = week_5['team'].values.reshape(30,1)
oa5 = week_5['opponent'].values.reshape(30,1)
aa5 = week_5['win?'].values.reshape(30,1)
gida5 = week_5['game_id'].values.reshape(30,1)
fav5 = week_5['favorite'].values.reshape(30,1)

targa6 = model6.predict_proba(X_test_w6)[:,1:]
ta6 = week_6['team'].values.reshape(28,1)
oa6 = week_6['opponent'].values.reshape(28,1)
aa6 = week_6['win?'].values.reshape(28,1)
gida6 = week_6['game_id'].values.reshape(28,1)
fav6 = week_6['favorite'].values.reshape(28,1)

targa7 = model7.predict_proba(X_test_w7)[:,1:]
ta7 = week_7['team'].values.reshape(28,1)
oa7 = week_7['opponent'].values.reshape(28,1)
aa7 = week_7['win?'].values.reshape(28,1)
gida7 = week_7['game_id'].values.reshape(28,1)
fav7 = week_7['favorite'].values.reshape(28,1)

targa8 = model8.predict_proba(X_test_w8)[:,1:]
ta8 = week_8['team'].values.reshape(30,1)
oa8 = week_8['opponent'].values.reshape(30,1)
aa8 = week_8['win?'].values.reshape(30,1)
gida8 = week_8['game_id'].values.reshape(30,1)
fav8 = week_8['favorite'].values.reshape(30,1)

targa9 = model9.predict_proba(X_test_w9)[:,1:]
ta9 = week_9['team'].values.reshape(28,1)
oa9 = week_9['opponent'].values.reshape(28,1)
aa9 = week_9['win?'].values.reshape(28,1)
gida9 = week_9['game_id'].values.reshape(28,1)
fav9 = week_9['favorite'].values.reshape(28,1)

targa10 = model10.predict_proba(X_test_w10)[:,1:]
ta10 = week_10['team'].values.reshape(26,1)
oa10 = week_10['opponent'].values.reshape(26,1)
aa10 = week_10['win?'].values.reshape(26,1)
gida10 = week_10['game_id'].values.reshape(26,1)
fav10 = week_10['favorite'].values.reshape(26,1)

targa11 = model11.predict_proba(X_test_w11)[:,1:]
ta11 = week_11['team'].values.reshape(28,1)
oa11 = week_11['opponent'].values.reshape(28,1)
aa11 = week_11['win?'].values.reshape(28,1)
gida11 = week_11['game_id'].values.reshape(28,1)
fav11 = week_11['favorite'].values.reshape(28,1)

targa12 = model12.predict_proba(X_test_w12)[:,1:]
ta12 = week_12['team'].values.reshape(28,1)
oa12 = week_12['opponent'].values.reshape(28,1)
aa12 = week_12['win?'].values.reshape(28,1)
gida12 = week_12['game_id'].values.reshape(28,1)
fav12 = week_12['favorite'].values.reshape(28,1)

targa13 = model13.predict_proba(X_test_w13)[:,1:]
ta13 = week_13['team'].values.reshape(32,1)
oa13 = week_13['opponent'].values.reshape(32,1)
aa13 = week_13['win?'].values.reshape(32,1)
gida13 = week_13['game_id'].values.reshape(32,1)
fav13 = week_13['favorite'].values.reshape(32,1)

targa14 = model14.predict_proba(X_test_w14)[:,1:]
ta14 = week_14['team'].values.reshape(32,1)
oa14 = week_14['opponent'].values.reshape(32,1)
aa14 = week_14['win?'].values.reshape(32,1)
gida14 = week_14['game_id'].values.reshape(32,1)
fav14 = week_14['favorite'].values.reshape(32,1)

targa15 = model15.predict_proba(X_test_w15)[:,1:]
ta15 = week_15['team'].values.reshape(32,1)
oa15 = week_15['opponent'].values.reshape(32,1)
aa15 = week_15['win?'].values.reshape(32,1)
gida15 = week_15['game_id'].values.reshape(32,1)
fav15 = week_15['favorite'].values.reshape(32,1)

targa16 = model16.predict_proba(X_test_w16)[:,1:]
ta16 = week_16['team'].values.reshape(32,1)
oa16 = week_16['opponent'].values.reshape(32,1)
aa16 = week_16['win?'].values.reshape(32,1)
gida16 = week_16['game_id'].values.reshape(32,1)
fav16 = week_16['favorite'].values.reshape(32,1)

targa17 = model17.predict_proba(X_test_w17)[:,1:]
ta17 = week_17['team'].values.reshape(32,1)
oa17 = week_17['opponent'].values.reshape(32,1)
aa17 = week_17['win?'].values.reshape(32,1)
gida17 = week_17['game_id'].values.reshape(32,1)
fav17 = week_17['favorite'].values.reshape(32,1)


####### use above for wins, use code below for spread####

targ2 = model4.predict_proba(X_test_w4)[:,1:]
t = week_4['team'].values.reshape(30,1)
o = week_4['opponent'].values.reshape(30,1)
a = week_4['covered_spread?'].values.reshape(30,1)
gid = week_4['game_id'].values.reshape(30,1)
fav1 = week_4['favorite'].values.reshape(30,1)
spr1 = week_4['spread'].values.reshape(30,1)

targ5 = model5.predict_proba(X_test_w5)[:,1:]
t5 = week_5['team'].values.reshape(30,1)
o5 = week_5['opponent'].values.reshape(30,1)
a5 = week_5['covered_spread?'].values.reshape(30,1)
gid5 = week_5['game_id'].values.reshape(30,1)
fav5 = week_5['favorite'].values.reshape(30,1)
spr5 = week_5['spread'].values.reshape(30,1)

targ6 = model6.predict_proba(X_test_w6)[:,1:]
t6 = week_6['team'].values.reshape(28,1)
o6 = week_6['opponent'].values.reshape(28,1)
a6 = week_6['covered_spread?'].values.reshape(28,1)
gid6 = week_6['game_id'].values.reshape(28,1)
fav6 = week_6['favorite'].values.reshape(28,1)
spr6 = week_6['spread'].values.reshape(28,1)

targ7 = model7.predict_proba(X_test_w7)[:,1:]
t7 = week_7['team'].values.reshape(28,1)
o7 = week_7['opponent'].values.reshape(28,1)
a7 = week_7['covered_spread?'].values.reshape(28,1)
gid7 = week_7['game_id'].values.reshape(28,1)
fav7 = week_7['favorite'].values.reshape(28,1)
spr7 = week_7['spread'].values.reshape(28,1)

targ8 = model8.predict_proba(X_test_w8)[:,1:]
t8 = week_8['team'].values.reshape(30,1)
o8 = week_8['opponent'].values.reshape(30,1)
a8 = week_8['covered_spread?'].values.reshape(30,1)
gid8 = week_8['game_id'].values.reshape(30,1)
fav8 = week_8['favorite'].values.reshape(30,1)
spr8 = week_8['spread'].values.reshape(30,1)

targ9 = model9.predict_proba(X_test_w9)[:,1:]
t9 = week_9['team'].values.reshape(28,1)
o9 = week_9['opponent'].values.reshape(28,1)
a9 = week_9['covered_spread?'].values.reshape(28,1)
gid9 = week_9['game_id'].values.reshape(28,1)
fav9 = week_9['favorite'].values.reshape(28,1)
spr9 = week_9['spread'].values.reshape(28,1)

targ10 = model10.predict_proba(X_test_w10)[:,1:]
t10 = week_10['team'].values.reshape(26,1)
o10 = week_10['opponent'].values.reshape(26,1)
a10 = week_10['covered_spread?'].values.reshape(26,1)
gid10 = week_10['game_id'].values.reshape(26,1)
fav10 = week_10['favorite'].values.reshape(26,1)
spr10 = week_10['spread'].values.reshape(26,1)

targ11 = model11.predict_proba(X_test_w11)[:,1:]
t11 = week_11['team'].values.reshape(28,1)
o11 = week_11['opponent'].values.reshape(28,1)
a11 = week_11['covered_spread?'].values.reshape(28,1)
gid11 = week_11['game_id'].values.reshape(28,1)
fav11 = week_11['favorite'].values.reshape(28,1)
spr11 = week_11['spread'].values.reshape(28,1)

targ12 = model12.predict_proba(X_test_w12)[:,1:]
t12 = week_12['team'].values.reshape(28,1)
o12 = week_12['opponent'].values.reshape(28,1)
a12 = week_12['covered_spread?'].values.reshape(28,1)
gid12 = week_12['game_id'].values.reshape(28,1)
fav12 = week_12['favorite'].values.reshape(28,1)
spr12 = week_12['spread'].values.reshape(28,1)

targ13 = model13.predict_proba(X_test_w13)[:,1:]
t13 = week_13['team'].values.reshape(32,1)
o13 = week_13['opponent'].values.reshape(32,1)
a13 = week_13['covered_spread?'].values.reshape(32,1)
gid13 = week_13['game_id'].values.reshape(32,1)
fav13 = week_13['favorite'].values.reshape(32,1)
spr13 = week_13['spread'].values.reshape(32,1)

targ14 = model14.predict_proba(X_test_w14)[:,1:]
t14 = week_14['team'].values.reshape(32,1)
o14 = week_14['opponent'].values.reshape(32,1)
a14 = week_14['covered_spread?'].values.reshape(32,1)
gid14 = week_14['game_id'].values.reshape(32,1)
fav14 = week_14['favorite'].values.reshape(32,1)
spr14 = week_14['spread'].values.reshape(32,1)

targ15 = model15.predict_proba(X_test_w15)[:,1:]
t15 = week_15['team'].values.reshape(32,1)
o15 = week_15['opponent'].values.reshape(32,1)
a15 = week_15['covered_spread?'].values.reshape(32,1)
gid15 = week_15['game_id'].values.reshape(32,1)
fav15 = week_15['favorite'].values.reshape(32,1)
spr15 = week_15['spread'].values.reshape(32,1)

targ16 = model16.predict_proba(X_test_w16)[:,1:]
t16 = week_16['team'].values.reshape(32,1)
o16 = week_16['opponent'].values.reshape(32,1)
a16 = week_16['covered_spread?'].values.reshape(32,1)
gid16 = week_16['game_id'].values.reshape(32,1)
fav16 = week_16['favorite'].values.reshape(32,1)
spr16 = week_16['spread'].values.reshape(32,1)

targ17 = model17.predict_proba(X_test_w17)[:,1:]
t17 = week_17['team'].values.reshape(32,1)
o17 = week_17['opponent'].values.reshape(32,1)
a17 = week_17['covered_spread?'].values.reshape(32,1)
gid17 = week_17['game_id'].values.reshape(32,1)
fav17 = week_17['favorite'].values.reshape(32,1)
spr17 = week_17['spread'].values.reshape(32,1)




#### use thee below code for win go to 698 for spread #####

result_5= pd.DataFrame(np.hstack([ta5, oa5, targa5, aa5, gida5, fav5]), columns=['team','opp',
                    'proba_team_won', 'team_won', 'game_id', 'favorite'])
result_6= pd.DataFrame(np.hstack([ta6, oa6, targa6, aa6, gida6, fav6]), columns=['team','opp',
                    'proba_team_won', 'team_won', 'game_id', 'favorite'])

result_7= pd.DataFrame(np.hstack([ta7, oa7, targa7, aa7, gida7, fav7]), columns=['team','opp',
                    'proba_team_won', 'team_won', 'game_id', 'favorite'])

result_8= pd.DataFrame(np.hstack([ta8, oa8, targa8, aa8, gida8, fav8]), columns=['team','opp',
                    'proba_team_won', 'team_won', 'game_id', 'favorite'])

result_9= pd.DataFrame(np.hstack([ta9, oa9, targa9, aa9, gida9, fav9]), columns=['team','opp',
                    'proba_team_won', 'team_won', 'game_id', 'favorite'])

result_10= pd.DataFrame(np.hstack([ta10, oa10, targa10, aa10, gida10, fav10]), columns=['team','opp',
                    'proba_team_won', 'team_won', 'game_id', 'favorite'])

result_11= pd.DataFrame(np.hstack([ta11, oa11, targa11, aa11, gida11, fav11]), columns=['team','opp',
                    'proba_team_won', 'team_won', 'game_id', 'favorite'])

result_12= pd.DataFrame(np.hstack([ta12, oa12, targa12, aa12, gida12, fav12]), columns=['team','opp',
                    'proba_team_won', 'team_won', 'game_id', 'favorite'])

result_13= pd.DataFrame(np.hstack([ta13, oa13, targa13, aa13, gida13, fav13]), columns=['team','opp',
                    'proba_team_won', 'team_won', 'game_id', 'favorite'])

result_14= pd.DataFrame(np.hstack([ta14, oa14, targa14, aa14, gida14, fav14]), columns=['team','opp',
                    'proba_team_won', 'team_won', 'game_id', 'favorite'])

result_15= pd.DataFrame(np.hstack([ta15, oa15, targa15, aa15, gida15, fav15]), columns=['team','opp',
                    'proba_team_won', 'team_won', 'game_id', 'favorite'])

result_16= pd.DataFrame(np.hstack([ta16, oa16, targa16, aa16, gida16, fav16]), columns=['team','opp',
                    'proba_team_won', 'team_won', 'game_id', 'favorite'])
result_17= pd.DataFrame(np.hstack([ta17, oa17, targa17, aa17, gida17, fav17]), columns=['team','opp',
                    'proba_team_won', 'team_won', 'game_id', 'favorite'])

####spread results ###

result5= pd.DataFrame(np.hstack([t5, o5, targ5, a5, gid5, fav5, spr5]), columns=['team','opp',
                    'proba_team_covered', 'team_covered', 'game_id', 'favorite', 'spread'])

result6= pd.DataFrame(np.hstack([t6, o6, targ6, a6, gid6, fav6, spr6]), columns=['team','opp',
                    'proba_team_covered', 'team_covered', 'game_id', 'favorite', 'spread'])

result7= pd.DataFrame(np.hstack([t7, o7, targ7, a7, gid7, fav7, spr7]), columns=['team','opp',
                    'proba_team_covered', 'team_covered', 'game_id', 'favorite', 'spread'])

result8= pd.DataFrame(np.hstack([t8, o8, targ8, a8, gid8, fav8, spr8]), columns=['team','opp',
                    'proba_team_covered', 'team_covered', 'game_id', 'favorite', 'spread'])

result9= pd.DataFrame(np.hstack([t9, o9, targ9, a9, gid9, fav9, spr9]), columns=['team','opp',
                    'proba_team_covered', 'team_covered', 'game_id', 'favorite', 'spread'])

result10= pd.DataFrame(np.hstack([t10, o10, targ10, a10, gid10, fav10, spr10]), columns=['team','opp',
                    'proba_team_covered', 'team_covered', 'game_id', 'favorite', 'spread'])

result11= pd.DataFrame(np.hstack([t11, o11, targ11, a11, gid11, fav11, spr11]), columns=['team','opp',
                    'proba_team_covered', 'team_covered', 'game_id', 'favorite', 'spread'])

result12= pd.DataFrame(np.hstack([t12, o12, targ12, a12, gid12, fav12, spr12]), columns=['team','opp',
                    'proba_team_covered', 'team_covered', 'game_id', 'favorite', 'spread'])

result13= pd.DataFrame(np.hstack([t13, o13, targ13, a13, gid13, fav13, spr13]), columns=['team','opp',
                    'proba_team_covered', 'team_covered', 'game_id', 'favorite', 'spread'])

result14= pd.DataFrame(np.hstack([t14, o14, targ14, a14, gid14, fav14, spr14]), columns=['team','opp',
                    'proba_team_covered', 'team_covered', 'game_id', 'favorite', 'spread'])

result15= pd.DataFrame(np.hstack([t15, o15, targ15, a15, gid15, fav15, spr15]), columns=['team','opp',
                    'proba_team_covered', 'team_covered', 'game_id', 'favorite', 'spread'])

result16= pd.DataFrame(np.hstack([t16, o16, targ16, a16, gid16, fav16, spr16]), columns=['team','opp',
                    'proba_team_covered', 'team_covered', 'game_id', 'favorite', 'spread'])
result17= pd.DataFrame(np.hstack([t17, o17, targ17, a17, gid17, fav17, spr17]), columns=['team','opp',
                    'proba_team_covered', 'team_covered', 'game_id', 'favorite', 'spread'])


###run these for win results, the following lines of code copy and rebuild the dataframe to get rid of duplicates
#sort by game_id - this will bring all the games together
result_5 = result_5.sort_values(by=['game_id'])
result_6 = result_6.sort_values(by=['game_id'])
result_7 = result_7.sort_values(by=['game_id'])
result_8 = result_8.sort_values(by=['game_id'])
result_9 = result_9.sort_values(by=['game_id'])
result_10 = result_10.sort_values(by=['game_id'])
result_11 = result_11.sort_values(by=['game_id'])
result_12 = result_12.sort_values(by=['game_id'])
result_13 = result_13.sort_values(by=['game_id'])
result_14 = result_14.sort_values(by=['game_id'])
result_15 = result_15.sort_values(by=['game_id'])
result_16 = result_16.sort_values(by=['game_id'])
result_17 = result_17.sort_values(by=['game_id'])

#make copies with new names and the following columns

n_5 = result_5[['team', 'proba_team_won','team_won','game_id', 'favorite']]
n_6 = result_6[['team', 'proba_team_won','team_won','game_id', 'favorite']]
n_7 = result_7[['team', 'proba_team_won','team_won','game_id', 'favorite']]
n_8 = result_8[['team', 'proba_team_won','team_won','game_id', 'favorite']]
n_9 = result_9[['team', 'proba_team_won','team_won','game_id', 'favorite']]
n_10 = result_10[['team', 'proba_team_won','team_won','game_id', 'favorite']]
n_11 = result_11[['team', 'proba_team_won','team_won','game_id', 'favorite']]
n_12 = result_12[['team', 'proba_team_won','team_won','game_id', 'favorite']]
n_13 = result_13[['team', 'proba_team_won','team_won','game_id', 'favorite']]
n_14 = result_14[['team', 'proba_team_won','team_won','game_id', 'favorite']]
n_15 = result_15[['team', 'proba_team_won','team_won','game_id', 'favorite']]
n_16 = result_16[['team', 'proba_team_won','team_won','game_id', 'favorite']]
n_17 = result_17[['team', 'proba_team_won','team_won','game_id', 'favorite']]

# then rename the columns for the opponent

n_5.columns = ['opp', 'proba_opp_won', 'opp_won', 'game_id', 'opp_fav']
n_6.columns = ['opp', 'proba_opp_won', 'opp_won', 'game_id', 'opp_fav']
n_7.columns = ['opp', 'proba_opp_won', 'opp_won', 'game_id', 'opp_fav']
n_8.columns = ['opp', 'proba_opp_won', 'opp_won', 'game_id', 'opp_fav']
n_9.columns = ['opp', 'proba_opp_won', 'opp_won', 'game_id', 'opp_fav']
n_10.columns = ['opp', 'proba_opp_won', 'opp_won', 'game_id', 'opp_fav']
n_11.columns = ['opp', 'proba_opp_won', 'opp_won', 'game_id', 'opp_fav']
n_12.columns = ['opp', 'proba_opp_won', 'opp_won', 'game_id', 'opp_fav']
n_13.columns = ['opp', 'proba_opp_won', 'opp_won', 'game_id', 'opp_fav']
n_14.columns = ['opp', 'proba_opp_won', 'opp_won', 'game_id', 'opp_fav']
n_15.columns = ['opp', 'proba_opp_won', 'opp_won', 'game_id', 'opp_fav']
n_16.columns = ['opp', 'proba_opp_won', 'opp_won', 'game_id', 'opp_fav']
n_17.columns = ['opp', 'proba_opp_won', 'opp_won', 'game_id', 'opp_fav']


# from the copy drop the duplicates keeping the last occurance, because we sorted it we can then run this on the previous dataframe keeping the 
# first occurance and this will allow us to rebuild the dataframe to apply money lines to it
n_5 = n_5.drop_duplicates(['game_id'], keep='last')
n_6 = n_6.drop_duplicates(['game_id'], keep='last')
n_7 = n_7.drop_duplicates(['game_id'], keep='last')
n_8 = n_8.drop_duplicates(['game_id'], keep='last')
n_9 = n_9.drop_duplicates(['game_id'], keep='last')
n_10 = n_10.drop_duplicates(['game_id'], keep='last')
n_11 = n_11.drop_duplicates(['game_id'], keep='last')
n_12 = n_12.drop_duplicates(['game_id'], keep='last')
n_13 = n_13.drop_duplicates(['game_id'], keep='last')
n_14 = n_14.drop_duplicates(['game_id'], keep='last')
n_15 = n_15.drop_duplicates(['game_id'], keep='last')
n_16 = n_16.drop_duplicates(['game_id'], keep='last')
n_17 = n_17.drop_duplicates(['game_id'], keep='last')


# same operation but keep the first

result_5= result_5.drop_duplicates(['game_id'], keep='first')
result_6= result_6.drop_duplicates(['game_id'], keep='first')
result_7= result_7.drop_duplicates(['game_id'], keep='first')
result_8= result_8.drop_duplicates(['game_id'], keep='first')
result_9= result_9.drop_duplicates(['game_id'], keep='first')
result_10= result_10.drop_duplicates(['game_id'], keep='first')
result_11= result_11.drop_duplicates(['game_id'], keep='first')
result_12= result_12.drop_duplicates(['game_id'], keep='first')
result_13= result_13.drop_duplicates(['game_id'], keep='first')
result_14= result_14.drop_duplicates(['game_id'], keep='first')
result_15= result_15.drop_duplicates(['game_id'], keep='first')
result_16= result_16.drop_duplicates(['game_id'], keep='first')
result_17= result_17.drop_duplicates(['game_id'], keep='first')

#drop redundant columns
result_ = result_.drop(columns='opp')
result_5 = result_5.drop(columns='opp')
result_6 = result_6.drop(columns='opp')
result_7 = result_7.drop(columns='opp')
result_8 = result_8.drop(columns='opp')
result_9 = result_9.drop(columns='opp')
result_10 = result_10.drop(columns='opp')
result_11 = result_11.drop(columns='opp')
result_12 = result_12.drop(columns='opp')
result_13 = result_13.drop(columns='opp')
result_14 = result_14.drop(columns='opp')
result_15 = result_15.drop(columns='opp')
result_16 = result_16.drop(columns='opp')
result_17 = result_17.drop(columns='opp')

# now put the dataframes back together for team and opponent
merge_1 = result_.merge(new_1, on=['game_id'], how='left')
merge_5 = result_5.merge(n_5, on=['game_id'], how='left')
merge_6 = result_6.merge(n_6, on=['game_id'], how='left')
merge_7 = result_7.merge(n_7, on=['game_id'], how='left')
merge_8 = result_8.merge(n_8, on=['game_id'], how='left')
merge_9 = result_9.merge(n_9, on=['game_id'], how='left')
merge_10 = result_10.merge(n_10, on=['game_id'], how='left')
merge_11 = result_11.merge(n_11, on=['game_id'], how='left')
merge_12 = result_12.merge(n_12, on=['game_id'], how='left')
merge_13 = result_13.merge(n_13, on=['game_id'], how='left')
merge_14 = result_14.merge(n_14, on=['game_id'], how='left')
merge_15 = result_15.merge(n_15, on=['game_id'], how='left')
merge_16 = result_16.merge(n_16, on=['game_id'], how='left')
merge_17 = result_17.merge(n_17, on=['game_id'], how='left')

# order the columns in a way that makes sense

merge_5 = merge_5[['game_id','team','opp', 'proba_team_won', 'proba_opp_won',
                'team_won', 'opp_won', 'favorite', 'opp_fav']]

merge_6 = merge_6[['game_id','team','opp', 'proba_team_won', 'proba_opp_won',
                'team_won', 'opp_won', 'favorite', 'opp_fav']]
merge_7 = merge_7[['game_id','team','opp', 'proba_team_won', 'proba_opp_won',
                'team_won', 'opp_won', 'favorite', 'opp_fav']]
merge_8 = merge_8[['game_id','team','opp', 'proba_team_won', 'proba_opp_won',
                'team_won', 'opp_won', 'favorite', 'opp_fav']]
merge_9 = merge_9[['game_id','team','opp', 'proba_team_won', 'proba_opp_won',
                'team_won', 'opp_won', 'favorite', 'opp_fav']]
merge_10 = merge_10[['game_id','team','opp', 'proba_team_won', 'proba_opp_won',
                'team_won', 'opp_won', 'favorite', 'opp_fav']]
merge_11 = merge_11[['game_id','team','opp', 'proba_team_won', 'proba_opp_won',
                'team_won', 'opp_won', 'favorite', 'opp_fav']]
merge_12 = merge_12[['game_id','team','opp', 'proba_team_won', 'proba_opp_won',
                'team_won', 'opp_won', 'favorite', 'opp_fav']]
merge_13 = merge_13[['game_id','team','opp', 'proba_team_won', 'proba_opp_won',
                'team_won', 'opp_won', 'favorite', 'opp_fav']]
merge_14 = merge_14[['game_id','team','opp', 'proba_team_won', 'proba_opp_won',
                'team_won', 'opp_won', 'favorite', 'opp_fav']]
merge_15 = merge_15[['game_id','team','opp', 'proba_team_won', 'proba_opp_won',
                'team_won', 'opp_won', 'favorite', 'opp_fav']]
merge_16 = merge_16[['game_id','team','opp', 'proba_team_won', 'proba_opp_won',
                'team_won', 'opp_won', 'favorite', 'opp_fav']]
merge_17 = merge_17[['game_id','team','opp', 'proba_team_won', 'proba_opp_won',
                'team_won', 'opp_won', 'favorite', 'opp_fav']]



##### simplify the names to make it easier to look at
merge_1.columns = ['ID', 'team', 'opp', 'proba_win', 'proba_opp_win', 'team_won?',
                 'opp_won?', 'team_fav', 'opp_fav']
merge_5.columns = ['ID', 'team', 'opp', 'proba_win', 'proba_opp_win', 'team_won?',
                 'opp_won?', 'team_fav', 'opp_fav']
merge_6.columns = ['ID', 'team', 'opp', 'proba_win', 'proba_opp_win', 'team_won?',
                 'opp_won?', 'team_fav', 'opp_fav']
merge_7.columns = ['ID', 'team', 'opp', 'proba_win', 'proba_opp_win', 'team_won?',
                 'opp_won?', 'team_fav', 'opp_fav']
merge_8.columns = ['ID', 'team', 'opp', 'proba_win', 'proba_opp_win', 'team_won?',
                 'opp_won?', 'team_fav', 'opp_fav']
merge_9.columns = ['ID', 'team', 'opp', 'proba_win', 'proba_opp_win', 'team_won?',
                 'opp_won?', 'team_fav', 'opp_fav']
merge_10.columns = ['ID', 'team', 'opp', 'proba_win', 'proba_opp_win', 'team_won?',
                 'opp_won?', 'team_fav', 'opp_fav']
merge_11.columns = ['ID', 'team', 'opp', 'proba_win', 'proba_opp_win', 'team_won?',
                 'opp_won?', 'team_fav', 'opp_fav']
merge_12.columns = ['ID', 'team', 'opp', 'proba_win', 'proba_opp_win', 'team_won?',
                 'opp_won?', 'team_fav', 'opp_fav']
merge_13.columns = ['ID', 'team', 'opp', 'proba_win', 'proba_opp_win', 'team_won?',
                 'opp_won?', 'team_fav', 'opp_fav']
merge_14.columns = ['ID', 'team', 'opp', 'proba_win', 'proba_opp_win', 'team_won?',
                 'opp_won?', 'team_fav', 'opp_fav']
merge_15.columns = ['ID', 'team', 'opp', 'proba_win', 'proba_opp_win', 'team_won?',
                 'opp_won?', 'team_fav', 'opp_fav']
merge_16.columns = ['ID', 'team', 'opp', 'proba_win', 'proba_opp_win', 'team_won?',
                 'opp_won?', 'team_fav', 'opp_fav']
merge_17.columns = ['ID', 'team', 'opp', 'proba_win', 'proba_opp_win', 'team_won?',
                 'opp_won?', 'team_fav', 'opp_fav']

# shorthand copies for iterating
m_4 = merge_1.copy()
m_5 = merge_5.copy()
m_6 = merge_6.copy()
m_7 = merge_7.copy()
m_8 = merge_8.copy()
m_9 = merge_9.copy()
m_10 = merge_10.copy()
m_11 = merge_11.copy()
m_12 = merge_12.copy()
m_13 = merge_13.copy()
m_14 = merge_14.copy()
m_15 = merge_15.copy()
m_16 = merge_16.copy()
m_17 = merge_17.copy()


## teams and opps are mixed up from one scraper to the other, this can be simplified using the odds portal scraper

for idx, row in ml5.iterrows():
    m_5.loc[m_5['team']==row['team'],'money_line']=row['money_line']
    m_5.loc[m_5['opp']==row['team'],'opp_money_line']=row['money_line']
    m_5.loc[m_5['opp']==row['opp'],'opp_money_line']=row['opp_money_line']
    m_5.loc[m_5['team']==row['opp'],'money_line']=row['opp_money_line']

for idx, row in ml6.iterrows():
    m_6.loc[m_6['team']==row['team'],'money_line']=row['money_line']
    m_6.loc[m_6['opp']==row['team'],'opp_money_line']=row['money_line']
    m_6.loc[m_6['opp']==row['opp'],'opp_money_line']=row['opp_money_line']
    m_6.loc[m_6['team']==row['opp'],'money_line']=row['opp_money_line']

for idx, row in ml7.iterrows():
    m_7.loc[m_7['team']==row['team'],'money_line']=row['money_line']
    m_7.loc[m_7['opp']==row['team'],'opp_money_line']=row['money_line']
    m_7.loc[m_7['opp']==row['opp'],'opp_money_line']=row['opp_money_line']
    m_7.loc[m_7['team']==row['opp'],'money_line']=row['opp_money_line']

for idx, row in ml8.iterrows():
    m_8.loc[m_8['team']==row['team'],'money_line']=row['money_line']
    m_8.loc[m_8['opp']==row['team'],'opp_money_line']=row['money_line']
    m_8.loc[m_8['opp']==row['opp'],'opp_money_line']=row['opp_money_line']
    m_8.loc[m_8['team']==row['opp'],'money_line']=row['opp_money_line']

for idx, row in ml9.iterrows():
    m_9.loc[m_9['team']==row['team'],'money_line']=row['money_line']
    m_9.loc[m_9['opp']==row['team'],'opp_money_line']=row['money_line']
    m_9.loc[m_9['opp']==row['opp'],'opp_money_line']=row['opp_money_line']
    m_9.loc[m_9['team']==row['opp'],'money_line']=row['opp_money_line']
    
for idx, row in ml10.iterrows():
    m_10.loc[m_10['team']==row['team'],'money_line']=row['money_line']
    m_10.loc[m_10['opp']==row['team'],'opp_money_line']=row['money_line']
    m_10.loc[m_10['opp']==row['opp'],'opp_money_line']=row['opp_money_line']
    m_10.loc[m_10['team']==row['opp'],'money_line']=row['opp_money_line']    
    
for idx, row in ml11.iterrows():
    m_11.loc[m_11['team']==row['team'],'money_line']=row['money_line']
    m_11.loc[m_11['opp']==row['team'],'opp_money_line']=row['money_line']
    m_11.loc[m_11['opp']==row['opp'],'opp_money_line']=row['opp_money_line']
    m_11.loc[m_11['team']==row['opp'],'money_line']=row['opp_money_line']  


for idx, row in ml12.iterrows():
    m_12.loc[m_12['team']==row['team'],'money_line']=row['money_line']
    m_12.loc[m_12['opp']==row['team'],'opp_money_line']=row['money_line']
    m_12.loc[m_12['opp']==row['opp'],'opp_money_line']=row['opp_money_line']
    m_12.loc[m_12['team']==row['opp'],'money_line']=row['opp_money_line']
    
for idx, row in ml13.iterrows():
    m_13.loc[m_13['team']==row['team'],'money_line']=row['money_line']
    m_13.loc[m_13['opp']==row['team'],'opp_money_line']=row['money_line']
    m_13.loc[m_13['opp']==row['opp'],'opp_money_line']=row['opp_money_line']
    m_13.loc[m_13['team']==row['opp'],'money_line']=row['opp_money_line']
    
for idx, row in ml14.iterrows():
    m_14.loc[m_14['team']==row['team'],'money_line']=row['money_line']
    m_14.loc[m_14['opp']==row['team'],'opp_money_line']=row['money_line']
    m_14.loc[m_14['opp']==row['opp'],'opp_money_line']=row['opp_money_line']
    m_14.loc[m_14['team']==row['opp'],'money_line']=row['opp_money_line']
    
for idx, row in ml15.iterrows():
    m_15.loc[m_15['team']==row['team'],'money_line']=row['money_line']
    m_15.loc[m_15['opp']==row['team'],'opp_money_line']=row['money_line']
    m_15.loc[m_15['opp']==row['opp'],'opp_money_line']=row['opp_money_line']
    m_15.loc[m_15['team']==row['opp'],'money_line']=row['opp_money_line']

for idx, row in ml16.iterrows():
    m_16.loc[m_16['team']==row['team'],'money_line']=row['money_line']
    m_16.loc[m_16['opp']==row['team'],'opp_money_line']=row['money_line']
    m_16.loc[m_16['opp']==row['opp'],'opp_money_line']=row['opp_money_line']
    m_16.loc[m_16['team']==row['opp'],'money_line']=row['opp_money_line']

for idx, row in ml17.iterrows():
    m_17.loc[m_17['team']==row['team'],'money_line']=row['money_line']
    m_17.loc[m_17['opp']==row['team'],'opp_money_line']=row['money_line']
    m_17.loc[m_17['opp']==row['opp'],'opp_money_line']=row['opp_money_line']
    m_17.loc[m_17['team']==row['opp'],'money_line']=row['opp_money_line']

## add the weeks

m_5['week']=5
m_6['week']=6
m_7['week']=7
m_8['week']=8
m_9['week']=9
m_10['week']=10
m_11['week']=11
m_12['week']=12
m_13['week']=13
m_14['week']=14
m_15['week']=15
m_16['week']=16
m_17['week']=17

# finally concatenate to reduce redundant code

frames = [m_5, m_6, m_7, m_8, m_9, m_10, m_11, m_12,m_13,m_14,m_15,m_16,m_17]
model_gb = pd.concat(frames)

model_gb = model_gb.reset_index()

model_gb['money_line'] = model_gb['money_line'].apply(lambda x: float(x))
model_gb['opp_money_line'] = model_gb['opp_money_line'].apply(lambda x: float(x))

#after ensuring money lines are floats, convert American money lines to decimal money lines
model_gb.loc[model_gb['money_line']<0, 'dec_ml'] = (1 + 100/abs(model_gb['money_line']))               
model_gb.loc[model_gb['money_line']>0, 'dec_ml'] = (1 + abs(model_gb['money_line'])/100)
model_gb.loc[model_gb['opp_money_line']>0, 'dec_oml'] = (1 + abs(model_gb['opp_money_line'])/100)
model_gb.loc[model_gb['opp_money_line']<0, 'dec_oml'] = (1 + 100/abs(model_gb['opp_money_line']))


model_gb = model_gb.drop(columns='index')

# add a column for control bets to test only betting on the favorite or underdog

model_gb.loc[model_gb['favorite']==1, 'control_bet_for'] = 'team'
model_gb.loc[model_gb['opp_fav']==1, 'control_bet_for'] = 'opp'
model_gb.loc[model_gb['favorite']==0, 'control_bet_ud'] = 'team'
model_gb.loc[model_gb['opp_fav']==0, 'control_bet_ud'] = 'opp'

# profit from only betting on the favorite
model_gb.loc[(model_gb['control_bet_for']=='team') & (model_gb['team_won']== 1), 'fav_prof'] = (100*model_gb['dec_ml'])-100
model_gb.loc[(model_gb['control_bet_for']=='opp') & (model_gb['opp_won']== 1), 'fav_prof'] = (100*model_gb['dec_oml'])-100
model_gb.loc[(model_gb['control_bet_for']=='team') & (model_gb['team_won']== 0), 'fav_prof'] = -100 
model_gb.loc[(model_gb['control_bet_for']=='opp') & (model_gb['opp_won']== 0), 'fav_prof'] = -100

#profit from only betting on the underdog

model_gb.loc[(model_gb['control_bet_ud']=='team') & (model_gb['team_won']== 1), 'ud_prof'] = (100*model_gb['dec_ml'])-100
model_gb.loc[(model_gb['control_bet_ud']=='opp') & (model_gb['opp_won']== 1), 'ud_prof'] = (100*model_gb['dec_oml'])-100
model_gb.loc[(model_gb['control_bet_ud']=='team') & (model_gb['team_won']== 0), 'ud_prof'] = -100 
model_gb.loc[(model_gb['control_bet_ud']=='opp') & (model_gb['opp_won']== 0), 'ud_prof'] = -100                    

# test if only betting by higher winning probability is profitable
model_gb.loc[model_gb['proba_team_won'] > model_gb['proba_opp_won'], 'bet_placed'] = 'team'
model_gb.loc[model_gb['proba_team_won'] < model_gb['proba_opp_won'], 'bet_placed'] = 'opp'
model_gb.loc[model_gb['proba_team_won'] == model_gb['proba_opp_won'], 'bet_placed'] = 'push'

model_gb.loc[(model_gb['team_won']==1) & (model_gb['bet_placed']=='team'), 'profit'] = (100*model_gb['dec_ml'])-100            
model_gb.loc[(model_gb['team_won']==0) & (model_gb['bet_placed']=='team'), 'profit'] = -100
model_gb.loc[(model_gb['opp_won']==1) & (model_gb['bet_placed']=='opp'), 'profit'] = (100*model_gb['dec_oml'])-100            
model_gb.loc[(model_gb['opp_won']==0) & (model_gb['bet_placed']=='opp'), 'profit'] = -100 



# feature engineering to add in expected value betting
model_gb['team_AWPB'] = 100 * model_gb['dec_ml']
model_gb['opp_AWPB'] = 100 * model_gb['dec_oml']

model_gb['team_EV'] = (model_gb['team_AWPB'] * model_gb['proba_team_won']) - (100*(1-model_gb['proba_team_won']))
model_gb['opp_EV'] = (model_gb['opp_AWPB'] * model_gb['proba_opp_won']) - (100*(1-model_gb['proba_opp_won']))

model_gb.loc[(model_gb['team_EV']> 0) | (model_gb['opp_EV']> 0), 'ev_bet'] = True
model_gb.loc[(model_gb['team_EV']< 0) & (model_gb['opp_EV']< 0), 'ev_bet'] = False

#only place expected value bets for the greater expected value if both are positive
def ev_for(df):
    if (df['ev_bet'] ==True) and (df['team_EV'] > df['opp_EV']):
        return 'team'
    elif (df['ev_bet'] ==True) and (df['team_EV'] < df['opp_EV']):
        return 'opp'
    elif df['ev_bet'] == False:
        return 'no bet'

model_gb['ev_for'] = model_gb.apply(ev_for, axis = 1)


model_gb.loc[(model_gb['team_won']==1) & (model_gb['ev_for']=='team'), 'ev_profit'] = (100*model_gb['dec_ml'])-100            
model_gb.loc[(model_gb['team_won']==0) & (model_gb['ev_for']=='team'), 'ev_profit'] = -100
model_gb.loc[(model_gb['opp_won']==1) & (model_gb['ev_for']=='opp'), 'ev_profit'] = (100*model_gb['dec_oml'])-100            
model_gb.loc[(model_gb['opp_won']==0) & (model_gb['ev_for']=='opp'), 'ev_profit'] = -100  
model_gb.loc[(model_gb['opp_won']==0) & (model_gb['ev_for']=='no bet'), 'ev_profit'] = 0  
model_gb.loc[(model_gb['opp_won']==1) & (model_gb['ev_for']=='no bet'), 'ev_profit'] = 0

# expected value betting profit
model_gb['ev_profit'].sum()

# this is to test if blindly betting on the team with the higher probability is profitable
model_gb['profit'].sum()

#control profits for betting on favorite only and underdog only
model_gb['fav_prof'].sum()
model_gb['ud_prof'].sum()