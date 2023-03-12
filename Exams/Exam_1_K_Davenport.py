'''
    CS 5001
    Exam #1
    Katie Davenport
    3/3/22
'''


# QUESTION 9
def is_leap(year):
    '''
    Function: is_leap
    Parameters: year(int) - a year
    Returns: boolean
    Does: Determines if a year is a leap year 
    '''

    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        leap_year = True
    else:
        leap_year = False

    return leap_year    
 

# QUESTION 10
def is_vowel(letter):
    '''
    Function: is_vowel
    Parameters: string - a single letter
    Returns: boolean
    Does: determines is a letter is a vowel
    '''
    
    letter = letter.upper()
    letters = ['A','E','I','O','U']


    if letter in letters:
        vowel = True
    else:
        vowel = False

    return vowel    


# QUESTION 11  
def transformer(integer_list):
    '''
    Function: transformer
    Parameter: list of integers
    Returns: list of strings
    Does: converts list of integers to list of strings 'odd' or 'even' corresponding with integer value.
    '''
    
    new_list = []
    for integer in integer_list: 
        if integer % 2 == 1:
            item = 'Odd'
            new_list.append(item)
        else:    
            item = 'Even'
            new_list.append(item)

    return new_list   



                 

# QUESTION 12
def mutate_transformer(integer_list):
    '''
    Function: mutate_transformer
    Parameter: list of non-negative integers
    Returns: nothing
    Does: converts 0 to False and all other integers to True 
    '''
    
    for i in range(len(integer_list)):
        if integer_list[i] == 0:
            integer_list[i] = False
        else:    
            integer_list[i] = True  
                 

# QUESTION 13 
def substitute(my_string):
    '''
    Function: substitute
    Parameter: a string
    Returns: a string
    Does: replaces r with w and R with W if first letter in the word.  
    '''

    my_string_split = my_string.split()
    new_string = ''
    for i in range(len(my_string_split)):
        if my_string_split[i][0] == 'r':
            new_word = 'w' + my_string_split[i][1:] + ' ' 
        elif my_string_split[i][0] == 'R':
            new_word = 'W' + my_string_split[i][1:] + ' '
        else:
            new_word = my_string_split[i] + ' ' 
        new_string =   new_string + new_word  
    return new_string        

'''
-- professor solution

    words = message.split()
    for i in range(len(words)):
        if words[i][0] == 'R'
            if words[i][0] == 'r':
                words[i] = 'w' + words[i][i::]
            else:
                words[i] = 'W' + words[i][i::]
        MISSED REST        
'''


# QUESTION 14 - 
def median(a, b, c):
    '''
    Function: median
    Parameter: three integers
    Returns: one integer 
    Does: selects the median integer   
    '''
    
    my_list = []      
    my_list.append(a)
    my_list.append(b)
    my_list.append(c)
    my_list.sort()
    return my_list[1]
