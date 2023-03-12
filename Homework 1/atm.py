'''
CS5001
Spring 2022
Homework 1 - Program 2: ATM
Katie Davenport

This program determines the number of bills to be dispensed at an ATM.
The ATM dispenses fifties, twenties, tens, fives, and ones.
The ATM must dispense the fewest number of bills that it can.

Test case #1:
Input: $537
Output: 10 fifties, 1 twenties, 1 tens, 1 fives, 2 ones

Test case #2:
Input: $109
Output: 2 fifties, 0 twenties, 0 tens, 1 fives, 4 ones

Test case #3:
Input: $46
Output: 0 fifties, 2 twenties, 0 tens, 1 fives, 1 ones  
'''

def main():

    # Define constants needed for calcs(all denominations except ones).
    FIFTY = 50
    TWENTY = 20
    TEN = 10
    FIVE = 5

    # Input the withdrawal amount.
    withdraw_amount = int(input("Welcome to PDQ Bank! Amount to withdraw? $ "))

    # Calculate the number of fifties.
    fifties = withdraw_amount // FIFTY
    
    # Calculate the number of twenties based on the remainder. 
    remainder_after_fifties = withdraw_amount - (fifties * FIFTY) 
    twenties = remainder_after_fifties // TWENTY  

    # Calculte the number of tens based on the remainder.
    remainder_after_twenties = remainder_after_fifties - (twenties * TWENTY) 
    tens = remainder_after_twenties // TEN 
    
    # Calculate the number of fives based on the remainder.
    remainder_after_tens = remainder_after_twenties - (tens * TEN) 
    fives = remainder_after_tens // FIVE  

    # Calculte the number of ones based on the remainder.
    remainder_after_fives = remainder_after_tens - (fives * FIVE) 
    ones = remainder_after_fives 

    # Output the bills to be dispensed.
    print(f"Cha-ching! You asked for $ {withdraw_amount}")
    print(f"That breaks down to:")
    print(f" {fifties} fifties")
    print(f" {twenties} twenties")
    print(f" {tens} tens")
    print(f" {fives} fives")
    print(f" {ones} ones")
        
if __name__ == "__main__":
    main()  
