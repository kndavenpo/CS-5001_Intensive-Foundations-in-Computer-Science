'''
    CS5001
    Spring 2022
    Homework 3
    Programming #2: What Color is That Square?
    Test files for check_valid_row and check_valid_column functions
'''

from chessboard import check_valid_row
from chessboard import check_valid_column

def test_check_valid_row(row, expected):
    '''
    Function: test_check_valid_row
    Params:
        row (integer or string) - Row of a chessboard
        expected (boolean) - True if valid, False if invalid
    Return: A string that displays row, actual value, and expected value
    Does: Tests to see if the input row is a valid value for a chessboard.
    '''
    
    actual = check_valid_row( row )
    return(f'Row: {row}, Expected: {expected}, Actual: {actual}')
             
def test_check_valid_column(column, expected):
    '''
    Function: test_check_valid_column
    Params:
        column (string) - Column of a chessboard
        expected (boolean) - True if valid, False if invalid
    Return: A string that displays row, actual value, and expected value
    Does: Tests to see if the input row is a valid value for a chessboard.
    '''    
    actual = check_valid_column( column )
    return(f'Row: {column}, Expected: {expected}, Actual: {actual}')

def test_squares():
    print("\nTest row values:")
    print(test_check_valid_row(5, True))
    print(test_check_valid_row('1', True))
    print(test_check_valid_row(8, True))
    print(test_check_valid_row('0', False))
    print(test_check_valid_row(10, False))
    
    print("\nTest column values:")
    print(test_check_valid_column('a', True))
    print(test_check_valid_column('F', True))
    print(test_check_valid_column('h', True))
    print(test_check_valid_column('z', False))
    print(test_check_valid_column('I', False))
    
test_squares()
