'''
    CS5001
    Spring 2022
    Homework 3
    Programming #2: What Color is That Square?
    Determines the color of the a chessboard square.
'''

def black_or_white(row, column):
    '''
    Function: black_or_white 
    Parameters:
        row (int): the row of the chessboard 
        column (string): the column of the chessboard 
    Return: The string "BLACK" or "WHITE" to identify the color of the square. 
    Does: Deterimines the color of the square based on its coordinates.
    '''     
    
    # Convert the column string to its unicode equivalent integer:
    # Both capital and lowercase a, c, e, and g are odd
    # Both capital and lowercase b, d, f, and h are even
    column_int = ord(column)

    # Determine if the column's integer equivalent is even or odd
    column_mod_2 = column_int % 2

    # Cast row to int
    row = int(row)

    # Determine if the row is even or odd
    row_mod_2 = row % 2

    # If the row and column are both odd or both even then "BLACK" else "WHITE"
    if row_mod_2 == column_mod_2:
        return('BLACK') 
    else:
        return('WHITE')
