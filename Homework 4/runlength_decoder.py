'''
    CS5001
    Spring 2022
    Homework 4
    Programming #1: Runlength Decoder 

    This group of functions decodes RLE-encoded values with the "runs"
    expanded. The file includes two helper functions: get_rle_values() and
    get_rle_run_lengths(), which extract the two different data types in an
    RLE list. The decode() function uses these two separate lists to create
    a new list in the decoded format.
'''

# Import test data.
from hw4data import DATA0, DATA1, DATA2, DATA3, DATA4, DATA5

def get_rle_values( rle_list ):
    '''
    Function: get_rle_values()  
    Parameter: a list of RLE-encoded values
    Return: a list of string values from the RLE list
    Does: Extracts the string values that are to be expanded from the list. 
    '''

    # The string values are at index positions: 0, 2, 4 ... n-1
    value_list = []
    for i in range(0, len(rle_list), 2): 
        value = rle_list[i]
        value_list.append(value)
        i += 1

    return value_list
 
def get_rle_run_lengths( rle_list ):
    '''
    Function: get_rle_values()  
    Parameter: a list of RLE-encoded values 
    Return: a list of the integer run lengths for each RLE string value 
    Does: Extracts the run lengths only from the list. 
    '''

    # The run length values are at index positions: 1, 3, 5 ... n
    run_length_list = []
    for i in range(1, len(rle_list), 2):
        run_length = rle_list[i]
        run_length_list.append(run_length)
        i += 1

    return run_length_list

def decode( rle_list ):
    '''
    Function: decode()  
    Parameter: a list of RLE-encoded values 
    Return: a list containing the decoded values with the "runs" expanded 
    Does: Decodes RLE-encoded values in a list with the "runs" expanded
    '''  

    # Get the lists of string values and run lengths 
    rle_values = get_rle_values( rle_list )
    rle_run_lengths = get_rle_run_lengths( rle_list ) 

    # Create the decoded list with the "runs" expanded
    full_list = []
    for i in range(len(rle_values)):
        value = rle_values[i]
        run_length = rle_run_lengths[i]
        for j in range(run_length):
            full_list.append(value)
        
        i += 1
        j += 1

    return full_list    
