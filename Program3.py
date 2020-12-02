# Grading ID: D9744
#Program #3
#Course - CIS 443
#Section - 01
#Due - Nov. 2, 2020
#This program will 
"""Simulating the dice game Craps."""
import random

gamecount = 0
wincount = 0
losscount = 0
num_of_games = 1000
wins = {}
losses = {}
#all_rolls = {}

def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple

def display_dice(dice):
    """Display one roll of the two dice."""
    die1, die2 = dice  # unpack the tuple into variables die1 and die2
    #print(f'Player rolled {die1} + {die2} = {sum(dice)}')

die_values = roll_dice()  # first roll
display_dice(die_values)

while gamecount != num_of_games:
    rollcount = 0
    die_values = roll_dice()
    rollcount += 1
    display_dice(die_values)

# determine game status and point, based on first roll
    sum_of_dice = sum(die_values)

    if sum_of_dice in (7, 11):  # win
        wincount += 1
        gamecount += 1
        if rollcount in wins:
            wins[rollcount] += 1
        else:
            wins[rollcount] = 1
        game_status = 'WON'
    elif sum_of_dice in (2, 3, 12):  # lose
        losscount += 1
        gamecount += 1
        if rollcount in losses:
            losses[rollcount] += 1
        else:
            losses[rollcount] = 1
        game_status = 'LOST'
    else:  # remember point
        game_status = 'CONTINUE'
        my_point = sum_of_dice
        #print('Point is', my_point)

# continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        rollcount += 1
        display_dice(die_values)
        sum_of_dice = sum(die_values)
    
        if sum_of_dice == my_point:  # win by making point
            game_status = 'WON'
            wincount += 1
            if rollcount in wins:
                wins[rollcount] += 1
            else:
                wins[rollcount] = 1
            gamecount += 1
        elif sum_of_dice == 7:  # lose by rolling 7
            game_status = 'LOST'
            losscount += 1
            if rollcount in losses:
                losses[rollcount] += 1
            else:
                losses[rollcount] = 1
            gamecount += 1
        
print(wins)  #test statments
print(losses) #test statments


# display "wins" or "loses" message
# if game_status == 'WON':
#     print('Player wins')
# else:
#     print('Player loses')
    
    
print(f'Percentage of wins: {wincount*100/(gamecount):.2f}%')
print(f'Percentage of losses: {losscount*100/(gamecount):.2f}%')
print('Percentage of wins/losses based on total number of rolls')
print()
print('{:>25}{:>20} '.format('% Resolved','Cummulative %'))
print('{:<5}{:>20} {:>20}'.format('Rolls','on this roll','of games resolved'))

all_rolls = {**wins, **losses}

# for key in all_rolls.keys():
#     roll_resolved = all_rolls[key] * 100 / gamecount
    
    
##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
