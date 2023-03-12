"""
    CS5001
    Spring 2022
    The Game: MasterMind
    Katie Davenport

    This file contains helper functions related to opening and reading files
    and for logging Input/Output (IO) errors for the MasterMind game program.
"""

# Import classes and Python modules 
from Gameboard import Gameboard
import datetime

# Import constants 
from constants import *


def save_score(score):
    """
    Function: save_score -- Creates a text file to record wins if none exists.
        Appends new scores to the file when a player wins. Calls the log_error
        function when there is an I/O error. 
    Parameters:
        score (str) -- the score and player name  
    Returns: None 
    """  
     
    try:
        with open(SCORE_FILE, "a") as output_file:
            output_file.write(score + "\n")
    except IOError:
        error = "A file error occurred when writing scores to leaderboard.txt" 
        log_error(error)


def load_scores():
    """
    Function: load_scores -- Extracts score data from leaderboard.txt and
        appends each score to a list. Calls the log_error function when there
        is an I/O error. An error will be logged when the program is opened
        since leaderboard.txt is not created until a player's first win. 
    Parameters: None
    Returns: scores (list) -- a list containing score data
    """

    scores = []
    try:
        with open(SCORE_FILE, "r") as leader_file:
            for each in leader_file:
                scores.append(each)
    except IOError:
        Gameboard().add_image(POPUP_FILES[3], hide_image = True)
        error = "Could not open leaderboard.txt. Note that a file is generated\
 only after the player's first win."
        log_error(error)

    return scores


def test_images_exists():
    """
    Function: test_images_exist -- reads in the image files used in the program
        and calls the log_error function if they do not exist. The purpose of
        this function is to add an entry to the mastermind_errors.err file if
        an image file is missing. 
    Parameter: None
    Returns: None
    """
    
    print("Loading game images ...\n")

    for each in IMAGE_FILES: 
        try:
            with open(each, "r") as image:
                print(each + " loaded")
        except IOError:
            Gameboard().add_image(POPUP_FILES[3], hide_image = True)
            error = each + " does not exist"    
            log_error(error)


def log_error(error):
    """
    Function: log_errors -- Creates the mastermind_errors.err file to record
        I/O errors when the first error occurs and appends additional errors
        to the file. Also adds the date and time to each error. 
    Parameters: error (str) -- a description of the error
    Returns: None
    """  

    error_type = error
    error_time = str(datetime.datetime.now())
    error_message = error_type + " -- Error logged at: " + error_time + "\n"

    try:
        with open(ERROR_FILE, "a") as output_file:
            output_file.write(error_message)
    except IOError:
        error = 'IOError - log_errors function'
        log_error(error)
