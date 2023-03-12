'''
CS5001
Spring 2022
Homework 1 - Program 1: Bottles
Katie Davenport

This program computes the refund for containers.
Containers can either be one liter or less or greater than one liter. 
'''

def main():

    # Define constants.
    DEPOSIT_1_LITER_OR_LESS = 0.10
    DEPOSIT_MORE_THAN_1_LITER = 0.25

    # Input the number of containers one liter or less.
    containers_1_liter_or_less = \
        int(input('How many containers that are 1 liter or less? '))   

    # Input the number of containers more than one liter.
    containers_more_than_1_liter = \
        int(input('How many containers that are more than 1 liter? '))

    # Calculate refund.
    refund = (containers_1_liter_or_less * DEPOSIT_1_LITER_OR_LESS) +\
             (containers_more_than_1_liter * DEPOSIT_MORE_THAN_1_LITER)  

    # Output refund.
    print(f'Your total refund will be ${refund:.2f}')
    
if __name__ == "__main__":
    main()  
