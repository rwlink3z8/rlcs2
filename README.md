## Betting and the NFL

Sports gambling is a massive industry, specifically, gambling on NFL games is the third most popular kind of gambling in Las Vegas. The goal of this project is to use statistics and machine learning to predict winners and make money gambling on the outcome of NFL games. Below is the general flow of the project, I will scrape statistics, scrape gambling lines, perform data analysis to help guide feature selection and normalization, and ultimately build a model that can make money betting on football games.

![capstone_process](https://github.com/rwlink3z8/rlcs2/blob/master/img/capstone_process.png)

**Background Information**

![example_spread](https://github.com/rwlink3z8/rlcs2/blob/master/img/example_spread.png)

This is an example of what it looks like when you bet on a game.
The matchup is between the Buffalo Bills and the Minnesota Vikings.
  -17.5 -> this indicates the Vikings are favored to win by 17.5 points. This is the spread, conversley, it means the Bills are predicted to lose by 17.5 points. The goal of the spread is to keep gambling as close as possible to 50/50 for each team. The (-110) next to each spread is the spread money line, although this is spread indicates a 50/50 probability, the house takes a commission off the top, this is called the vigorish, or the rake. It means that by betting on the spread a gambler would have to wager $110 to possibly win $100. It ensures that the bookmakers always make a profit, and it means that make money on spread gambling, you would have to correctly predict roughly 52.5% of outcomes (11/21 correct).
  
-1429: This is the money line for the Vikings to win. It means that if the Vikings win and you wager $1429 you will win $100.
+871: This is the money line for the Bills to win. It means that if you wager on the Bills to win and they do, a bet of $100 would result in $871 profit

Example: Bet on the Vikings to win and they do

Wager $1429
Win: $100
Ending Balance: $1529

Example 2: Bet on the Bills to win and they do:

Wager $100
Win: $871
Ending Balance: $971

The final score is the result in this game.

Given the nature of spread betting and money line bets I chose to focus on money line wagers as they are more straight forward, pick a winner. 

## Tech Stack

![tech_stack](https://github.com/rwlink3z8/rlcs2/blob/master/img/tech_stack.png)

This is the general project flow. 

Beautifulsoup scraper - I scraped statistics from profootball reference and spread from teamrankings
Selenium scraper - I scraped moneylines for 2018 and 2019 from oddsportal and teamrankings
Feature engineering - Data normalization, and feature reduction
Exploratory Data Analysis - Matplotlib and Seaborn to initially identify important features

Then using the sci-kit learn library I built a model to predict winning probabilities and apply those to the money lines.

## Exploratory Data Analysis


Some baseline findings. Over the past 13 NFL seasons, favorites win 67% of games. They only cover the spread 48% of the time, however this number depends on the casino. 

61% of all games have a spread between 2.5-3.5 points, the next most common spread is 7 points, the following plots the distribution of the favorites spread (how much the underdog is predicted to lose by) and the actual point differential distribution of the underdog (how much they won or lost by)

![underdogs_ats](https://github.com/rwlink3z8/rlcs2/blob/master/img/underdogs_ats.png)

The next image shows some of the relationships I found important among winning teams and losing teams.

Turnovers - winning teams have spikes at 0 and 1. This is intuitive, winning teams don't lose the ball, where losing teams exhibit more of a poisson distribution. 
Favorites - on average the favorite wins 67% of games, however in 2019 underdogs did win 36% of games.
![eda1](https://github.com/rwlink3z8/rlcs2/blob/master/img/eda1.png)

Trough plotting colinear features can easily be visualized, to address this I normalized offensive and defensive yardage into two statistics.

Yards per play offense - passing yards, rushing yards, rush attempts, pass attempts, pass completions, total offensive plays

yards allowed per defensive play - total yards against, rush yards against, number of defensive plays.

## Model set up

A challenge to address when setting up the model is how to get it into a format that sci-kit learn can handle, a normal train test split would be giving the model data it could not see in advance. To address this, I set the model up to train and test on the prior 5 games. Modelling with more and less games yielded more variable results, so 5 games was chosen to minimize the noise and account for a teams recent and sustained success. For the testing set, the averages from those 5 games was used. The following figure shows how the model was set up.

![model_setup](https://github.com/rwlink3z8/rlcs2/blob/master/img/model_setup.png)

## Results

Different machine learning algorithms were used but the best performer was a gradient boosted classifier. The data was set up for to train on the first 4 weeks, and then build up to 5 prior games and model each week. The probabilities were taken for each team and converted to expected value. The formula for expected value is as follows:

Expected value = (Amount won per bet * probability of winning) - (Amount lost per bet * (1 - probability of winning))

If the model predicted a negative expected value for both teams, no bet was placed, otherwise, a bet was placed for the team with the higher expected value. 

Using 193 unseen games the model abstained from betting on 37 games, it placed 156 bets and it correctly predicted the outcome of 94/156 games. American money lines are normalized to $100 so that was the bet amount. Over a season the model placed $15,600 in bets and ended the season with $16,698 for a 7% ROI. The results are plotted as well as two controls over the same time period: only betting on the favorite ($441 in losses), and only betting on the underdog ($488 in losses)

![ev_betting4](https://github.com/rwlink3z8/rlcs2/blob/master/img/ev_betting4.png)

## Future work

Currently data is pulled from the cs2take2.ipynb and stored to a csv, the webscrapers run are in the src folder as well as the models used. These will be updated in the coming days.

Football is a highly variable sport with inherently small sample sizes
Future work should include pivoting to baseball because the season is longer making it easier to test on. The house edge is also half what it is in football and basketball to entice people to gamble on baseball. 



Deployment
There are several issues to address before deployment, notably, scraping live money lines, at this time no live sports are happening so this was not possible. Money lines and spreads change and that would make deploying any model difficult.

To scrape a season of statistics follow the instructions in the file located in the src:

`scraper_1.py` 

as of this time issues exist there and stats are scraped from `cs2take2.ipynb` saved to a csv called 'backup_stats5312020.csv and the opened in the modeling file. 


The money line scraper uses selenium to scrape closing money lines from teamrankings.com, this was later replaced by the oddsportal scraper but it is what I used for the 2019 season which was modeled. Further work will continue to use the oddsportal scraper, but it can be run from the following file:

`money_line_scraper.py`









