from project import compare_dice, sum_dice, validate, check_if_negative
from project import pregame_checks, roll_dice

# pytest test_project.py
pregame_checks() # creates the username and scoreboard files needed

def test_compare_dice():
    assert compare_dice(1,2) == 3 # min 2 dice
    assert compare_dice(5,6) == 11 # max 2 dice

def test_compare_dice_loop():
    for i in range(100):
        assert 2 <= compare_dice(roll_dice(),roll_dice()) <= 18

def test_sum_dice():
    assert sum_dice(1,2) == 3 # min 2 dice
    assert sum_dice(6,5) == 11 # max 2 dice
    assert sum_dice(1,6) == 7 # largest range 2 dice
    assert sum_dice(1,1,1) == 5 # min 3 dice
    assert sum_dice(2,2,4) == 8 # different values for dice_3
    assert sum_dice(6,6,6) == 18 # max 3 dice

def test_sum_dice_loop():
    for i in range(100):
        assert 2 <= sum_dice(roll_dice(), roll_dice()) <= 12
        assert 2 <= sum_dice(roll_dice(), roll_dice(), roll_dice()) <= 18

def test_validate():
    assert validate("Frodo","Samwise") == True # test valid names
    assert validate("Aragorn","Sauron") == False # test invalid pos 2
    assert validate("Sauruman","Gandalf") == False # test invalid pos 1
    assert validate("Shelob","Gollum") == False # test invalid pos 1 and 2
    assert validate("Samwise-Gamgee","Frodo Baggins") == False # test extra text
    assert validate("","Frodo") == False # test missing values
    assert validate("Gimli","Gimli") == False # test duplicate names
    assert validate("Sam","Gandalf") == False # test missing text (samwise)
    assert validate("a","b") == False # check single chars "in" names

def test_check_if_negative():
    assert check_if_negative(0) == 0
    assert check_if_negative(2) == 2 # min 2 dice
    assert check_if_negative(3) == 3 # min 3 dice
    assert check_if_negative(22) == 22 # max 2 dice
    assert check_if_negative(28) == 28 # max 3 dice
    assert check_if_negative(-2) == 0 # negative
    assert check_if_negative(-9999) == 0 # extreme negative

