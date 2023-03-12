'''
CS5001
Spring 2022
Homework 1 - Program 3: Field of Dreams
Katie Davenport

This program calculates field size in acres based on length and width in feet.
'''

def main():

    # Define constants.
    SQUARE_FEET_PER_ACRE = 43560

    # Input the length of the field in feet from the user.
    length = float(input('Enter the length of the field in feet: '))

    # Input the width of the field in feet from the user.
    width = float(input('Enter the width of the field in feet: ')) 

    # Calculate the area of the field in acres.
    field_area = (length * width) / SQUARE_FEET_PER_ACRE
    
    # Output the area of the field in acres. 
    print(f'The area of the field is {field_area:.3f}') 
    
if __name__ == "__main__":
    main()  
