'''
    CS5001
    Spring 2022
    Homework 4
    Programming #3: UPC

    This group of functions determines if a UPC is valid by using the
    validation algorithm. The file includes two helper functions,
    get_upc_group_1_values() and get_upc_group_2_values(), which extracts the
    digits in the odd and even positions (left to right), respectively. The
    group 1 values are multipled by three. The is_valid_upc() function
    combines both list, sums the values, and determines if the result is a
    mutliple of ten. It also checks additional validation conditions. 
'''

def get_upc_group_1_values( list_of_integers ): 
    '''
    Function: get_upc_group_1_values()  
    Parameter: a list of integers
    Return: a list integers 
    Does: Extract values in odd index positions (R to L) and multiply by 3. 
    '''

    # Remove the last integer from the UPC list
    list_of_integers_slice = list_of_integers[:-1]

    # Create an empty list
    group_1_list = []

    # Extract odd values from the UPC list, multipy by 3, and add to new list
    for i in range((len(list_of_integers_slice) - 1), -1, -2):
        group_1_value = list_of_integers_slice[i]
        group_1_value_times_three = group_1_value * 3
        group_1_list.append(group_1_value_times_three) 
        i += 1

    return group_1_list 

def get_upc_group_2_values( list_of_integers ): 
    '''
    Function: get_upc_group_2_values()  
    Parameter: a list of integers
    Return: a list integers 
    Does: Extract values in even index positions (right to left) 
    '''

    # Create an empty list
    group_2_list = []

    # Extract even values from the UPC list and add to the new list
    for i in range((len(list_of_integers) - 1), -1, -2):
        group_2_value = list_of_integers[i]
        group_2_list.append(group_2_value) 
        i += 1

    return group_2_list

def is_valid_upc( list_of_integers ):
    '''
    Function: is_valid_upc()  
    Parameter: a list of integers 
    Return: a boolean
    Does: Indicates if list of integers is a valid upc_code 
    '''

    # Get group 1 list  
    group_1_list_times_three = get_upc_group_1_values(list_of_integers)

    # Get group 2 list 
    group_2_list = get_upc_group_2_values(list_of_integers)

    # Combine the two groups into one list 
    combined_list = group_1_list_times_three + group_2_list

    # Sum the values of the combined list 
    summed_values = sum(combined_list)

    # Check the validation algorithm to determine if the code is valid
    if len(list_of_integers) < 2:   # Condition: Must be at least 2 digits 
        is_valid_upc = False
    elif max(list_of_integers) == 0:  # Condition: All digits cannot be zero 
        is_valid_upc = False     
    elif summed_values % 10 != 0: # Condition: Sum must be divisible by 10 
        is_valid_upc = False
    else:
        is_valid_upc = True

    return is_valid_upc  
