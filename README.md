
# Football simulation

A program that will create players, teams and leagues.  

Clone the repoTo install:  

    pip install .  

## Example usage  

In a python interpreter:  

    import football.seasons as fs

    s = fs.Season()
    
    s.play_season()

    s.league_table
   
The above will create a Season object consisting of a league, 20 teams and 23 players for each team.  
Season will then create and play a whole seasons worth of fixtures and then display the league table at the end of the season

Congratulations to 'Dornoch', the winners of the first full season of the Reed league 2019/2020.


<img src="https://github.com/jr-42/football_simulation/blob/develop/images/league.png" alt="drawing" width="500"/>

