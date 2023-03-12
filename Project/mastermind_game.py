"""
    CS5001
    Spring 2022
    The Game: MasterMind
    Katie Davenport

    This program runs a one-person version of MasterMind using a Turtle
    gameboard and a user interface for entering guesses and game actions.
    This file includes core game functions. Additional files required to
    play the game are imported. These include: classes used to create Marbles
    (empty or colored circles) and the gameboard, helper functions for handling
    files and setting up the gameboard, and contants. The Python random module
    is also imported for generating the 4-color secret code.
"""

# Import classes and Python modules 
from Marble_adjusted import Marble
from Point import Point
from Gameboard import Gameboard
import random

# Import helper functions
from mastermind_helper_functions_files import *
from mastermind_helper_functions_gameboard import *

# Import constants 
from constants import *

     
def get_player_input(): 
    """
    Function: get_player_input -- Allows players to enter a guess and select a
        game action (confirm guess, pick again, or quit). Includes print
        statements to guide player input.
    Parameters: None
    Returns: player_input (tuple) -- contains five strings that include each
        color in the player's guess plus the player's selected action
    """ 

    print("\nPick four distinct colors out of these options:\n"
          "\tred, yellow, green, blue, purple, black\n")
    color_1 = input("First color: ").lower().strip()
    color_2 = input("Second color: ").lower().strip()
    color_3 = input("Third color: ").lower().strip()
    color_4 = input("Fourth color: ").lower().strip()

    print(f"\nYour guess is: {color_1}, {color_2}, {color_3}, {color_4}") 
    print("\nWhat would you like to do?\n"
          "C: Confirm choices\n"
          "X: Pick again\n"
          "Q: Quit game\n")

    game_action = input("Your choice: ").upper()
    player_input = (color_1, color_2, color_3, color_4, game_action)
    return player_input


def generate_secret_code(): 
    """ 
    Function: generate_secret_code -- Creates a list of four distinct colors
        out of six designated game choices.
    Parameters: None
    Returns: secret_code (list) -- contains four strings - the color code
    """ 
    
    # List of six designated game colors
    color_list = COLORS.copy()

    # Generate the secret code 
    i = 0
    secret_code = []
    for i in range(CODE_LENGTH):
        max_random_index = len(color_list) - 1
        random_index = random.randint(0, max_random_index)
        color = color_list[random_index]
        secret_code.append(color)
        color_list.pop(random_index)
        i += 1

    return secret_code    

         
def count_cows_and_bulls(secret_code, guess): 
    """ 
    Function: count_cows_and_bulls() -- Counts the number of cows and bulls
        and generates a list that determines the colors of the pegs used to
        display cows and bulls with colors in the following order: black
        (bulls), red (cows), and white (neither cows nor bulls).  
    Parameters:
        secret_code (list) -- contains four strings - the secret code
        guess (list) -- contains four strings - the player's guess 
    Returns: cow_and_bull_data (tuple) -- contains: 
        cows (int) -- the number of cows
        bulls (int) -- the number of bulls 
        color_list (list) -- includes 4 strings containing a combination of
            black (bull), red (cow), or white (neither cow nor bull) in
            alphabetical order
    """ 
    
    cows = 0
    bulls = 0
    color_list = []
    for i in range(len(guess)):
        if guess[i] in secret_code and guess[i] != secret_code[i]:
            color_list.append(COW_COLOR)
            cows += 1
        if guess[i] == secret_code[i]:
            color_list.append(BULL_COLOR)
            bulls += 1

    for i in range(CODE_LENGTH - len(color_list)):
        color_list.append(BLANK)

    color_list.sort()
    cow_and_bull_data = (cows, bulls, color_list)
    
    return cow_and_bull_data


def populate_guess(secret_code, guess, guess_number):
    """ 
    Function: populate_guess -- Calls the count_cows_and_bulls function and
        uses the output to fill in marbles for both the guess and to display
        the number of bulls and cows. Also determines if the player won during
        that guess.
    Parameters:
        secret_code (list) -- contains four strings - the secret code
        guess (list) -- contains four strings - the player's guess 
        guess_number (int) -- the number of the player's guess
    Returns:
        win_tag (bool) -- indicates if the player won  
    """ 

    # Call count_cows_and_bulls function and extract inputs from tuple 
    cows_and_bulls = count_cows_and_bulls(secret_code, guess)
    cows = cows_and_bulls[0]    # number of cows
    bulls = cows_and_bulls[1]   # number of bulls
    peg_color_list = cows_and_bulls[2]  # a list containing the peg colors

    # Spacer for each new row
    row_spacer = ROW_SPACER * (guess_number - 1)

    # Marbles for the four colors in the guess 
    Marble(Point(GUESS_X, GUESS_Y - row_spacer), color = guess[0]).draw()
    Marble(Point((GUESS_X + COLUMN_SPACER), GUESS_Y - row_spacer), color = \
           guess[1]).draw()
    Marble(Point((GUESS_X + COLUMN_SPACER * 2), GUESS_Y - row_spacer), color \
           = guess[2]).draw()
    Marble(Point((GUESS_X + COLUMN_SPACER * 3), GUESS_Y - row_spacer), color \
           = guess[3]).draw()

    # Smaller marbles (pegs) to display the number of bulls and cows
    Marble(Point(PEG_X1, GUESS_Y + PEG_Y_OFFSET - row_spacer), PEG_RADIUS, \
           peg_color_list[0]).draw() 
    Marble(Point(PEG_X2, GUESS_Y + PEG_Y_OFFSET - row_spacer), PEG_RADIUS, \
           peg_color_list[1]).draw() 
    Marble(Point(PEG_X1, GUESS_Y - row_spacer), PEG_RADIUS, peg_color_list[2])\
            .draw() 
    Marble(Point(PEG_X2, GUESS_Y - row_spacer), PEG_RADIUS, peg_color_list[3])\
            .draw()

    # Create a tag to indicate if the player won on a particular guess 
    if bulls == 4:
        win_tag = True
    else:
        win_tag = False 

    return win_tag

    
def orchestrate_game():
    """ 
    Function: orchestrates_game -- Orchestrates the game. Calls functions to
        set up the board, get the player's name, and generate the secret code.
        Uses a while loop to allow the player to guess up to ten times. The
        loop collect user input, fills in marbles in the guess area, and
        determines if the player won on a particular guess. The player exits
        the loop if they win the game, lose the game, or quit. 
    Parameters: None
    Returns: None 
    """
    
    # Setup board 
    orchestrate_board_setup()
    
    # Get player's name and secret code 
    player_name = Gameboard().get_player_name() 
    secret_code = generate_secret_code()

    # Welcome message for user interface version 
    print("\n\nWelcome to Mastermind " + player_name + "!")   
 
    done = False
    guess_number = 1
    while not done:  
        player_input = get_player_input()
        guess = [player_input[0], player_input[1], player_input[2], \
                 player_input[3]]
        menu_option = player_input[4]
        if menu_option == "X":
            print("\nSelect again.")
        elif len(set(guess)) < len(guess) or guess[0] not in \
             COLORS or guess[1] not in COLORS or guess[2] not in \
             COLORS or guess[3] not in COLORS:
            print("You picked an invalid color or you picked the same color \
more than once. Pick again.\n")
        elif menu_option not in MAIN_MENU_CHOICES:
            print("Invalid menu choice. Pick again.\n")  
        elif menu_option == "C":
            win_tag = populate_guess(secret_code, guess, guess_number)
            pointer_y = POINTER_Y - ROW_SPACER * (guess_number)
            guess_number += 1
            if guess_number <= 10:
               Gameboard().add_image(POINTER_IMAGE, POINTER_X, pointer_y) 
            if win_tag == True:
                Gameboard().add_image(POPUP_FILES[1])
                score = str(guess_number - 1)
                new_score = score + ": " + player_name
                save_score(new_score)
                done = True 
            elif guess_number == 11:
                Gameboard().add_image(POPUP_FILES[2])
                done = True
        elif menu_option == "Q":
            Gameboard().add_image(POPUP_FILES[0])

     
def main():

    orchestrate_game()

if __name__ == "__main__":
    main()
