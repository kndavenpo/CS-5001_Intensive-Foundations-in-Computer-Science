'''
    CS5001
    Spring 2022
    Homework 2 - Programming #2: BMI
    Katie Davenport

    This program defines functions to calculate BMI and Imperial BMI.
'''

# Import required conversion functions.
from measurement_conversions import inches_to_cm, pounds_to_kg

def bmi( height, weight ):
    '''
    Function -- bmi
        Takes as input height and weight in cm and kg and returns
        the BMI value
    Parameters:
        height (in cm)
        weight (in kg)
    Returns a float value representing the calculated bmi
    '''

    # Define constant.
    METERS_PER_CM = 0.01 

    # Convert weight from centimeters to meters.
    height_meters = height * METERS_PER_CM

    # Calculate and return bmi.
    bmi = float(weight / (height_meters * height_meters))
    return bmi

def imperial_bmi( height, weight):
    '''
    Function -- imperial_bmi
        Takes as input height in inches and weight in pounds &
        returns the BMI value
    Parameters:
        height (in inches)
        weight (in pounds)
    Returns a float value representing the calculated bmi
    '''

    # Convert height and weight to centimeters and kilograms. 
    height = inches_to_cm(height)
    weight = pounds_to_kg(weight)

    # Calculate and return Imperial BMI.
    imperial_bmi = bmi( height, weight )
    return imperial_bmi

def main():

    # Input height and weight from User.
    height_metric = float(input('What is your height in centimeters? ')) 
    weight_metric = float(input('What is your weight in kilograms? ')) 
    height_imperial = float(input('What is your height in inches? ')) 
    weight_imperial = float(input('What is your weight in pounds? ')) 

    # Calculate user's BMI and Imperial BMI.
    user_bmi = bmi(height_metric, weight_metric)
    user_imperial_bmi = imperial_bmi(height_imperial, weight_imperial)

    # Output User's BMI and Imperial BMI.
    print(f'Your bmi is: {user_bmi:.3f}')
    print(f'Your imperial bmi is: {user_imperial_bmi:.3f}')

if __name__ == "__main__":
    main()
