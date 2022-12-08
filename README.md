# Game of Dice
#### Video Demo:  <URL HERE>
#### Description:

This project was originally created as coursework for my GCSE Computer Science course 3 years ago before I even knew what object-oriented programming was, however has now been rewritten using the understanding of Python I have since gained from CS50P and other courses.

I used the object-oriented programming paradigm to create the "player" classes, collating multiple variables - name and score - into a single data type with their own methods.

**[linktr.ee](https://linktr.ee/coreyrichardson) | [github](https://github.com/corey-richardson) | [linkedin](https://www.linkedin.com/in/corey-richardson-833300247/) | [youtube](https://www.youtube.com/@corey-richardson) | [project-repository](https://github.com/corey-richardson/cs50p-2022-final-project)**

---

## CS50P Final Project Requirements:
- Your project must be implemented in Python. ```yes```
- Your project must have a main function and three or more additional functions. ```yes```
- At least three of those additional functions must be accompanied by tests that can be executed with pytest. ```yes```
- Your main function must be in a file called project.py ```yes```
- Your 3 required custom functions other than main must also be in project.py and defined at the same indentation level as main. ```yes```
- Your test functions must be in a file called test_project.py, which should also be in the “root” of your project. ```yes```
- Be sure they have the same name as your custom functions, prepended with test_ ```yes```
- Implementing your project should entail more time and effort than is required by each of the course’s problem sets. ```yes```
- Any pip-installable libraries that your project requires must be listed, one per line, in a file called requirements.txt in the root of your project. ```none required```

---

- classes and objects
- file i/o
- functions
- exceptions
- unit testing

---

## Functions and Procedures:

**Player.\_\_init__() dunder method** Initialises an object with a provided name and sets score = 0
```
self.name = name
self.score = 0
```
**Player.add_to_score()** Adds the provided score to the total score for the player
```
self.score += score
```
**Player.authenticate()** Opens the "username.txt" file and checks the players name is in the file and is therefore allowed to play. SEE **PIOs** FURTHER DOWN FOR MORE INFORMATION.

**Player.\_\_repr__() dunder method** String representation for the player object.
```
return f"{self.name} had a score of {self.score} points."
```
**starting_screen() procedure** Displays ASCII art and the rules, pauses before the game starts. Uses a "raw string" to prevent escape characters from having any effect.
```
art = r'''
  ___    __    __  __  ____    _____  ____    ____  ____  ___  ____
 / __)  /__\  (  \/  )( ___)  (  _  )( ___)  (  _ \(_  _)/ __)( ___)
( (_-. /(__)\  )    (  )__)    )(_)(  )__)    )(_) )_)(_( (__  )__)
 \___/(__)(__)(_/\/\_)(____)  (_____)(__)    (____/(____)\___)(____)

'''
```

**check_dir_exists() procedure** Checks that the directory "files" exists and if it doesn't then create the folder.
```
if not exists("files"):
    mkdir("files")
```

**check_usernames_exists() procedure** Checks that "usernames.txt" exists and if it doesn't then create the file and add the valid names to it
```
if not exists("usernames.txt"):
    with open("usernames.txt","w") as usernames:
        for name in list_of_names:
            usernames.write(name + "\n")
```

**check_scoreboard_exists() procedure** Checks that "scoreboard.txt" exists, if not then create it
```
from os.path import exists
if not exists("scoreboard.txt"):
    with open("scoreboard.txt","w") as sb:
        pass
```

**validate() function** Takes both player names as arguments. Checks for various ways a user could bypass the authentication system, e.g. entering the same name twice or entering empty names. Then will create the class objects for each player and call the class function "authenticate()" If both authentication checks return True then validate() will return True.

**roll_dice() function** Uses the "random" module to generate and return a random number between 1 and 6.
```
import random
dice = random.randint(1,6)
return dice
```

**compare_dice() function** Takes the value of both dice as arguments. Checks to see if the dice are equal; doubles. If they are then it will one again call "roll_dice()". Provides output to let the player know their score for that turn. Returns "turn_score"

**check_if_negative() function** Checks if turn_score was less than 0. If it is, return 0 to prevent the user from losing points.
```
if turn_score < 0:
    print("Your score for this turn has been reset to 0!")
    return 0
else: return turn_score
```

**even_odd() procedure** Checks if the turn_score is even or odd. If it is odd, then it subtracts 5 points and uses the class function "player.add_to_score()" to add the turn_score to the total score. Outputs the turn score to screen.

**sum_dice() function** Calculates the total score for all dice. As dice_3 is only created when doubles occur, this value defaults to 0. Returns dice_total.
```
return dice_1 + dice_2 + dice_doubles
```

**player_turn() procedure** Takes the player object as an argument. Outputs the player name. Lets the user roll two dice. Calls compare_dice() as an argument of even_odd().

    even_odd( player, compare_dice(dice_1, dice_2) )

**check_for_winner() function** Takes both player objects as arguments. Compares the players total scores and calls "write_to_scoreboard()" on the winner player object before returning the winning players name. If the scores are equal then call "sudden_death()"
```
if player_1.score > player_2.score:
    print(f"\n{player_1.name} wins!")
elif player_2.score > player_1.score:
    print(f"\n{player_2.name} wins!")
else:
    sudden_death(player_1, player_2)
```

**sudden_death() recursive procedure** If the players have the same score then they each get an extra turn. This continues until there is a difference in final score. Calls "check_for_winner()".

**write_to_scoreboard() procedure** Appends the winning score and name to a text file. Uses leading 0's to three digits to make sure values are comparable for sorting: "12" is sorted as higher than "119" but "012" is sorted as lower than "119". Calls "sort_and_cut_scoreboard()". If "scoreboard.txt" does not exist, it will create it
```
to_write = "%03i - %s\n" % (winner.score,winner.name)
sb.write(to_write)
```

**sort_and_cut_scoreboard() procedure** Saves each line in the scoreboard file to a list and sorts them in descending order. Then, write the top "how_many" (I've set this to 5) scores to the file. Calls "display_scoreboard()"
```
how_many = 5
```
```
with open("scoreboard.txt") as sb:
    lines = sb.readlines()
    lines.sort(reverse=True)
with open("scoreboard.txt","w") as sb:
    for line in lines[0:how_many]:
        sb.write(line)
```

**display_scoreboard() procedure** Iterates through each lines of the file and prints to screen. Removes the "\n" new line character as Python already adds one of these whilst printing.

**check_play_again() function** Asks the user if they want to play again. If they do then return True, if they don't then return False; this breaks a while loop in "main()". Only compares against the first character of an inputted string so "y"/"yes"/"yeah" and "n"/"no"/"nope" are all valid entries. If a KeyError is raised, i.e. when input is empty then a "try: except:" is used to reprompt until valid input is provided.

---
# Showcase

## Starting Screen

      ___    __    __  __  ____    _____  ____    ____  ____  ___  ____
     / __)  /__\  (  \/  )( ___)  (  _  )( ___)  (  _ \(_  _)/ __)( ___)
    ( (_-. /(__)\  )    (  )__)    )(_)(  )__)    )(_) )_)(_( (__  )__)
     \___/(__)(__)(_/\/\_)(____)  (_____)(__)    (____/(____)\___)(____)


    Two players roll two 6-sided dice.
    Points are added based on the result of the dice.
    The points rolled are added to the score. e.g. 3 and 4 --> 7
    If the total is an even number, the user gets an extra 10 points.
    If the total is odd, the user loses 5 points.
    If the two dices roll the same, the user gets an additional dice roll.
    The person with the highest score after 5 rounds will win.
    If the users have the same end result, the game will enter sudden death.
    Only authorised users can play the game.

    [Press enter to play]

## Authentication:

    Enter Player 1's name: Frodo
    Enter Player 2's name: Sauron
    Not accepted! Try again!

    Enter Player 1's name: Gimli
    Enter Player 2's name: Gimli
    Not accepted! Try again!

    Enter Player 1's name: Legolas
    Enter Player 2's name:
    Not accepted! Try again!

    Enter Player 1's name: Frodo
    Enter Player 2's name: Samwise
    LOG: Users Frodo and Sam are validated.

## Turn:

    Turn 1:

    David:
    Press ENTER to roll the dice!
    Your dice rolls were 6 and 2
    These sum to 8 points!
    EVEN NUMBER! You gain 10 points.
    Your total score is 18.

    Gandalf:
    Press ENTER to roll the dice!
    Your dice rolls were 6 and 1
    These sum to 7 points!
    ODD NUMBER! You lose 5 points.
    Your total score is 2.

    David had a score of 18 points.
    Gandalf had a score of 2 points.

## Doubles:

    Turn 5:

    David:
    ...

    Gandalf:
    Press ENTER to roll the dice!
    DOUBLES! Your dice rolls were 6, 6 and 4.
    These sum to 16 points!
    EVEN! You gain 10 points.
    Your total score is 32.

    David had a score of 6 points.
    Gandalf had a score of 32 points.

## Game Finished:

    David had a score of 6 points.
    Gandalf had a score of 32 points.

    Gandalf wins!

## Sudden Death:

    Corey had a score of 34 points.
    Frodo had a score of 34 points.
    It's a draw! Starting sudden death...

    Corey:
    Press ENTER to roll the dice!
    Your dice rolls were 4 and 5
    These sum to 9 points!
    ODD NUMBER! You lose 5 points.
    Your total score is 38.

    Frodo:
    Press ENTER to roll the dice!
    Your dice rolls were 1 and 4
    These sum to 5 points!
    ODD NUMBER! You lose 5 points.
    Your total score is 34.

    Corey wins!

## Display Scoreboard:

    Top 5 Scores:
    074 - Corey
    070 - Legolas
    066 - Corey
    060 - Frodo
    060 - Frodo

## Play Again (no):

    Do you want to play again? [y/n] n

    Game over!

## Play Again (yes):

    Do you want to play again? [y/n] yes

    Enter Player 1's name: Merry
    Enter Player 2's name: Pippin
    LOG: Users Merry and Pippin are validated.

---

## Files:

### scoreboard.txt

    074 - Corey
    070 - Legolas
    066 - Corey
    060 - Frodo
    060 - Frodo

### usernames.txt

    Corey
    David
    Frodo
    Samwise
    Gandalf
    Aragorn
    Legolas
    Gimli
    Pippin
    Merry
    Boromir

---

## PIOs:

**Problems, Incidents, Oppurtunities**

**resolved** Will currently accept partial names as valid because it is checking if "name in name_list" not if "name is equal to name_list(idx)"

    Enter Player 1's name: gand
    Enter Player 2's name: sam
    LOG: Users Gand and Sam are validated.
    ["Gand" is in "Gandalf" and "Sam" is in "Samwise"]

or even more severely

    Enter Player 1's name: a
    Enter Player 2's name: b
    LOG: Users A and B are validated.
    ["a" is in "Gandalf" and "b" is in "Boromir"]

I believe this mildly invalidates the validation system.

```
if self.name in names:
    return True
else: return False
```

To fix this I could iterate through each value of the name list and check for equality.

```
def authenticate(self):
    # Opens the username text file and checks whether the inputted names are in the file
    with open("usernames.txt") as accepted_names:
        names = accepted_names.readlines()
        for name in list(names):
            if name.rstrip() == self.name:
                return True
        return False
```

Opens "usernames.txt" in read only mode, reads each line of the file, iterates through each lines. For each valid name in the list, check if valid name is equal to the inputted name. If it is return True. If after all the valid names have been checked against no match is found then return False.

---

## Testing:

Import the relevant functions from project.py
```
from project import compare_dice, sum_dice, validate, check_if_negative
from project import roll_dice # needed by compare dice
```
Test that compare_dice() is summing correctly and is correctly detecting doubles
```
def test_compare_dice():
    assert compare_dice(1,2) == 3 # min 2 dice
    assert compare_dice(5,6) == 11 # max 2 dice
    for i in range(100): # due to randomness i have added a for loop to maximise the chance of finding an error
        assert 2 < compare_dice(1,1) <= 8
        assert 12 < compare_dice(6,6) <= 18
```
Tests that sum_dice() is summing correctly for scenarios involving two or three dice
```
def test_sum_dice():
    assert sum_dice(1,2) == 3 # min 2 dice
    assert sum_dice(6,5) == 11 # max 2 dice
    assert sum_dice(1,6) == 7 # valid extremes
    assert sum_dice(1,1,1) == 5 # min doubles
    assert sum_dice(6,6,6) == 18 # max doubles
```
Tests that the validation system is allowing authenticated users and blocking unauthenticated users or maliciously inputted values.
```
def test_validate():
    assert validate("Frodo","Sam") == True # Check valid names
    assert validate("Aragorn","Sauron") == False # Pos 2 invalid
    assert validate("Sauruman","Gandalf") == False # Pos 1 invalid
    assert validate("Shelob","Gollum") == False # Both invalid
    assert validate("Samwise","Frodo Baggins") == False # Frodo, not Frodo Baggins
    assert validate("","Frodo") == False # Empty name
    assert validate("Gimli","Gimli") == False # Double name
    assert validate("Sam","Gandalf") == False # Samwise, not Sam
    assert validate("a","b") == False # To prove I fixed the "in" instead of quality bug
```
Tests that the script correctly identifies negative values for the turn_score
```
def test_check_if_negative():
    assert check_if_negative(0) == 0 # zero
    assert check_if_negative(2) == 2 # min 2 dice
    assert check_if_negative(3) == 3 # min 3 dice
    assert check_if_negative(22) == 22 # max 2 dice
    assert check_if_negative(28) == 28 # max 3 dice
    assert check_if_negative(-2) == 0 # negative
    assert check_if_negative(-9999) == 0 # extreme negative
```
### Test Output:

        ====================================================================================================================================================================================================== test session starts =======================================================================================================================================================================================================
    platform linux -- Python 3.10.7, pytest-7.2.0, pluggy-1.0.0
    rootdir: /workspaces/16747709/Week9/project
    collected 4 items

    test_project.py ....                                                                                                                                                                                                                                                                                                                                                                                                       [100%]

    ======================================================================================================================================================================================================= 4 passed in 0.03s ========================================================================================================================================================================================================

---

**check_if_negative()** called from even_odd() (Manually tested as even_odd() takes in a Player class as a parameter which cannot be given to Pytest)

    Frodo:
    Press ENTER to roll the dice!
    Your dice rolls were 1 and 2
    These sum to 3 points!
    ODD NUMBER! You lose 5 points.
    Your score for this turn has been reset to 0!
    Your score for this turn is 0.
    Your total score is 20.

### lines.py

    Week6/lines/ $ python lines.py ../../Week9/project/project.py
    Lines: 194
    Comments and Whitespace: 145
    Total: 339

---

gimli quotes

> and my axe
>
> nobody tosses a dwarf
>
> i have the eyes of a hawk and the ears of a fox
>
> don't tell the elf
>
> he was twitching because he's got my axe embedded in his nervous system
>
> it's the dwarves that go swimming with little hairy women
>
> certainty of death? small chance of success? what are we waiting for
>
> aye i could do that

---

# The End
