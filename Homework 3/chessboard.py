'''
    CS5001
    Spring 2022
    Homework 3
    Programming #2: What Color is That Square?
    Determines if the row or column are valid or not for a standard chessboard.
'''

def check_valid_row( row ):
    '''
    Function: check_valid_row 
    Parameter: row (integer or string) - Row of a chessboard  
    Return: A boolean value 
    Does: Determines if the row that is passed is a valid value.
    '''    

    row = int( row )

    if (row >= 1 and row <= 8):
        row_valid = True
    else:
        row_valid = False

    return row_valid 


def check_valid_column( column ):
    '''
    Function: check_valid_column 
    Parameter: column (string) - Column of a chessboard
    Return: A boolean value - True if valid, False if invalid
    Does: Deterimines if the column that is passed is a valid value.
    ''' 
    column = str(column)

    if (ord(column) >= 97 and ord(column) <= 104) or \
       (ord(column) >= 65 and ord(column) <= 72):
        column_valid = True      
    else:
        column_valid = False

    return column_valid     
