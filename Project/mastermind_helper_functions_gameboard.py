"""
    CS5001
    Spring 2022
    The Game: MasterMind
    Katie Davenport

    This file contains helper functions related to creating and setting up the
    gameboard for the MasterMind game program.
"""

# Import classes 
from Marble_adjusted import Marble
from Point import Point
from Gameboard import Gameboard

# Import helper function for files -- Required for testing that images exist.
from mastermind_helper_functions_files import * 

# Import constants 
from constants import *


def create_board_structure():
    """
    Function: create_board_structure -- Creates the gameboard and adds boxes
        for the play area (bottom), guess area (top left), and leaderboard
        (top right). 
    Parameters: None
    Returns: None
    """

    Gameboard(POSITION_PLAY_BOX).draw_box(DIMENSIONS_PLAY)     
    Gameboard(POSITION_GUESS_BOX).draw_box(DIMENSIONS_GUESS)  
    Gameboard(POSITION_LEADER_BOX).draw_box(DIMENSIONS_LEADER, COLORS[3]) 


def setup_play_area():
    """
    Function: setup_play_area -- Adds the colored marbles and images to the
        play area. The marbles are the colors that the player can choose
        from and the images are intended to allow the player to confirm the
        guess, select again, or quit the game. 
    Parameters: None
    Returns: None 
    """
    
    # Add the colored marbles  
    button_x = BUTTON_X
    for i in range(len(COLORS)):
        Marble(Point(button_x, BUTTON_Y), color = COLORS[i]).draw()
        button_x += X_INCREMENT

    # Add the images
    Gameboard().add_image(IMAGES[0], IMAGE_X[0], IMAGE_Y)
    Gameboard().add_image(IMAGES[1], IMAGE_X[1], IMAGE_Y)
    Gameboard().add_image(IMAGES[2], IMAGE_X[2], IMAGE_Y)

 
def setup_guess_area():
    """
    Function: setup_guess_area -- Adds ten rows of four empty marbles to
        display a single guess and four smaller marbles to display the number
        of bulls and cows for that guess. Also adds a pointer to highlight the
        player's guess number. 
    Parameters: None
    Returns: None 
    """
    
    guess_y = GUESS_Y
    for i in range(GUESSES):
        # Marbles for each code guess 
        Marble(Point(GUESS_X, guess_y)).draw()
        Marble(Point((GUESS_X + COLUMN_SPACER), guess_y)).draw()
        Marble(Point((GUESS_X + COLUMN_SPACER * 2), guess_y)).draw()
        Marble(Point((GUESS_X + COLUMN_SPACER * 3), guess_y)).draw()

        # Pegs to display cows and bulls 
        Marble(Point(PEG_X1, guess_y + PEG_Y_OFFSET), PEG_RADIUS).draw() 
        Marble(Point(PEG_X2, guess_y + PEG_Y_OFFSET), PEG_RADIUS).draw() 
        Marble(Point(PEG_X1, guess_y), PEG_RADIUS).draw() 
        Marble(Point(PEG_X2, guess_y), PEG_RADIUS).draw() 

        guess_y -= ROW_SPACER

    # Pointer
    Gameboard().add_image(POINTER_IMAGE, POINTER_X, POINTER_Y)   


def setup_leaderboard(scores):
    """
    Function: setup_leaderboard -- Adds a header and individual scores to the
        leaderboard. 
    Parameters:
        scores (list) -- a list containing score data 
    Returns: None
    """

    # Add header text 
    Gameboard(HEADER_POSITION).add_text(HEADER_TEXT, HEADER_SIZE, HEADER_STYLE)

    # Add individual scores 
    scores.sort() # Sort scores in ascending order
    for i in range(len(scores)):
        Gameboard([HEADER_POSITION[0], (HEADER_POSITION[1] - SPACE * \
                (i + 1))]).add_text(scores[i].strip(), BODY_SIZE, BODY_STYLE)


def orchestrate_board_setup():
    """
    Function: orchestrate_board_setup -- Calls function that checks if all 
        image files are present and functions that setup the complete
        MasterMind gameboard. Ensures that at least two scores are displayed on
        the leaderboard. Uses default scores if leaderboard.txt does not exist
        or if it contains only one score. 
    Parameters: None
    Returns: None 
    """
    
    # Check that all image files are present
    test_images_exists()

    # Setup gameboard 
    create_board_structure()   
    setup_play_area() 
    setup_guess_area()

    # Add scores to leaderboard
    scores = load_scores() # Load scores from leaderboard.txt
    default_scores = DEFAULT_SCORES.copy()
    if len(scores) == 0:
        scores = default_scores 
    elif len(scores) == 1:
        scores = [scores[0], default_scores[1]] 
    setup_leaderboard(scores)
