"""
    CS5001
    Spring 2022
    The Game: MasterMind
    Katie Davenport

    This file contains the Gameboard class that is used for creating a
    gameboard for theMasterMind game.  
"""  

# Import necessary files and packages
from turtle import *    
import turtle
from Point import Point
from constants import *


class Gameboard:
    """
    Class: Gameboard 
    Attributes: self, pen, screen, x_position, y_position
    Methods: draw_box, add_text, add_image, get_player_name, __str__
    """

    def __init__(self, position = [DEFAULT_X, DEFAULT_Y]):
        """
        Constructor -- Creates a new instance of the turtle gameboard where
            turtle objects can be added at a defined location on the board.
        Parameters:
            self -- the current gameboard
            position (optional)(list) -- the x and y coordinates of the turtle    
        """
        
        self.pen = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.x_position = position[0]
        self.y_position = position[1]
        self.pen.hideturtle()
        self.pen.visible = False
        self.pen.speed(0)                       
        self.pen.up()
        self.pen.goto(self.x_position, self.y_position)


    def draw_box(self, dimensions, color = "black"):
        """
        Method -- Adds an empty box to this screen.
        Parameters:
            self -- the current gameboard screen 
            dimensions (list) -- the height and width of the box in pixels
            color (optional)(str) -- the color of the outline of the box
        Returns: None    
        """
        
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.pen.pencolor(color)
        self.pen.pensize(4)
        self.pen.down()
        self.pen.forward(self.width)
        self.pen.right(90)
        self.pen.forward(self.height)
        self.pen.right(90)
        self.pen.forward(self.width)
        self.pen.right(90)
        self.pen.forward(self.height)


    def add_text(self, text, font_size, font_style):
        """
        Method -- Adds text to this screen.
        Parameters:
            self -- the current gameboard screen 
            text (str) -- text to add to the screen 
            font_size (int) -- the size of the font 
            font_style (str) -- the style of the font (e.g. underline, normal)
        Returns: None  
        """
        
        self.text = text
        self.pen.color(TEXT_COLOR) 
        self.font = TEXT_FONT 
        self.align = TEXT_JUSTIFY 
        self.font_size = font_size
        self.font_style = font_style 
        self.style = (self.font, self.font_size, self.font_style)
        self.pen.write(self.text, True, self.align, font = self.style)


    def add_image(self, image, image_x = DEFAULT_X, image_y = DEFAULT_Y, \
                  hide_image = False):
        """
        Method -- Adds an image to this screen.
        Parameters:
            self -- the current gameboard screen 
            image (str) -- the name of the image file 
            image_x (optional)(int) -- the x-coordinate where the image appears
            image_y (optional)(int) -- the y-coordinate where the image appears
            hide_image (optional)(bool) -- hides the image after adding it 
        Returns: None   
        """
        
        self.image = image
        self.image_x = image_x
        self.image_y = image_y
        self.turtle = turtle.Turtle()
        self.screen.addshape(self.image)
        self.turtle.visible = False
        self.turtle.up()
        self.turtle.goto(self.image_x, self.image_y)
        self.turtle.shape(self.image)
        if hide_image == True:
            self.turtle.hideturtle()

            
    def get_player_name(self):
        """
        Method -- Launches a pop-up for the player to enter their name.
        Parameters:
            self -- the current gameboard screen  
        Returns:
            name (str) -- the name entered by the player    
        """

        name = self.screen.textinput("MasterMind", "Your Name: ")
        return name


    def __str__(self):
        """
        Method -- returns a string that represents this gameboard screen
        Parameters:
            self -- the current gameboard screen
        Returns:
            output (str) -- string to define this object
        """
        
        output = "Turtle screen for MasterMind"
        return output    
