"""
    CS5001
    Spring 2022
    Project - The Game: MasterMind 
    Katie Davenport

    This program tests core game model functions in mastermind_game.py. The
    test functions print either the direct output or characteristics of the
    output along with the input of the test functions for multiple test cases
    to compare. 
"""

from mastermind_game import count_cows_and_bulls, generate_secret_code
from constants import *

def test_count_cows_and_bulls( secret_code, guess, expected ):
    """
    Function -- test_count_cows_and_bulls - Testing for the
        count_cows_and_bulls function.
    Parameters:
        secret_code (list) -- contains four strings - the secret code
        guess (list) -- contains four strings - the player's guess 
        expected (tuple) -- the expected output of the function:
            cows (int) -- the number of cows
            bulls (int) -- the number of bulls 
            color_list (list) -- includes four strings containing a combination
                of black (bull), red (cow), or white (neither cow nor bull) in
                alphabetical order
    Return: None -- inputs are printed out with the output of the
        count_cows_and_bulls function              
    """

    result = count_cows_and_bulls (secret_code, guess)
    print(f"\nTesting secret code {secret_code} with guess {guess}")
    print(f">> Result:   {result}")
    print(f">> Expected: {expected}")

def test_generate_secret_code( expected_length, expected_distinct_length,
                               expected_values):
    """
    Function -- test_generate_secret_code - Testing for the
        generate_secret_code function. There are no input parameters for
        generate_secret_code. This function will test: the length of the list
        returned, that the list contains strings that are designated game
        colors, and that no colors are repeated.
    Parameters:
        expected_length (int) -- 4
        expected_distinct_length (int) -- 4 indicating no repeats
        expected_values (boolean) -- True indicating values are game colors
    Return:  None -- inputs are printed out with corresponding characteristics
        of the list returned from the generate_secret_code function
    """

    result = generate_secret_code ()

    # Items to tuest 
    length = len(result)
    distinct_length = len(set(result))
    if result[0] in COLORS and result[1] in COLORS and result[2] in COLORS and\
       result[3] in COLORS:
        values = True
    else:
        values = False 
    
    print(f">> Result length is :               {length}")
    print(f">> Result distinct length is :      {distinct_length}")
    print(f">> Result values are game colors:   {values}")
    print("")
    print(f">> Expected length is:              {expected_length}")
    print(f">> Expected distinct length is:     {expected_distinct_length}")
    print(f">> Expected values are game colors: {expected_values}")
    
def main():
      
    # Test cases: test_count_cows_and_bulls
    print(f"*** Testing count_cows_and_bulls function:")
    secret_code = ["red", "blue", "purple", "yellow"]
    guess = ["red", "green", "blue", "purple"]
    expected = (2, 1, ["black", "red", "red", "white"])
    test_count_cows_and_bulls (secret_code, guess, expected)

    secret_code = ['blue', 'green', 'black', 'yellow']
    guess = ['red', 'purple', 'blue', 'green']
    expected = (2, 0, ['red', 'red', 'white', 'white'])
    test_count_cows_and_bulls (secret_code, guess, expected)

    secret_code = ['purple', 'yellow', 'blue', 'black']
    guess = ['yellow', 'blue', 'black', 'purple']
    expected = (4, 0, ['red', 'red', 'red', 'red'])
    test_count_cows_and_bulls (secret_code, guess, expected)

    secret_code = ['red', 'yellow', 'green', 'blue']
    guess = ['red', 'yellow', 'green', 'blue']
    expected = (0, 4, ['black', 'black', 'black', 'black'])
    test_count_cows_and_bulls (secret_code, guess, expected)

    print("")

    # Test cases: test_generate_secret_code
    print(f"\n*** Testing generate_secret_code function:")
    print("Test #1:")
    test_generate_secret_code (CODE_LENGTH, CODE_LENGTH, VALUES)

    print("\nTest #2:")
    test_generate_secret_code (CODE_LENGTH, CODE_LENGTH, VALUES)
        
if __name__ == "__main__":
    main()
