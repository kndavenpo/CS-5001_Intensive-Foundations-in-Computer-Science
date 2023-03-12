'''
    Intro to classes and objects 
    
'''
class Square:
    def __init__(self, width): #constructor method
        self.width = width

    def get_area(self):
        return self.width ** 2

    def get_perimeter(self):
        return self.width * 4

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width
    

    def __str__(self):
        return "Area of square with width " + str(self.width)
        



