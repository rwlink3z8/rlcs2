from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import pandas as pd 
import logging
import time


# oddsportal scraper, incomplete, pulls everything from the page, to get older money lines and to scrape live moneylines, clean up and store
# detailed instructions on building a live oddsportal scraper:  https://www.youtube.com/watch?v=mgAqcpYJQag&t=658s


browser = webdriver.Chrome()
browser.get("https://www.oddsportal.com/american-football/usa/nfl-2017-2018/results/")
time.sleep(2)

# this is the main table, gives matchups and average money lines for each game, can also be pulled by class name
tab_main = browser.find_element_by_xpath('//*[@id="tournamentTable"]/tbody').text 

# or 
#tab_main = browser.find_element_by_class_name('odd.deactivate')
# game xpath: find_element_by_xpath('/tbody/tr[4]/td[2]')
#  money line team 1: find_element_by_xpath('/tbody/tr[4]/td[4]')
#  money line team 2 find_element_by_xpath('/tbody/tr[4]/td[6]')


games = [l.split('\n9') for l in tab_main.split('\n')[:-1]]