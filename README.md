
# Football simulation

A program that will create players, teams and leagues.

Current features:
- Create a league
- Simulate multiple seasons
- Get tables and stats for each season
- Get fixtures and results for individual teams
- Get fixtures and results for league seasons and rounds
- Relegation (* lose three bottom teams each year)
- Each team has own play style and rating
- Each player has own position and basic information 
- Player stats (scoring and appearances)
- Lineups for each game
- Rewards for position finished in league (money, improving rating, new players etc)

Short Term : Future improvements and features:
- Improve match engine 
- Take form into account when calculating win/loss probabilities
- League heirarchy (promotion and relegation)

Long Term : Future improvements and features:
- Add GUI for interactivity
- Ability to create own team and manage à la Football Manager (which i am definitely not copying)

## To install on mac

- Clone the repo into a folder and then with terminal:

```
python3 -m venv .venv
source .venv/bin/activate
pip install .
```

## Example usage  

See Jupyter Notebook

Congratulations to 'Lochgilphead'. Winners of the 2019/2020 and 2020/2021 Joe League. Hard luck for 'Axminster Town', losing out on goal difference in season 2.


<img src="https://github.com/jr-42/football_simulation/blob/develop/images/season1.png" alt="drawing" width="500"/>


<img src="https://github.com/jr-42/football_simulation/blob/develop/images/season2.png" alt="drawing" width="500"/>
