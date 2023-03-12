"""
    CS5001
    Spring 2022
    The Game: MasterMind
    Katie Davenport

    This file contains the Marble class. It uses the Marble class provided
    in the starter file with a few minor adjustments - the default color is
    set to BLANK (white) and constants are imported from constants.py. 
"""  

import turtle
from Point import Point
from constants import *

class Marble:
    def __init__(self, position, size = RADIUS, color = BLANK):
        self.pen = self.new_pen()
        self.position = position
        self.color = color
        self.visible = False
        self.is_empty = True
        self.pen.hideturtle()
        self.size = size
        self.pen.speed(0)  # Set to fastest drawing

    def new_pen(self): 
        return turtle.Turtle()

    def new_screen(self):
        return turtle.Screen()

    def set_color(self, color):
        self.color = color
        self.is_empty = False

    def get_color(self):
        return self.color

    def get_name(self):
        return self.name

    def draw(self):
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = False
        self.pen.down()
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.pen.circle(self.size)
        self.pen.end_fill()

    def draw_empty(self):
        self.erase()
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = True
        self.pen.down()
        self.pen.circle(self.size)
        
    def erase(self):
        self.visible = False
        self.pen.clear()

    def clicked_in_region(self, x, y):
        if abs(x - self.position.x) <= self.size * 2 and \
           abs(y - self.position.y) <= self.size * 2:
            return True
        return False
