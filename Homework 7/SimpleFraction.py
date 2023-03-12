"""
    CS5001
    Spring 2022
    Homework 7: Simple Fraction 
    Katie Davenport

    This program creates a SimpleFraction class that manages rational numbers.
"""

class SimpleFraction:
    """
    Class: SimpleFraction
    Attributes: numerator, denominator, fraction
    Methods: __init__, get_numerator, get_denominator, get_fraction,
        make_reciprocal, validate, multiply, divide, __str__, __eq__
    """
    
    def __init__(self, numerator=1, denominator=1): 
        self.numerator = numerator
        self.denominator = denominator
        self.validate()
            
    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator
 
    def make_reciprocal(self):
        if self.numerator == 0:
            raise ValueError("The denominator cannot be zero.")
        else: 
            reciprocal_numerator = self.denominator 
            reciprocal_denominator = self.numerator
            return SimpleFraction(reciprocal_numerator, reciprocal_denominator)

    def validate(self):
        if type(self.numerator) != int or type(self.denominator) != int:
            raise ValueError("The numerator and denominator must be integers.") 
        elif self.denominator == 0:
            raise ZeroDivisionError("The denominator cannot be zero.")
        else:
            return True
 
    def multiply(self, other):
        if isinstance(other, SimpleFraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return SimpleFraction(new_numerator, new_denominator)
        else:
            new_numerator = self.numerator * other
            return SimpleFraction(new_numerator, self.denominator)  

    def divide(self, other):
        if isinstance(other, SimpleFraction):
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return SimpleFraction(new_numerator, new_denominator)
        else:
            if other == 0:
                raise ZeroDivisionError("The denominator cannot be zero.")
            else:
                new_denominator = self.denominator * other
                return SimpleFraction(self.numerator, new_denominator)
    
    def __str__(self):
        output = (f"{self.numerator}/{self.denominator}")
        return(output)

    def __eq__(self, other):
        if isinstance(other, SimpleFraction):
            return self.numerator / self.denominator == \
                   other.numerator / other.denominator
        return self.numerator / self.denominator == other
