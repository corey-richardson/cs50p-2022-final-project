##########################################################################
##   ___    __    __  __  ____    _____  ____    ____  ____  ___  ____  ##
##  / __)  /__\  (  \/  )( ___)  (  _  )( ___)  (  _ \(_  _)/ __)( ___) ##
## ( (_-. /(__)\  )    (  )__)    )(_)(  )__)    )(_) )_)(_( (__  )__)  ##
##  \___/(__)(__)(_/\/\_)(____)  (_____)(__)    (____/(____)\___)(____) ##
##                                                                      ##
##########################################################################
##                    ## CS50P Final Project 2022 ##                    ##
##########################################################################
##    github.com/corey-richardson    ||    linktr.ee/coreyrichardson    ##
##########################################################################
## This project was originally created as coursework for my GCSE        ##
## Computer Science course 3 years ago before I even knew what          ##
## object-oriented programming was, however has now been rewritten      ##
## using the understanding of Python I have since gained from CS50P and ##
## other courses. I used the object-oriented programming paradigm to    ##
## create the "player" classes, collating multiple variables - name     ##
## and score - into a single data type with their own methods.          ##
##########################################################################

############################
# FREQUENTLY USED COMMANDS #
############################

# cd Week9/project
# pytest test_project.py

#############################
# ASSIGN KEY VARIABLES HERE #
#############################

# There was an attempt:
# import re
# project_name = re.search("/.[^/]+\.py$",__file__)
# project_name = project_name.group(0)
# ROOT = __file__.strip(project_name)
# DIRECTORY_NAME = ROOT + "/files"

global NUMBER_OF_ITEMS_SCOREBOARD, NUMBER_OF_TURNS
global DIRECTORY_NAME, USERNAMES_PATH, SCOREBOARD_PATH
NUMBER_OF_ITEMS_SCOREBOARD = 5
NUMBER_OF_TURNS            = 5
DIRECTORY_NAME             = "files"
USERNAMES_PATH             = DIRECTORY_NAME + "/usernames.txt"
SCOREBOARD_PATH            = DIRECTORY_NAME + "/scoreboard.txt"

################
# PLAYER CLASS #
################

class Player:
    # Player class
    def __init__(self,name):
        self.name = name
        self.score = 0

    def add_to_score(self,score):
        # Adds the passed in score to the player object score
        self.score += score

    def authenticate(self):
        # Opens the username text file and checks whether the inputted names are in the file
        with open(USERNAMES_PATH) as accepted_names:
            names = accepted_names.readlines()
            for name in list(names):
                if name.rstrip() == self.name:
                    return True
            return False

    def __repr__(self):
        # String representation
        return f"{self.name} had a score of {self.score} points."

####################
# CONTROL FUNCTION #
####################

# MAIN
def main():
    pregame_checks()
    starting_screen()

    play_again = True
    while play_again:

        # Take user input and authenticate
        checked = False
        while not checked:
            player_1_name = input("Enter Player 1's name: ").title().rstrip() # user inputs name
            player_2_name = input("Enter Player 2's name: ").title().rstrip() # "
            checked = validate(player_1_name,player_2_name)

        for i in range(NUMBER_OF_TURNS): # 5 turns
            print(f"\nTurn {i+1}:")
            player_turn(player_1)
            player_turn(player_2)
            print(player_1.__repr__())
            print(player_2.__repr__())

        # after all rounds have been played, compare the scores
        check_for_winner(player_1, player_2)
        play_again = check_play_again()

    print("\nGame over!")

###############################
# PRE GAME DISPLAY AND CHECKS #
###############################

# STARTING SCREEN
def starting_screen():
    art = r'''
  ___    __    __  __  ____    _____  ____    ____  ____  ___  ____
 / __)  /__\  (  \/  )( ___)  (  _  )( ___)  (  _ \(_  _)/ __)( ___)
( (_-. /(__)\  )    (  )__)    )(_)(  )__)    )(_) )_)(_( (__  )__)
 \___/(__)(__)(_/\/\_)(____)  (_____)(__)    (____/(____)\___)(____)

''' # 'Bulbhead' font from patorjk.com/software/taag
    print(art)

    print('''Two players roll two 6-sided dice.
Points are added based on the result of the dice.
The points rolled are added to the score. e.g. 3 and 4 --> 7
If the total is an even number, the user gets an extra 10 points.
If the total is odd, the user loses 5 points.
If the turn score is below 0 it is set back to 0.
If the two dices roll the same, the user gets an additional dice roll.
The person with the highest score after 5 rounds will win.
If the users have the same end result, the game will enter sudden death.
Only authorised users can play the game.\n''')
    input("[Press enter to play]")
    print("")

# PRE GAME CHECKS
def pregame_checks():
    # Set up needed files
    check_dir_exists()
    check_usernames_exists()
    check_scoreboard_exists()

# CHECK DIR EXISTS
def check_dir_exists():
    from os.path import exists
    from os import mkdir
    if not exists(DIRECTORY_NAME):
        mkdir(DIRECTORY_NAME)

# CHECK USERNAMES EXISTS
def check_usernames_exists():
    from os.path import exists
    if not exists(USERNAMES_PATH): # checks the file exists, if no then:
        # Only checks whether the file exists, does not check it contains the right names
        with open(USERNAMES_PATH,"w") as usernames: # create the file
            list_of_names = ["Corey","Carlene","Faith","Frodo","Samwise","Gandalf","Aragorn","Legolas","Gimli","Pippin","Merry","Boromir"]
            for name in list_of_names: # write each element of the name list to the file on a new liine
                usernames.write(name + "\n")

#CHECK SCOREBOARD EXISTS
def check_scoreboard_exists():
    from os.path import exists
    if not exists(SCOREBOARD_PATH):
        with open(SCOREBOARD_PATH,"w") as sb:
            pass

##################
# AUTHENTICATION #
##################

# VALIDATE
def validate(player_1_name,player_2_name):
    # Checks for malicious attempts to bypass authentication
    if player_1_name == "" or player_2_name == "":
        print("Not accepted! Try again!\n")
        return False
    if player_1_name == player_2_name:
        print("Not accepted! Try again!\n")
        return False
    # Uses class functions to check player names are in the username.txt file
    global player_1, player_2
    player_1 = Player(player_1_name) # Create player objects
    player_2 = Player(player_2_name) # "
    player_1_validated = player_1.authenticate() # Authenticate the player, check name is in the list of valid names
    player_2_validated = player_2.authenticate() # "
    # Returns True or False
    if player_1_validated and player_2_validated:
        print(f"LOG: Users {player_1.name} and {player_2.name} are validated.")
        return True # break from while loop
    else:
        print("Not accepted! Try again!\n")
        return False

#############################
# GAME LOGIC AND ARITHMETIC #
#############################

# ROLL DICE
def roll_dice():
    #generates a random integer between 1 and 6
    import random
    dice = random.randint(1,6)
    return dice

# COMPARE DICE
def compare_dice(dice_1,dice_2):
    # checks if doubles have been rolled
    # if yes, roll an extra dice
    # then, sum all dice and return this value
    if dice_1 == dice_2:
        dice_3 = roll_dice()
        turn_score = sum_dice(dice_1,dice_2,dice_3)

        print(f"DOUBLES! Your dice rolls were {dice_1}, {dice_2} and {dice_3}.")
        print(f"These sum to {turn_score} points!")

        return turn_score
    else:
        turn_score = sum_dice(dice_1,dice_2)
        print(f"Your dice rolls were {dice_1} and {dice_2}")
        print(f"These sum to {turn_score} points!")

        return turn_score

# CHECK IF NEGATIVE
def check_if_negative(turn_score):
    if turn_score < 0:
        print("Your score for this turn has been reset to 0!")
        return 0
    else: return turn_score

# EVEN ODD
def even_odd(player, turn_score):
    # Check if odd / even then add to total score for the game
    # if odd: minus 5
    # if even: add 10
    if turn_score % 2 == 1:
        print("ODD NUMBER! You lose 5 points.")
        turn_score -= 5
        turn_score = check_if_negative(turn_score)
        print(f"Your score for this turn is {turn_score}.")
        player.add_to_score(turn_score)
    else:
        print("EVEN! You gain 10 points.")
        turn_score += 10
        turn_score = check_if_negative(turn_score)
        print(f"Your score for this turn is {turn_score}.")
        player.add_to_score(turn_score)

    print(f"Your total score is {player.score}.\n")

# SUM DICE
def sum_dice(dice_1,dice_2,dice_doubles = 0):
    # dice_doubles is only needed when doubles are rolled so it defaults to 0
    return dice_1 + dice_2 + dice_doubles

# PLAYER TURN
def player_turn(player):
    print(f"\n{player.name}:")
    # Roll dice
    input("Press ENTER to roll the dice!")
    dice_1 = roll_dice()
    dice_2 = roll_dice()
    # If doubles rolled, roll again
    # Output the scores and sum the total score for the turn
    even_odd( player, compare_dice(dice_1, dice_2) ) # compare_dice returns turn_score

#########################
# END OF GAME FUNCTIONS #
#########################

# CHECK FOR WINNER
def check_for_winner(player_1,player_2):
    # check which score is higher and output the winner
    # call write_to_scoreboard entering the winner player object
    # if scores are equal call sudden death to get the winner
    if player_1.score > player_2.score:
        print(f"\n{player_1.name} wins!")
        write_to_scoreboard(player_1)
        return player_1.name
    elif player_2.score > player_1.score:
        print(f"\n{player_2.name} wins!")
        write_to_scoreboard(player_2)
        return player_2.name
    else:
        print("It's a draw! Starting sudden death...")
        sudden_death(player_1, player_2)
        print(player_1.__repr__())
        print(player_2.__repr__())

# SUDDEN DEATH
def sudden_death(player_1, player_2): # tested and working :)
    # if player_1.score == player_2.score, reroll until winner is found
    player_turn(player_1)
    player_turn(player_2)
    check_for_winner(player_1, player_2) # recursive, could just pass in player_n object

#######################
# POST GAME FUNCTIONS #
#######################

# WRITE TO SCOREBOARD
def write_to_scoreboard(winner):
    # uses a context manager to append the most recent score to the file
    with open(SCOREBOARD_PATH,"a") as sb:
        to_write = "%03i - %s\n" % (winner.score,winner.name)
        sb.write(to_write) # adds the newest winner score to the scoreboard
    sort_and_cut_scoreboard(NUMBER_OF_ITEMS_SCOREBOARD) # <-- increase or decrease number of items displayed here

# SORT AND CUT SCOREBOARD
def sort_and_cut_scoreboard(how_many):
    with open(SCOREBOARD_PATH) as sb: # read only
        lines = sb.readlines() # save each line to a list
        lines.sort(reverse=True) # sort the list
    with open(SCOREBOARD_PATH,"w") as sb:
        for line in lines[0:how_many]: # select the first five elements from the list
            sb.write(line) # write to file
    display_scoreboard()

# DISPLAY SCOREBOARD
def display_scoreboard():
    # outputs the scoreboard to screen
    with open(SCOREBOARD_PATH) as sb: # read only
        scores = sb.readlines()
        print("\nTop 5 Scores:")
        for score in scores:
            print(score.replace("\n",""))
        print("\n")

# CHECK PLAY AGAIN
def check_play_again():
    input_valid = False
    while input_valid == False:
        play_again = input("Do you want to play again? [y/n] ")

        try:
            match play_again[0].lower(): # replace if-else statement with switch / match statement, cleaner
                case "y":
                    return True
                case "n":
                    return False
                case _:
                    print("Reprompt:")
        except IndexError:
             print("Reprompt:")

########################
# TOP LEVEL CODE CHECK #
########################

if __name__ == "__main__":
    main()