"""
    CS 5001
    Fall 2021
    Homework 2 Starter Code

    Measurement conversions from/to Imperial and Metric
    Includes functions to covert pounds <-> kg and inches <-> kg
    
    Author: Keith
"""


INCHES_TO_CM = 2.54
POUNDS_TO_KG = 0.453592


def inches_to_cm( inches ):
    '''
    Function -- inches_to_cm
        Converts inches to centimeters and returns (answers) the resulting
        value
    Parameters:
        inches (float) -- the original distance/height in inches
    Returns a float value representing the original vaule converted
        to centimeters
    '''

    return abs(inches * INCHES_TO_CM) # convert negative distance to positive

def cm_to_inches( centimeters ):
    '''
    Function -- cm_to_inches
        Converts centimeters to inches and returns (answers) the resulting
        value
    Parameters:
        centimeters (float) -- the original distance/height in centimeters
    Returns a float value representing the original vaule converted
        to inches
    '''

    return abs(centimeters * (1 / INCHES_TO_CM))

def pounds_to_kg( pounds ):
    '''
    Function -- pounds_to_kg
        Converts pounds to kilograms and returns (answers) the resulting
        value
    Parameters:
        pounds (float) -- the original weight in pounds
    Returns a float value representing the original vaule converted
        to kilograms
    '''

    return abs(pounds * POUNDS_TO_KG) # convert negative weight to positive

def kg_to_pounds( kg ):
    '''
    Function -- cm_to_inches
        Converts kilograms to pounds and returns (answers) the resulting
        value
    Parameters:
        centimeters (float) -- the original weight in kilograms
    Returns a float value representing the original vaule converted
        to pounds
    '''

    return abs(kg * (1 / POUNDS_TO_KG))
