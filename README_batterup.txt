Introduction

In baseball statistics, the slugging percentage (SLG) is a popular measure of the power of a hitter.  You will be given a list of players and their at-bats for a single game.  You will need to compute each player’s slugging percentage.  For this exercise, no player will be hit by a pitch.

The slugging percentage is found by counting all the singles, doubles, triples, and home runs in a given game and applying a set weight to each achievement (home runs are worth more than singles), then dividing that number by the total number of at-bats in that game.

Program

Create a new Python file named BatterUp_LastName. Where "LastName" is replaced by your last name. Important: The first letter of "batter" and "up" should be capitalized along with the first letter of your last name. The rest of the file name should be lowercase. Example: BatterUp_Funderburk. If you have more than one last name, use the first one that shows up in Focus.

Create a fixed variable at the top called LASTNAME and set it equal to your last name.

Students must create a function, slg(data), that accepts one parameter, data, which will be a string of data for that player. This data will include a single string per player that consists of the batter's name, a colon, and some number of at-bats separated by commas. A player's at-bats can be any of the following:

    BB means the player was walked by the pitcher and does not count as an at-bat.
    K is an at-bat where the player struck out and did not reach a base.
    1B is an at-bat where the player hit a single.
    2B is an at-bat where the player hit a double.
    3B is an at-bat where the player hit a triple.
    HR is an at-bat where the player hit a home run.

Please note that not every player in the game has the same number of at-bats. If a player has no at-bats, then their slugging percentage should be zero.

Your function should return the player's name as it appears in the parameter, data, an equals sign, and then their slugging percentage rounded to 3 decimal places. No spaces.