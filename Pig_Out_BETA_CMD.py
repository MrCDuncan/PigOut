#Final Project BETA Pig Out script BETA CDuncan 3/1/20
import random
print ('Here are the rules of Pig Out:')
print ('Each player is trying to get to a score of 100 without going over')
print ('A player may roll or pass')
print ('If a player rolls a 1, then their score goes back to 0')
print ('If a player goes over 100, they lose.')
print ('Good Luck!')
print (' ')

player1 = input('Player 1 name: ')
player2 = input('Player 2 name: ')
turn = 'r'
roll = 2
score1 = 0
score2 = 0
playagain = 'y'

while (playagain == 'y') or (playagain == 'Y'):
    
    while (score1 < 100) and (score2 < 100):

        while (roll > 1) and ((score1 < 100 ) and (score2 < 100)) and ((turn == 'r') or (turn == 'R')):
            print (' ')
            print (player1, 'rolls the dice')
            roll = random.randint(1,6)
            score1 += roll
            print ('You rolled a', roll)
            if score1 >= 101:
                print ('Busted! You rolled over 100.')
            elif roll == 1:
                score1 = 0
                roll = 0    
                print ('Pig Out! Score is now', score1, player2, ', Your turn.')
            else:
                print ('    Your score is', score1)
                print (' ')
                if score1 < 100:
                    turn = input('Type p if you want to pass the dice or r to roll again: ')
        turn = 'r'
        roll = 2
    
        while ((roll > 1) and (score1 < 100 and score2 < 100) and (turn == 'r' or turn == 'R')):
            print (' ')
            print (player2, 'rolls the dice')
            roll = random.randint(1,6)
            score2 += roll
            print ('You rolled a', roll)
            if score2 >= 101:
                print ('Busted! You rolled over 100.')
                roll = 0
            elif roll == 1:
                score2 = 0
                roll = 0
                print ('Pig Out! Score is now, ',score2, player1, ', Your turn.')
            else:
                print ('    Your score is', score2)
                print (' ')
                if score2 < 100:
                    turn = input('Type p if you want to pass the dice or r to roll again:  ')
        turn ='r'
        roll = 2
    
    if score1 == 100:
        print ('Perfect score! ')
    elif score2 == 100:
        print ('Perfect score! ')
    if (score1 <= 100) and (score2 > 100):
        print (player1, 'WINS!')
    elif (score2 <= 100) and (score1 > 100):
        print (player2, 'WINS!')	
    print (' ')
    print ('Final Score:')
    print (player1, ': ', score1)
    print (player2, ': ', score2)
    print ('Good game! Pay up all bets.')
    print (' ')
    turn = 'r'
    roll = 2
    score1 = 0
    score2 = 0
    playagain = input('Want to play again? y or n: ')

print (' ')    
print ('Thank you! Come back soon.')
#end
