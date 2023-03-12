'''
    CS5001
    Spring 2022
    Homework 2 - Programming #3: Align Draw
    Katie Davenport

    Includes several Turtle functions required for this assignement: create a
    Turtle window, draw a square, draw a circle, clear the screen, run program
    as specified in the assignment with input from user to define where to
    draw a second square and circle.     
'''

# Import required for turtle libraries.
from turtle import *    # Includes window functions.
import turtle           # Includes turtle functions.

def create_window(screen, height, width, picname):
    '''
    Function -- create_window
        Creates a Turtle window with a specified size and background.
    Parameters:
        screen -- a Turtle graphics window.
        height (float) -- the height of the screen in pixels. 
        width (float) -- the width of the screen in pixels. 
        picname -- a background image.   
    Returns a Turtle window.
    '''
    
    screen.screensize(height, width) # Set screen size. 
    screen.bgpic(picname) # Set background image. 

def draw_square(turtle, color, length, x, y):
    '''
    Function -- draw_square
        Draws a square in the Turtle window with a specified color, length, and
        center location coordinates.
    Parameters:
        turtle -- a Turtle object that draws a shape on the screen.
        color -- a fill color for the square. 
        length (float) -- the length of the square in pixels. 
        x (int) -- the x-coordinate to start drawing the square. 
        y (int) -- the y-coordinate to start drawing the square.
    Returns a square on the screen.
    '''

    # Adjust the x and y coordinates from start location to center location.
    x_adjustment = -(length / 2)
    y_adjustment = (length / 2)

    # Draw the square.
    turtle.hideturtle()
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x + x_adjustment, y + y_adjustment)
    turtle.begin_fill()
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.end_fill()
    turtle.pendown()

def draw_circle(turtle, color, length, x, y):
    '''
    Function -- draw_circle
        Draws a circle in the Turtle window with a specified color, length, and
        center location coordinates.
    Parameters:
        turtle -- a Turtle object that draws a shape on the screen.
        color -- a fill color for the circle. 
        length (float) -- the length (diameter) of the circle in pixels. 
        x (int) -- the x-coordinate to start drawing the circle. 
        y (int) -- the y-coordinate to start drawing the circle.
    Returns a circle on the screen.
    '''

    # Adjust the y coordinate from start location to center location.
    y_adjustment = - (length / 2)

    # Define the radius.
    radius = length / 2

    # Draw the circle.
    turtle.penup() 
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, (y + y_adjustment))
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.pendown()

def clear_turtle(turtle):
    '''
    Function -- clear_circle
        Erase existing objects on the Turtle screen.
    Parameters:
        turtle -- a Turtle object that draws a shape on the screen.
    Returns a blank Turtle screen.
    '''
    
    turtle.clear()
    
 
def run_program():
    '''
    Function -- run_program
        Executes program as specified in the assignment using the functions
        defined in this file.
    Returns a circle and square in center locations input by a user.
    '''

    # Define constants for the screen. 
    PICNAME = 'shape_window.png'
    HEIGHT = 635
    WIDTH = 970

    # Define constants for the shapes.
    LENGTH = 80
    SQUARE_COLOR = 'DarkOliveGreen3'
    CIRCLE_COLOR = 'DeepPink'

    # Create the screen. 
    screen = Screen()
    create_window(screen, HEIGHT, WIDTH, PICNAME)

    # Set the parameters to draw the first square and circle.   
    first_shapes = turtle.Turtle()
    x = 0
    y = 0

    # Draw the first square and circle.
    draw_square(first_shapes, SQUARE_COLOR, LENGTH, x, y)
    draw_circle(first_shapes, CIRCLE_COLOR, LENGTH, x, y)

    # Input coordinates for the center of the second square and circle.     
    x_square = int(input('Please provide an x-coordinate for the square: '))
    y_square = int(input('Please provide a y-coordinate for the square: '))
    x_circle = int(input('Please provide an x-coordinate for the circle: '))
    y_circle = int(input('Please provide a y-coordinate for the circle: '))    

    # Erase the first square and circle. 
    clear_turtle(first_shapes)

    # Draw the second square and circle.
    second_shapes = turtle.Turtle()
    draw_square(second_shapes, SQUARE_COLOR, LENGTH, x_square, y_square)
    draw_circle(second_shapes, CIRCLE_COLOR, LENGTH, x_circle, y_circle)
