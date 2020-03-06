#Import libraries
import random
import turtle  

#**
# * Chris Duncan
# * Object Oriented Progrmaing
# * Spring 2020 Semester, week 8, Final Class Project
# * Pig Out! The game. A Python version of the game pass the pig.

#Set varabiles
scoreP1 = 0
scoreP2 = 0
global turn
turn = 0
global playagain
playagain = 'y'
global player
player = 1

#Set up graphical display
draw=turtle.Turtle()
draw.pensize(5)     

#Pig renderings
def sider():
    x = random.randint(-300, 300)  #Random placing of shapes on cavas
    y = random.randint(-300, 300)
    draw.penup()
    draw.setpos(x,y)
    draw.pendown()
    draw.forward(150)    
    draw.right(90)
    draw.forward(100)
    draw.right(90) 
    draw.forward(150)    
    draw.right(90)
    draw.forward(100)
    draw.penup()
    draw.setpos(x,y)
    draw.left(180)
    draw.forward(50)
    draw.left(90)
    draw.forward(70)
    draw.pendown()
    if pigRoll.spot == 1:  #Determines if pig is showing a dot on it's side
        draw.circle(5)
    draw.penup() 
    draw.home()    
    draw.ht()
    draw.st()

def razorback():
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    draw.penup()
    draw.setpos(x,y)
    draw.pendown()
    draw.left(105)
    draw.forward(150)     
    draw.right(215)
    draw.forward(155)
    draw.left(110) 
    draw.forward(90)     
    draw.left(140)
    draw.penup()
    draw.setpos(x,y)
    draw.left(10)
    draw.forward(50)
    draw.pendown()
    if pigRoll.spot == 1:
        draw.circle(5)
    draw.penup() 
    draw.home()    
    draw.ht()
    draw.st()

def trotter():
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    draw.penup()
    draw.setpos(x,y)
    draw.pendown()
    draw.left(25)
    draw.forward(150)     
    draw.right(115)
    draw.forward(100)
    draw.right(105) 
    draw.forward(137)     
    draw.right(40)
    draw.penup()
    draw.setpos(x,y)
    draw.right(125)
    draw.forward(100)
    draw.pendown()
    if pigRoll.spot == 1:
        draw.circle(5)
    draw.penup() 
    draw.home()    
    draw.ht()
    draw.st()

def snouter():
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    draw.penup()
    draw.setpos(x,y)
    draw.pendown()
    draw.right(105)
    draw.forward(150)     
    draw.left(215)
    draw.forward(155)
    draw.right(110) 
    draw.forward(90)     
    draw.left(40)
    draw.penup()
    draw.back(50)
    draw.pendown()
    if pigRoll.spot == 1:
        draw.circle(5)
    draw.penup() 
    draw.home()    
    draw.ht()
    draw.st()

def leaner():
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    draw.penup()
    draw.setpos(x,y)
    draw.pendown()
    draw.left(25)
    draw.forward(150)    
    draw.right(115)
    draw.forward(65)
    draw.right(90) 
    draw.forward(135)     
    draw.right(40)
    draw.penup()
    draw.setpos(x,y)
    draw.right(130)
    draw.forward(100)
    draw.pendown()
    if pigRoll.spot == 1:
        draw.circle(5)
    draw.penup() 
    draw.home()    
    draw.ht()
    draw.st()

def oinker():  #Draws a pig face when player  looses all points
    draw.home()
    #head
    n = 6
    draw.pencolor('red')
    for i in range(n):     #Loop to minimze amount of code needed for polygon
        draw.forward(100)     
        draw.right(360/n)   #determining the exterior angle of the polygon
    draw.penup()
    draw.home()
    draw.pencolor('blue')
    #nose R
    draw.right (50)
    draw.forward(115) 
    draw.pendown()  
    for i in range(n):     
        draw.forward(12)     
        draw.right(360/n)  
    draw.penup()
    draw.home
    #nose L
    draw.right(100)
    draw.forward(35)
    draw.pendown()
    for i in range(n):     
        draw.forward(12)    
        draw.right(360/n)    
    draw.penup()
    draw.home()
    #ear L
    draw.right(175)
    draw.forward(5)
    draw.pendown()
    for i in range(n):     
        draw.forward(30)    
        draw.right(360/n)    
    draw.penup()
    draw.home()
    #ear R
    draw.right(15)
    draw.forward(60)
    draw.left(65)
    draw.forward(55)
    draw.pendown()
    for i in range(n):     
        draw.forward(30)     
        draw.right(360/n)    
    draw.penup()
    draw.home()
    #eye L
    draw.right(260)
    draw.back(45)
    draw.pendown()
    for i in range(n):     
        draw.forward(6)     
        draw.right(360/n)    
    draw.penup()
    draw.home()
    #eye R
    draw.forward(75)
    draw.left(90)
    draw.back(45)
    draw.pendown()
    for i in range(n):     
        draw.forward(6)     
        draw.right(360/n)    
    draw.penup()
    draw.goto(-300,-300)
    draw.st()

def instructions():  #Displays instructions at start of game
    print ('Here are the rules of Pig Out - aka Pass The Pig:')
    print ('Each player is trying to get to a score of 100')
    print ('A player may roll or pass')
    print ('Each turn involves one player throwing two model pigs, each of which has a dot on one side.\nThe player gains or loses points based on the way the pigs land.\nEach turn lasts until the player throwing either rolls the pigs in a way that wipes out their current score, is one sider with a dot and one with out, or decides to stop their turn.')
    print ('Sider - The pigs are on their sides, either both with the spot facing upward or both with the spot facing downward - 1 Point')
    print ('Double Razorback - The pigs are both lying on their backs - 20 Points')
    print ('Double Trotter - The pigs are both standing upright - 20 Points')
    print ('Double Snouter - The pigs are both leaning on their snouts - 40 Points')
    print ('Double Leaning Jowler - The pigs are both resting between snouts and ears - 60 Points')
    print ('Pig Out - If both pigs are lying on their sides, one with the spot facing upwards and one with the spot facing downwards the score for that player is reset to 0 and the turn changes to the next player')
    print ('Oinker- If both pigs are touching in any position,[2] then the total score is reset to 0 and the turn changes to the next player')
    print ('Mixed Combo - A combination not mentioned above is the sum of the single pigs scores')
    print ('   Razorback - The pig is lying on its back - 5 Points')
    print ('   Trotter - The pig is standing upright - 5 Points')
    print ('   Snouter - The pig is leaning on its snout - 10 Points')
    print ('   Leaning Jowler - The pig is resting on its snout and ear - 15 Points')
    print ('Good Luck!')
    print (' ')

def pigRoll():   #Function for rolling the pigs and calling the proper rendering. 
    pigRoll.wipe = 0
    pigRoll.passPig = 0
    matchingDot = 0
    rollP1 = random.randint(0,100)   #Random number for Pig 1
    rollP1dot = random.randint(1,3)  #Determine if Pig 1 has a dot on its side
    rollP2 = random.randint(0,100)   #Random number for Pig 2
    rollP2dot = random.randint(1,3)  #Determine if Pig 2 has a dot on its side
    if (rollP1dot == rollP2dot) or (rollP1dot + rollP2dot == 5):
        matchingDot = 1
    if rollP1 == 0:
        rollP2 = 0
    if rollP2 == 0:
        rollP1 = 0
    
    # Determine which rendering to call and collect points for scoreing 
    # Pig 1
    draw.clear()   
    draw.pencolor('red')
    if rollP1 == 0:
        print ('You rolled an Oinker! Your score is reset to zero.')
        pigRoll.score1 = 0
        pigRoll.wipe = 1
        oinker()
        rollP1 = 999
    if rollP1 < 65:  #Random number range is weighted to give rolls real world relative frequencies
        print ("First Pig is a sider")
        shape1 = "sider"
        if rollP1dot == 1:
            pigRoll.spot = 1
        else:
            pigRoll.spot = 0
        if (rollP1 > 0 and rollP1 < 65) and (rollP2 > 0 and rollP2 < 65) and (matchingDot == 1):  # determins of same pig shape matching dot or no dot was rolled for both pigs which is worth bonus points
            pigRoll.score1  = 1
        else:
            pigRoll.score1 = 0
        sider()
        rollP1 = 999
    if rollP1 < 88:
        print ("First Pig is a Razorback")
        shape1 = "razor"
        if rollP1dot == 1:
            pigRoll.spot = 1
        else:
            pigRoll.spot = 0
        if (rollP1 > 64 and rollP1 < 88) and (rollP2 > 64 and rollP2 < 88):
            pigRoll.score1 = 20
        else:
            pigRoll.score1 = 5
        razorback()
        rollP1 = 999
    if rollP1 < 96:
        print ("First Pig is a Trotter")
        shape1 = "trot"
        if rollP1dot == 1:
            pigRoll.spot = 1
        else:
            pigRoll.spot = 0
        if (rollP1 > 87 and rollP1 < 96) and (rollP2 > 87 and rollP2 < 96):
            pigRoll.score1 = 20
        else:
            pigRoll.score1 = 5
        trotter()
        rollP1 = 999
    if rollP1 < 99:
        print ("First Pig is a Snouter")
        shape1 = 'snout'
        if rollP1dot == 1:
            pigRoll.spot = 1
        else:
            pigRoll.spot = 0
        if (rollP1 > 95 and rollP1 < 99) and (rollP2 > 95 and rollP2 < 99):
            pigRoll.score1 = 40
        else:
            pigRoll.score1 = 10
        snouter()
        rollP1 = 999
    if rollP1 < 101:
        print ("First Pig is a Leaning Jowler")
        shape1 = 'lean'
        if rollP1dot == 1:
            pigRoll.spot = 1
        else:
            pigRoll.spot = 0
        if (rollP1 > 98 and rollP1 < 101) and (rollP2 > 98 and rollP2 < 101):
            pigRoll.score1 = 60
        else:
            pigRoll.score1 = 15
        leaner()
        rollP1 = 999
    
    # Pig 2
    draw.pencolor('blue')
    if rollP2 == 0:
        pigRoll.score2 = 0
        rollP2 = 999
    if rollP2 < 65:
        print ("Second Pig is a sider")
        if rollP2dot == 1:
            pigRoll.spot = 1
        else:
            pigRoll.spot = 0
        if shape1 == 'sider':
            pigRoll.score2  = 0
        else:
            pigRoll.score2 = 0
        if shape1 == 'sider' and  matchingDot == 0:
            pigRoll.passPig = 1
        sider()
        rollP2 = 999
    if rollP2 < 87:
        print ("Second Pig is a Razorback")
        if rollP2dot == 1:
            pigRoll.spot = 1
        else:
            pigRoll.spot = 0
        if shape1 == 'razor':
            pigRoll.score2 = 0
        else:
            pigRoll.score2 = 5
        razorback()
        rollP2 = 999
    if rollP2 < 95:
        print ("Second Pig is a Trotter")
        if rollP2dot == 1:
           pigRoll.spot = 1
        else:
            spot = 0
        if shape1 == 'trot':
            pigRoll.score2 = 0
        else:
            pigRoll.score2 = 5
        trotter()
        rollP2 = 999
    if rollP2 < 98:
        print ("Second Pig is a Snouter")
        if rollP2dot == 1:
            pigRoll.spot = 1
        else:
            spot = 0
        if shape1 == 'snout':
            pigRoll.score2 = 0
        else:
            pigRoll.score2 = 10
        snouter()
        rollP2 = 999
    if rollP2 < 101:
        print ("Second Pig is a Leaning Jowler")
        if rollP2dot == 1:
            pigRoll.spot = 1
        else:
            pigRoll.spot = 0
        if shape1 == 'lean':
            pigRoll.score2 = 0
        else:
            pigRoll.score2 = 15
        leaner()
        rollP2 = 999

# MAIN
instructions() # Call to instructions
player1 = input('Player 1 name: ')  #User name input
player2 = input('Player 2 name: ')


while (playagain == 'y' or playagain == 'Y'):                                               #Loop to repeat game play
    while (scoreP1 < 100) and (scoreP2 < 100) and (turn != 'q' and turn !='Q'):        #Loop to end game play based on score or quit request
        while (player == 1) and (scoreP1 < 100 ) and (scoreP2 < 100):   #Loop for first player 
            print (' ')
            print (player1, 'rolls the pigs')
            pigRoll()                                                    #Call to pig rolling function
            scoreP1 = (scoreP1 + (pigRoll.score1 + pigRoll.score2))
            if pigRoll.wipe == 1:
                scoreP1 = 0
                player = 2
            if scoreP1 >= 100:
                print (player1, ' WINS With A Score of ', scoreP1)
                print (player2, ' Comes in second with a score of ', scoreP2)
            else:
                print ('    Your score is', scoreP1)
                print (' ')
            if pigRoll.passPig == 1:
                player = 2
                print (' Pigout! -no points and the roll passes to next player')
                pigRoll.passPig = 0
            if scoreP1 < 100 and pigRoll.wipe == 0 and player != 2:
                turn = input('Press p to pass the pigs, r to roll again and q to quit: ')
                if turn == 'q' or turn == 'Q':
                    break
                elif turn == 'r' or turn == 'R':
                    player = 1
                else:
                    player = 2
                
        while (player == 2) and (scoreP1 < 100 ) and (scoreP2 < 100):      #Loop for second player
            print (' ')
            print (player2, 'rolls the pigs')
            pigRoll()
            scoreP2 = (scoreP2 + (pigRoll.score1 + pigRoll.score2))
            if pigRoll.wipe == 1:
                scoreP2 = 0
                player = 1
            if scoreP2 >= 100:
                print (player2, ' WINS With A Score of ', scoreP2)
                print (player1, ' Comes in second with a score of ', scoreP1)
            else:
                print ('    Your score is', scoreP2)
                print (' ')
            if pigRoll.passPig == 1:
                player = 1
                print (' Pigout! -no points and the roll passes to next player')
                pigRoll.passPig = 0
            if scoreP2 < 100 and pigRoll.wipe == 0 and player != 1:
                turn = input('Press p to pass the pigs, r to roll again and q to quit: ')
                if turn == 'q' or turn == 'Q':
                    break
                elif turn == 'r' or turn == 'R':
                    player = 2
                else:
                    player = 1
   
   #Closing out of game
    print (' ')
    print ('Final Score:')
    print (player1, ': ', scoreP1)
    print (player2, ': ', scoreP2)
    print ('Good game! Pay up all bets.')
    print (' ')
    turn = 'r'
    player = 1
    scoreP1 = 0
    scoreP2 = 0
    playagain = input('Want to play again? y or n: ')

print (' ')    
print ('Thank you! Yall Come back now ya hear!')
#end
