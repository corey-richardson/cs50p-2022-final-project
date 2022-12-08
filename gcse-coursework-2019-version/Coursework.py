# more functions / procedures (scoreboards)
global gameOn
gameOn = True

#################
# Authenticator #
#################

# Defines a function called authenticateUser()
# This function is used to check the users credentials by cross-referencing their name against a list in a word file.
# Later on in the program, the function is called to variables, player1 and player2. 
def authenticateUser(i):
    # Authenticator  
    # Opens a file containing username list
    # Splits file into a list
    # Closes file
    f=open("usernames.txt", 'r')
    userList = f.readline()
    userList = userList.split()
    f.close()
    
    # Var assignments
    attempts = 0 
    locked = False
    login = False

    # While loop allows me to break the loop easily
    while locked == False:         
        # Asks user for input
        userName = input("Player %s: Please enter your username: " % (i))
        # Checks user input against list
        if userName in userList:
            print("Logged In\n")
            login = True
            locked = True
            return userName
                  
        # If the name isn't on the list, checks how many attempts have been taken
        # Too many attempts "locks" the game
        else:
            print("Unsuccessful login.")
            attempts += 1
            if attempts >= 5:
                locked = True
                # if you have too many attempts, it will lock the
                # program for 5 minutes
                # this will help to prevent brute force attacks, increasing
                # how robust the program is
                import time
                print("Locked out - please wait - 5 Minutes")
                time.sleep(300)
                attempts -= 1
                locked = False
                
            else:
                pass
                     
#########
# Rules #
#########

global player1Score
global player2Score

player1Score = 0
player2Score = 0

def rules():
    #shows the rules of the game
    print('''Two players roll two 6-sided dice.
Points are added based on the result of the dice.
The points rolled are added to the score. e.g. 3 and 4 --> 7
If the total is an even number, the user gets an extra 10 points.
If the total is odd, the user loses 5 points.
If the two dices roll the same, the user gets an additional dice roll.
The score cannot fall below 0. If this happens, your score will be reset to 0.
The person with the highest score after 10 rounds will win.
If the users have the same end result, the game will enter sudden death.

Only authorised users can play the game.

''')

# generates random number
def rollDice():
    import random
    dice = random.randint(1,6)
    return dice

# if the two dices are doubles, this function will roll an extra dice
def doubles():
    import random
    dice = random.randint(1,6)
    return dice

# adds the value of dice1 and dice2
def diceAdd(dice1, dice2,dice3):
    diceTotal = dice1 + dice2 + dice3
    return diceTotal

# Player 1 Turn
def player1Turn(player1Score):
    import time
    time.sleep(0.5)
    # formatting
    print("It is now %s's turn." % (player1))
    print("Press ENTER / RETURN to roll the dice!")
    input()
    # runs rollDice function, x2
    dice1 = rollDice()
    dice2 = rollDice()
    # compares for doubles
    if dice1 == dice2:
        print("Doubles! Extra roll!")
        dice3 = rollDice()
    else:
        dice3 = 0
    # uses diceTotal function to calculate score
    diceTotal = diceAdd(dice1,dice2,dice3)
        
    # prints diceTotal
    print("You got a score of %s!\n" % (diceTotal))
    # checks if odd / even
    if diceTotal % 2 == 1:
        # if odd, -5 points
        print("However, this is an odd number. You lose 5 points.")
        diceTotal -= 5
    else:
        # if even +10 points
        print("You gain 10 points for an even number!")
        diceTotal+= 10
    print("Your overall score for this round is %s!\n" % (diceTotal))
    player1Score = player1Score + diceTotal
    return player1Score

# player 2 turn
def player2Turn(player2Score):
    import time
    time.sleep(0.5)
    print("It is now %s's turn." % (player2))
    print("Press ENTER / RETURN to roll the dice!")
    input()
    # runs rollDice function x2
    dice1 = rollDice()
    dice2 = rollDice()
    #compares and checks for doubles
    if dice1 == dice2:
        print("Doubles! Extra roll!")
        dice3 = rollDice()
    else:
        dice3 = 0
        # finds dice total
    diceTotal = diceAdd(dice1,dice2,dice3)

    print("You got a score of %s!\n" % (diceTotal))
    if diceTotal % 2 == 1:
        print("However, this is an odd number. You lose 5 points.")
        diceTotal -= 5
    else:
        print("You gain 10 points for an even number!")
        diceTotal+= 10
    print("Your overall score for this round is %s!\n" % (diceTotal))
    player2Score = player2Score + diceTotal
    return player2Score

def winnerCheck(player1Score,player2Score):
    # checks who has the higher overall score
    if player1Score > player2Score:
        return True
    elif player1Score == player2Score:
        draw = True
        # Runs sudden death function
        suddenDeath()
    else:
        return False

# procedure
def suddenDeath():
    import time
    # wait for added effect :)
    time.sleep(1)
    print("SUDDEN DEATH")
    time.sleep(1)
    print("%s, roll dice!" % (player1))
    input()
    # rolls dice
    suddenScore1 = rollDice()
    print("\n%s, roll dice!\n" % (player2))
    input()
    # rolls dice
    suddenScore2 = rollDice()
    # tension
    print("One person got a score of %s. The other, a score of %s\n" % (suddenScore1, suddenScore2))
    time.sleep(1)
    # drama
    print("%s had a score of %s!" % (player1,suddenScore1))
    print("%s had a score of %s!" % (player2,suddenScore2))
    winnerCheck(suddenScore1,suddenScore2)

# Writes the top users score to a .txt file
# Add sorting and removing # but doesnt work
def writeScoreboard(playerName,playerScore):
    # write into a file
    playerScore = str(playerScore)
    if len(playerScore) == 2:
        playerScore = "0" + playerScore
    elif len(playerScore) == 1:
        playerScore = "00" + playerScore
    f = open("scoreboard.txt","a")
    f.write(str(playerScore)+" "+str(playerName)+"\n")
    f.close()

    f = open("scoreboard.txt","r")
    lines=f.readlines()
    f.close()

    lines.sort(reverse = True)

    f = open("scoreboard.txt","w")
    f.writelines(lines)
    f.close()  
    
# Shows the scoreboard .txt file
def showScoreboard():
    print("\nScoreboard:")
    f = open("scoreboard.txt","r")
    for lines in f:
        print(lines)
    f.close()
    print("\n\n")
    
# open file
# read
# sort
# close
# reopen file
# write
# close

# overall main loop / control loop
def mainLoop(player1Score,player2Score):
    import time
    # for loop to have 10 rounds
    for i in range(1,11):
        time.sleep(0.2)
        print("\nRound %s:\n" % (i))
        # runs player turn functions
        player1Score = player1Turn(player1Score)
        player2Score = player2Turn(player2Score)
        # checks score maintains over 0
        if player1Score < 0:
            player1Score = 0
            
        elif player2Score < 0:
            player2Score = 0
            
        else:
            pass
        print("%s has a current score of %s." % (player1,player1Score))
        print("%s has a current score of %s.\n" % (player2,player2Score))
    winner = False
    # checks who won the game
    winner = winnerCheck(player1Score,player2Score)
    if winner == True:
        print("\n%s wins!\n" % (player1))
        writeScoreboard(player1,player1Score)
    else:
        print("\n%s wins!\n\n" % (player2))
        writeScoreboard(player2,player2Score)

#############
# Main Menu #
#############
def mainMenu():
    player1Score = 0
    player2Score = 0
    menu = '''Play [G]ame
Show [R]ules
Show [S]coreboard
[E]xit
'''
    print(menu)
    gameSelect = input()
    gameSelect = gameSelect.lower()
    if gameSelect[0] == "g":
        # Runs the authenticateUser() function and assigns the returned value to variables
        # Also checks the names are different. 
        dif = False

        while dif == False:
            global player1
            player1 = authenticateUser(1)
            global player2
            player2 = authenticateUser(2)
    
            if player1 == player2:
                print("You have used the same login both times.")
                print("Please re-login using different users.\n")
        
            else:
                dif = True
                print("Welcome to the Dice Game!")
                mainLoop(player1Score,player2Score)      

    elif gameSelect[0] == "r":
        rules()
    elif gameSelect[0] == "s":
        showScoreboard()
    elif gameSelect[0] == "e":
        gameOn = False
        exit()
    
while gameOn == True:
    mainMenu()

# End break
input()
