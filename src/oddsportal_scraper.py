from selenium import webdriver
import pandas as pd


url = "https://www.oddsportal.com/american-football/usa/nfl-2017-2018/results/#/page/{}/"

def scrape_odds_portal(url):
    #instantiate an automated browser
    browser = webdriver.Chrome()
    browser.get(url)
    # get the sources of the page
    df= pd.read_html(browser.page_source, header=0)[0]
    # we are interested in dates, matchups, and moneylines for each team
    dateList = [] 
    gameList = [] #row[2]
    money_line1List = [] #row[5]
    money_line2List = [] # row[6]

    for row in df.itertuples():
        if not isinstance(row[1], str):
            continue
        elif ':' not in row[1]:
            date = row[1].split('-')[0]
            continue
        time = row[1]
        dateList.append(date)
        gameList.append(row[2])
        money_line1List.append(row[5])
        money_line2List.append(row[6])

    result = pd.DataFrame({'date':dateList,
                       'game':gameList,
                       'money_line1':money_line1List,
                       'money_line2':money_line2List})

    return result


url1 = "https://www.oddsportal.com/american-football/usa/nfl-2017-2018/results/#/page/1/"
url2 = "https://www.oddsportal.com/american-football/usa/nfl-2017-2018/results/#/page/2/"
url3 = "https://www.oddsportal.com/american-football/usa/nfl-2017-2018/results/#/page/3/"
url4 = "https://www.oddsportal.com/american-football/usa/nfl-2017-2018/results/#/page/4/"
url5 = "https://www.oddsportal.com/american-football/usa/nfl-2017-2018/results/#/page/5/"
url6 = "https://www.oddsportal.com/american-football/usa/nfl-2017-2018/results/#/page/6/"


oddsportal_dataframe1 = scrape_odds_portal(url1)
oddsportal_dataframe2 = scrape_odds_portal(url2)
oddsportal_dataframe3 = scrape_odds_portal(url3)
oddsportal_dataframe4 = scrape_odds_portal(url4)
oddsportal_dataframe5 = scrape_odds_portal(url5)
oddsportal_dataframe6 = scrape_odds_portal(url6)

od1 = oddsportal_dataframe1.copy()
od2 = oddsportal_dataframe1.copy()
od3 = oddsportal_dataframe1.copy()
od4 = oddsportal_dataframe1.copy()
od5 = oddsportal_dataframe1.copy()
od6 = oddsportal_dataframe1.copy()

frames = [od1, od2, od3, od4, od5, od6]

odds_2018 = pd.concat(frames)
