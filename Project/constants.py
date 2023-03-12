"""
    CS5001
    Spring 2022
    The Game: MasterMind
    Katie Davenport

    This file includes all constants used in the MasterMind game. 
"""

# Screen and board configurations
WINDOW_WIDTH = 0.5
WINDOW_HEIGHT = 0.9
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 800

POSITION_PLAY_BOX = [-350, -290]  
POSITION_GUESS_BOX = [-350, 375]        
POSITION_LEADER_BOX = [70, 375]       

DIMENSIONS_PLAY = [700, 85]     
DIMENSIONS_GUESS = [400, 650]              
DIMENSIONS_LEADER = [280, 650]        

# Play area configurations
RADIUS = 15
BUTTON_X = -300 
BUTTON_Y = -345
X_INCREMENT = 40
COLORS = ["red", "yellow", "green", "blue", "purple", "black"]
BLANK = "white"
IMAGE_X = [10, 80, 250]
IMAGE_Y = -330
IMAGE_RADII = [30, 30, 50]
IMAGES = ["checkbutton.gif", "xbutton.gif", "quit.gif"]

# Guess area configurations
GUESSES = 10     
GUESS_X = -260
GUESS_Y = 310
PEG_X1 = -50
PEG_X2 = -30
PEG_Y_OFFSET = 20
PEG_RADIUS = 6
ROW_SPACER = 60
COLUMN_SPACER = 40
BULL_COLOR = "black"
COW_COLOR = "red"
POINTER_IMAGE = "arrow.gif"
POINTER_X = -310
POINTER_Y = 325     

# Leaderboard configurations
TEXT_COLOR = "blue"
TEXT_FONT = "Arial"
TEXT_JUSTIFY = "left" 
HEADER_POSITION = [100, 330]
HEADER_TEXT = "Leaders:"
HEADER_SIZE = 16
HEADER_STYLE = "underline"
SPACE = 40
BODY_SIZE = 14
BODY_STYLE = "normal"
SCORE_FILE = "leaderboard.txt"
DEFAULT_SCORES = ["8: Steve", "6: Helen"]
ERROR_FILE = "mastermind_errors.err"

# Popups
POPUP_FILES = ["quitmsg.gif", "winner.gif", "Lose.gif", \
               "leaderboard_error.gif"]
DEFAULT_X = 0
DEFAULT_Y = 0

# Basic game information
CODE_LENGTH = 4
MAIN_MENU_CHOICES = ["C", "X", "Q"] 

# Testing and error handling
VALUES = True
IMAGE_FILES = ["arrow.gif", "checkbutton.gif", "leaderboard_error.gif", \
               "Lose.gif", "quit.gif", "quitmsg.gif", "winner.gif", \
               "xbutton.gif"]
