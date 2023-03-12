'''
    CS5001
    Spring 2022
    Homework 3
    Programming #1: Shaper Clicker 
    Write the code to erase and draw circle based on screen clicks. 
'''

# Import required libraries
from turtle import *    
import turtle
import PositionService

# Set global variable for turtle
_pen = turtle.Turtle()

# Set constant for screen settings and circle  
PICNAME = 'shape_window.png'
HEIGHT = 635
WIDTH = 970
RADIUS = 80
COLOR = 'Green'

def draw_circle(x, y):
    '''
    Function: draw_circle
    Parameters:
        x (int) - the x-coordinate for the center of the circle 
        y (int) - the y-coordinate for the center of the circle
    Returns: None
    Does: Draws the circle
    '''
    
    global _pen

    # Adjust the y coordinate from start to center location
    y_adjusted = y - RADIUS

    # Draw circle 
    _pen.penup()
    _pen.color(COLOR)
    _pen.goto(x, y_adjusted)
    _pen.pendown() 
    _pen.circle(RADIUS)
    _pen.penup()

def erase_or_draw_circle(x, y):
    '''
    Function: erase_or_draw_circle 
    Parameters:
        x (float): x-coordinate of click 
        y (float): y-coordinate of click 
    Returns: None
    Does: Erases the circle if the click is with the square area. Draws a new
    circle at the location of the click if there is no square on the screen.
    '''
    global _pen

    # Get the x and y position of the circle
    x_circle = PositionService.get_position_x()
    y_circle = PositionService.get_position_y()

    # Define the boundary of the square with the inscribed circle 
    circle_left = x_circle - RADIUS 
    circle_right = x_circle + RADIUS
    circle_bottom = y_circle - RADIUS 
    circle_top = y_circle + RADIUS

    # Define the logic to erase or draw the circle 
    if PositionService.is_visible() == True \
       and (x >= circle_left and  x <= circle_right and y >= circle_bottom and
            y <= circle_top):
        _pen.clear()
        PositionService.set_visible(False)

    elif PositionService.is_visible() == False:
        draw_circle(x, y) 
        PositionService.set_position_x( x )
        PositionService.set_position_y( y ) 
        PositionService.set_visible(True)
                                
def main():
    # Create the screen
    screen = Screen()
    screen.screensize(HEIGHT, WIDTH)  
    screen.bgpic(PICNAME) 

    # Draw the initial circle and set to visible
    draw_circle(0, 0)
    PositionService.set_visible(True)

    # Erase or draw circle at the click location
    screen.onclick(erase_or_draw_circle)
    
if __name__ == "__main__":
    main() 
