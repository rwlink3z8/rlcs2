from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import pandas as pd 
import logging
import time

browser = webdriver.Chrome()

browser.get("https://www.teamrankings.com/nfl-odds-week-4")
time.sleep(2)
# unique table class to pull each game, score, and teams closing money line 
games = browser.find_elements_by_css_selector("table.tr-table.space-bottom")
game_list = []
for game in games:
    # The xpath allows us to drill down into the html of the current game
    # You can specify which of the tags you want
    # because selinum is written in JavaScript it starts its lists at 1
    team1 = game.find_element_by_xpath('./tbody/tr/td/strong/a').text
    team2 = game.find_element_by_xpath('./tbody/tr[2]/td/strong/a').text
    ml1 = game.find_element_by_xpath('./tbody/tr[1]/td[5]').text
    ml2 = game.find_element_by_xpath('./tbody/tr[2]/td[5]').text
    score1 = game.find_element_by_xpath('./tbody/tr[1]/td[2]').text
    score2 = game.find_element_by_xpath('./tbody/tr[2]/td[2]').text
    game_row = (team1, ml1, score1, team2, ml2, score2)
    game_list.append(game_row)

#now make it a dataframe
w4_money_line = pd.DataFrame(game_list, columns =['team', 'money_line', 'team_score', 
                                                  'opp', 'opp_money_line', 'opp_score'])



browser = webdriver.Chrome()

browser.get("https://www.teamrankings.com/nfl-odds-week-5")
time.sleep(2)
 
games = browser.find_elements_by_css_selector("table.tr-table.space-bottom")
game_list5 = []
for game in games:
    team1 = game.find_element_by_xpath('./tbody/tr/td/strong/a').text
    team2 = game.find_element_by_xpath('./tbody/tr[2]/td/strong/a').text
    ml1 = game.find_element_by_xpath('./tbody/tr[1]/td[5]').text
    ml2 = game.find_element_by_xpath('./tbody/tr[2]/td[5]').text
    score1 = game.find_element_by_xpath('./tbody/tr[1]/td[2]').text
    score2 = game.find_element_by_xpath('./tbody/tr[2]/td[2]').text
    game_row = (team1, ml1, score1, team2, ml2, score2)
    game_list5.append(game_row)

w5_money_line = pd.DataFrame(game_list5, columns =['team', 'money_line', 'team_score', 
                                                  'opp', 'opp_money_line', 'opp_score'])

browser = webdriver.Chrome()
browser.get("https://www.teamrankings.com/nfl-odds-week-6")
time.sleep(2)  
games = browser.find_elements_by_css_selector("table.tr-table.space-bottom")
game_list6 = []
for game in games:
    team1 = game.find_element_by_xpath('./tbody/tr/td/strong/a').text
    team2 = game.find_element_by_xpath('./tbody/tr[2]/td/strong/a').text
    ml1 = game.find_element_by_xpath('./tbody/tr[1]/td[5]').text
    ml2 = game.find_element_by_xpath('./tbody/tr[2]/td[5]').text
    score1 = game.find_element_by_xpath('./tbody/tr[1]/td[2]').text
    score2 = game.find_element_by_xpath('./tbody/tr[2]/td[2]').text
    game_row = (team1, ml1, score1, team2, ml2, score2)
    game_list6.append(game_row)

w6_money_line = pd.DataFrame(game_list6, columns =['team', 'money_line', 'team_score', 
                                                  'opp', 'opp_money_line', 'opp_score']) 

browser = webdriver.Chrome()
browser.get("https://www.teamrankings.com/nfl-odds-week-7")
time.sleep(2)  
games = browser.find_elements_by_css_selector("table.tr-table.space-bottom")
game_list7 = []
for game in games:
    team1 = game.find_element_by_xpath('./tbody/tr/td/strong/a').text
    team2 = game.find_element_by_xpath('./tbody/tr[2]/td/strong/a').text
    ml1 = game.find_element_by_xpath('./tbody/tr[1]/td[5]').text
    ml2 = game.find_element_by_xpath('./tbody/tr[2]/td[5]').text
    score1 = game.find_element_by_xpath('./tbody/tr[1]/td[2]').text
    score2 = game.find_element_by_xpath('./tbody/tr[2]/td[2]').text
    game_row = (team1, ml1, score1, team2, ml2, score2)
    game_list7.append(game_row)

w7_money_line = pd.DataFrame(game_list7, columns =['team', 'money_line', 'team_score', 
                                                  'opp', 'opp_money_line', 'opp_score']) 


browser = webdriver.Chrome()
browser.get("https://www.teamrankings.com/nfl-odds-week-8")
time.sleep(2)  
games = browser.find_elements_by_css_selector("table.tr-table.space-bottom")
game_list8 = []
for game in games:
    team1 = game.find_element_by_xpath('./tbody/tr/td/strong/a').text
    team2 = game.find_element_by_xpath('./tbody/tr[2]/td/strong/a').text
    ml1 = game.find_element_by_xpath('./tbody/tr[1]/td[5]').text
    ml2 = game.find_element_by_xpath('./tbody/tr[2]/td[5]').text
    score1 = game.find_element_by_xpath('./tbody/tr[1]/td[2]').text
    score2 = game.find_element_by_xpath('./tbody/tr[2]/td[2]').text
    game_row = (team1, ml1, score1, team2, ml2, score2)
    game_list8.append(game_row)

w8_money_line = pd.DataFrame(game_list8, columns =['team', 'money_line', 'team_score', 
                                                  'opp', 'opp_money_line', 'opp_score']) 

browser = webdriver.Chrome()
browser.get("https://www.teamrankings.com/nfl-odds-week-9")
time.sleep(2)  
games = browser.find_elements_by_css_selector("table.tr-table.space-bottom")
game_list9 = []
for game in games:
    team1 = game.find_element_by_xpath('./tbody/tr/td/strong/a').text
    team2 = game.find_element_by_xpath('./tbody/tr[2]/td/strong/a').text
    ml1 = game.find_element_by_xpath('./tbody/tr[1]/td[5]').text
    ml2 = game.find_element_by_xpath('./tbody/tr[2]/td[5]').text
    score1 = game.find_element_by_xpath('./tbody/tr[1]/td[2]').text
    score2 = game.find_element_by_xpath('./tbody/tr[2]/td[2]').text
    game_row = (team1, ml1, score1, team2, ml2, score2)
    game_list9.append(game_row)

w9_money_line = pd.DataFrame(game_list9, columns =['team', 'money_line', 'team_score', 
                                                  'opp', 'opp_money_line', 'opp_score']) 

browser = webdriver.Chrome()
browser.get("https://www.teamrankings.com/nfl-odds-week-10")
time.sleep(2)  
games = browser.find_elements_by_css_selector("table.tr-table.space-bottom")
game_list10 = []
for game in games:
    team1 = game.find_element_by_xpath('./tbody/tr/td/strong/a').text
    team2 = game.find_element_by_xpath('./tbody/tr[2]/td/strong/a').text
    ml1 = game.find_element_by_xpath('./tbody/tr[1]/td[5]').text
    ml2 = game.find_element_by_xpath('./tbody/tr[2]/td[5]').text
    score1 = game.find_element_by_xpath('./tbody/tr[1]/td[2]').text
    score2 = game.find_element_by_xpath('./tbody/tr[2]/td[2]').text
    game_row = (team1, ml1, score1, team2, ml2, score2)
    game_list10.append(game_row)

w10_money_line = pd.DataFrame(game_list10, columns =['team', 'money_line', 'team_score', 
                                                  'opp', 'opp_money_line', 'opp_score']) 

browser = webdriver.Chrome()
browser.get("https://www.teamrankings.com/nfl-odds-week-11")
time.sleep(2)  
games = browser.find_elements_by_css_selector("table.tr-table.space-bottom")
game_list11 = []
for game in games:
    team1 = game.find_element_by_xpath('./tbody/tr/td/strong/a').text
    team2 = game.find_element_by_xpath('./tbody/tr[2]/td/strong/a').text
    ml1 = game.find_element_by_xpath('./tbody/tr[1]/td[5]').text
    ml2 = game.find_element_by_xpath('./tbody/tr[2]/td[5]').text
    score1 = game.find_element_by_xpath('./tbody/tr[1]/td[2]').text
    score2 = game.find_element_by_xpath('./tbody/tr[2]/td[2]').text
    game_row = (team1, ml1, score1, team2, ml2, score2)
    game_list11.append(game_row)

w11_money_line = pd.DataFrame(game_list11, columns =['team', 'money_line', 'team_score', 
                                                  'opp', 'opp_money_line', 'opp_score']) 

browser = webdriver.Chrome()
browser.get("https://www.teamrankings.com/nfl-odds-week-12")
time.sleep(2)  
games = browser.find_elements_by_css_selector("table.tr-table.space-bottom")
game_list12 = []
for game in games:
    team1 = game.find_element_by_xpath('./tbody/tr/td/strong/a').text
    team2 = game.find_element_by_xpath('./tbody/tr[2]/td/strong/a').text
    ml1 = game.find_element_by_xpath('./tbody/tr[1]/td[5]').text
    ml2 = game.find_element_by_xpath('./tbody/tr[2]/td[5]').text
    score1 = game.find_element_by_xpath('./tbody/tr[1]/td[2]').text
    score2 = game.find_element_by_xpath('./tbody/tr[2]/td[2]').text
    game_row = (team1, ml1, score1, team2, ml2, score2)
    game_list12.append(game_row)

w12_money_line = pd.DataFrame(game_list12, columns =['team', 'money_line', 'team_score', 
                                                  'opp', 'opp_money_line', 'opp_score']) 

browser = webdriver.Chrome()
browser.get("https://www.teamrankings.com/nfl-odds-week-13")
time.sleep(2)  
games = browser.find_elements_by_css_selector("table.tr-table.space-bottom")
game_list13 = []
for game in games:
    team1 = game.find_element_by_xpath('./tbody/tr/td/strong/a').text
    team2 = game.find_element_by_xpath('./tbody/tr[2]/td/strong/a').text
    ml1 = game.find_element_by_xpath('./tbody/tr[1]/td[5]').text
    ml2 = game.find_element_by_xpath('./tbody/tr[2]/td[5]').text
    score1 = game.find_element_by_xpath('./tbody/tr[1]/td[2]').text
    score2 = game.find_element_by_xpath('./tbody/tr[2]/td[2]').text
    game_row = (team1, ml1, score1, team2, ml2, score2)
    game_list13.append(game_row)

w13_money_line = pd.DataFrame(game_list13, columns =['team', 'money_line', 'team_score', 
                                                  'opp', 'opp_money_line', 'opp_score']) 

browser = webdriver.Chrome()
browser.get("https://www.teamrankings.com/nfl-odds-week-14")
time.sleep(2)  
games = browser.find_elements_by_css_selector("table.tr-table.space-bottom")
game_list14 = []
for game in games:
    team1 = game.find_element_by_xpath('./tbody/tr/td/strong/a').text
    team2 = game.find_element_by_xpath('./tbody/tr[2]/td/strong/a').text
    ml1 = game.find_element_by_xpath('./tbody/tr[1]/td[5]').text
    ml2 = game.find_element_by_xpath('./tbody/tr[2]/td[5]').text
    score1 = game.find_element_by_xpath('./tbody/tr[1]/td[2]').text
    score2 = game.find_element_by_xpath('./tbody/tr[2]/td[2]').text
    game_row = (team1, ml1, score1, team2, ml2, score2)
    game_list14.append(game_row)

w14_money_line = pd.DataFrame(game_list14, columns =['team', 'money_line', 'team_score', 
                                                  'opp', 'opp_money_line', 'opp_score']) 

browser = webdriver.Chrome()
browser.get("https://www.teamrankings.com/nfl-odds-week-15")
time.sleep(2)  
games = browser.find_elements_by_css_selector("table.tr-table.space-bottom")
game_list15 = []
for game in games:
    team1 = game.find_element_by_xpath('./tbody/tr/td/strong/a').text
    team2 = game.find_element_by_xpath('./tbody/tr[2]/td/strong/a').text
    ml1 = game.find_element_by_xpath('./tbody/tr[1]/td[5]').text
    ml2 = game.find_element_by_xpath('./tbody/tr[2]/td[5]').text
    score1 = game.find_element_by_xpath('./tbody/tr[1]/td[2]').text
    score2 = game.find_element_by_xpath('./tbody/tr[2]/td[2]').text
    game_row = (team1, ml1, score1, team2, ml2, score2)
    game_list15.append(game_row)

w15_money_line = pd.DataFrame(game_list15, columns =['team', 'money_line', 'team_score', 
                                                  'opp', 'opp_money_line', 'opp_score']) 

browser = webdriver.Chrome()
browser.get("https://www.teamrankings.com/nfl-odds-week-16")
time.sleep(2)  
games = browser.find_elements_by_css_selector("table.tr-table.space-bottom")
game_list16 = []
for game in games:
    team1 = game.find_element_by_xpath('./tbody/tr/td/strong/a').text
    team2 = game.find_element_by_xpath('./tbody/tr[2]/td/strong/a').text
    ml1 = game.find_element_by_xpath('./tbody/tr[1]/td[5]').text
    ml2 = game.find_element_by_xpath('./tbody/tr[2]/td[5]').text
    score1 = game.find_element_by_xpath('./tbody/tr[1]/td[2]').text
    score2 = game.find_element_by_xpath('./tbody/tr[2]/td[2]').text
    game_row = (team1, ml1, score1, team2, ml2, score2)
    game_list16.append(game_row)

w16_money_line = pd.DataFrame(game_list16, columns =['team', 'money_line', 'team_score', 
                                                  'opp', 'opp_money_line', 'opp_score']) 

browser = webdriver.Chrome()
browser.get("https://www.teamrankings.com/nfl-odds-week-17")
time.sleep(2)  
games = browser.find_elements_by_css_selector("table.tr-table.space-bottom")
game_list17 = []
for game in games:
    team1 = game.find_element_by_xpath('./tbody/tr/td/strong/a').text
    team2 = game.find_element_by_xpath('./tbody/tr[2]/td/strong/a').text
    ml1 = game.find_element_by_xpath('./tbody/tr[1]/td[5]').text
    ml2 = game.find_element_by_xpath('./tbody/tr[2]/td[5]').text
    score1 = game.find_element_by_xpath('./tbody/tr[1]/td[2]').text
    score2 = game.find_element_by_xpath('./tbody/tr[2]/td[2]').text
    game_row = (team1, ml1, score1, team2, ml2, score2)
    game_list17.append(game_row)

w17_money_line = pd.DataFrame(game_list17, columns =['team', 'money_line', 'team_score', 
                                                  'opp', 'opp_money_line', 'opp_score']) 

ml4 = w4_money_line.copy()
ml5 = w5_money_line.copy()
ml6 = w6_money_line.copy()  
ml7 = w7_money_line.copy() 
ml8 = w8_money_line.copy()
ml9 = w9_money_line.copy()
ml10 = w10_money_line.copy()
ml11 = w11_money_line.copy()
ml12 = w12_money_line.copy()
ml13 = w13_money_line.copy()
ml14 = w14_money_line.copy() 
ml15 = w15_money_line.copy()
ml16 = w16_money_line.copy() 
ml17 = w17_money_line.copy() 

