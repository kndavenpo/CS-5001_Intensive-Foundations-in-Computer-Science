'''
    CS5001
    Spring 2022
    Homework 2 - Programming #1: Test Measurements
    Katie Davenport

    This program tests four functions in the measurement_conversions.py file
    that convert to and from Imperial and Metric:
    pounds <-> kilograms and inches <-> centimeters

    Returns output of functions and expected results for several test cases.
'''

from measurement_conversions import inches_to_cm
from measurement_conversions import cm_to_inches
from measurement_conversions import pounds_to_kg
from measurement_conversions import kg_to_pounds

def test_inches_to_cm ( inches, expected ):
    '''
    Function -- test_inches_to_cm                             
        Tests the inches_to_cm function.
    Parameters:
        inches (float) -- the original distance / height in inches. 
        expected (float) -- the expected distance / height in inches. 
    Returns float values representing the result or output of the function
        and the expected result.  
    '''
    
    result = inches_to_cm( inches )
    print(f'Converting {inches} inches to centimeters: ')
    print(f'>> result = {result:.2f}  expected = {expected:.2f}\n')  

def test_cm_to_inches ( centimeters, expected ):
    '''
    Function -- test_cm_to_inches                             
        Tests the cm_to_inches function.
    Parameters:
        centimeters (float) -- the original distance / height in centimeters. 
        expected (float) -- the expected distance / height in centimeters. 
    Returns float values representing the result or output of the function
        and the expected result.  
    '''
    
    result = cm_to_inches( centimeters )
    print(f'Converting {centimeters} centimeters to inches: ')
    print(f'>> result = {result:.2f}  expected = {expected:.2f}\n') 

def test_pounds_to_kg ( pounds, expected ):
    '''
    Function -- test_pounds_to_kg                             
        Tests the pounds_to_kg function.
    Parameters:
        pounds (float) -- the original weight in pounds. 
        expected (float) -- the expected weight in pounds. 
    Returns float values representing the result or output of the function
        and the expected result.
    '''
    
    result = pounds_to_kg( pounds )
    print(f'Converting {pounds} pounds to kilograms: ')
    print(f'>> result = {result:.2f}  expected = {expected:.2f}\n') 

def test_kg_to_pounds ( kg, expected ):
    '''
    Function -- test_kg_to_pounds                             
        Tests the kg_to_pounds function.
    Parameters:
        kg (float) -- the original weight in kilograms. 
        expected (float) -- the expected weight in kilograms. 
    Returns float values representing the result or output of the function
        and the expected result.
    '''
    
    result = kg_to_pounds( kg )
    print(f'Converting {kg} kilograms to pounds: ')
    print(f'>> result = {result:.2f}  expected = {expected:.2f}\n') 


def main():

    # Test cases for inches to centimeters conversion function.
    print(f'*** Testing inches --> cm conversions\n')
    test_inches_to_cm (0.00, 0.00)
    test_inches_to_cm (10.00, 25.40)
    test_inches_to_cm (7.51, 19.08)
    test_inches_to_cm (-2.47, 6.27)

    # Test cases for centimeters to inches conversion function.
    print(f'\n*** Testing cm --> inches conversions\n')
    test_cm_to_inches (0.00, 0.00)
    test_cm_to_inches (10.00, 264.55)
    test_cm_to_inches (7.51, 122.62)
    test_cm_to_inches (-2.47, 22.05)

    # Test cases for pounds to kilograms conversion function.
    print(f'\n*** Testing pounds --> kg conversions\n')
    test_pounds_to_kg (0.00, 0.00)
    test_pounds_to_kg (120.00, 54.43)    
    test_pounds_to_kg (55.62, 25.23)
    test_pounds_to_kg (-10.00, 4.54)

    # Test cases for kilograms to pounds conversion function.
    print(f'\n*** Testing kg --> pound conversions')
    test_kg_to_pounds (0.00, 0.00)
    test_kg_to_pounds (120.00, 264.55)    
    test_kg_to_pounds (55.62, 122.62)
    test_kg_to_pounds (-10.00, 22.05)
        
if __name__ == "__main__":
    main()
