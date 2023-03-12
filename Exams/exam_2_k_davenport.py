'''
    CS 5001
    Exam #2
    Katie Davenport
    4/28/22    
'''

# Constant for Question #12
AMBIGRAM_INTEGERS = '12580'

# Constants for Question #13
MIN_BATTERY_VALUE = 50
MAX_BATTERY_VALUE = 200
MIN_CHARGE_STATE = 0.0
MAX_CHARGE_STATE = 1.0
WINTER_TRUE = 0.7
WINTER_FALSE = 1.0

# Question 7
def is_cs5001(my_string):
    """
    Name: is_cs5001 -- Indicates if "CS5001" is in the string. 
    Parameters: my_string (str) - any string
    Returns: boolean 
    """

    if 'CS5001' in my_string:
        return True
    else:           # Test if we need else 
        return False

    
# Question 8
def append(my_dict, new_key, new_value): 
    """
    Name: append -- Adds the new key/value pair to the dictionary if the key is
        not already in the dictionary. If the key is in the dictionary, do not
        modify the dictionary.
    Parameters:
        my_dict (dict)
        my_key (any legal data type) 
        value (any data type)
    Returns:
        my_dict (dict)
    """

    if new_key not in my_dict.keys():
        my_dict[new_key] = new_value

    return my_dict 
    

# Question 9
def recursive_reverse(my_string):
    """
    Name: recursive_reverse -- Reverses the string using recursion.
    Parameters: my_string (str) -- any string 
    Returns: my_string (str) -- the original string reversed
    """

    if len(my_string) == 0:
        return my_string
    elif len(my_string) == 1:
        return my_string
    else:
        reverse_string = my_string[-1] + recursive_reverse(my_string[:-1])

    return reverse_string    
        
 
# Question 10
def reverse_list_of_pairs(list_of_pairs):
    """
    Name: reverse_list_of_pairs -- reverses the order of the pairs in the
        nested lists 
    Parameters: list_of_pairs (list) -- a nested list that contains lists of
        length two (pairs)  
    Returns: list_of_pairs_swapped (list) -- a nested list that contains lists of
        length two (pairs)  
    """

    list_of_pairs_swapped = []
    for pair in list_of_pairs:
        list_of_pairs_swapped.append([pair[1], pair[0]])

    return list_of_pairs_swapped           

# Question 11
def evens(integer_list):
    """
    Name: integer_list -- Returns a list of the even integers in the Parameter
        list. 
    Parameters: integer_list (list) -- a list of integers
    Returns: list_of_evens (evens) -- a list of even integers 
    """

    list_of_evens = []
    for integer in integer_list:
        if integer % 2 == 0:
            list_of_evens.append(integer) 

    return list_of_evens   

# Question 12
def check_ambigram(my_int_str):
    """
    Name: ambigram_check -- Determines if a sting of integers is an ambigram. 
    Parameters:  my_int_str(str) -- a string of non-negative integers
    Returns: boolean
    """    

    digit_check = 0 
    for integer in my_int_str:
        if integer in AMBIGRAM_INTEGERS:
            digit_check += 1
        
    return digit_check == len(my_int_str) 

def check_palindrome(my_int_str):
    """
    Name: palindrome_check -- Determines if a string of integers is a
        palindrome. 
    Parameters:  my_int_str(str) -- a string of non-negative integers
    Returns: boolean
    """        

    return my_int_str == my_int_str[::-1]

def is_ambigram(my_int):
    """
    Name: is_ambigram -- Determines if a number is both a palindrome and an
        ambigram. Uses two helper functions: check_ambigram and
        check_palindrome.
    Parameters: my_integer(int) -- a non-negative integer
    Returns: boolean
    """

    if my_int < 0:
        print("Integer must be positive.") 
    
    my_int_str = str(my_int)
    ambigram_indicator = check_ambigram(my_int_str)
    palindrome_indicator = check_palindrome(my_int_str)

    if ambigram_indicator == True and palindrome_indicator == True:
        return True
    return False 


# Question 13
class ElectricCar:
    """
    Class: ElectricCar
    Attributes: name, battery, winter (default) 
    Methods: calculate_range, get_winter, set_winter, get_name
    """   

    def __init__(self, name, battery):
        self.name = name 
        self.battery = battery
        self.winter = False  # Default 
        if self.battery < MIN_BATTERY_VALUE or self.battery > \
           MAX_BATTERY_VALUE:
            raise ValueError
           
    def calculate_range(self, state_of_charge):
        self.state_of_charge = state_of_charge
        if self.state_of_charge < MIN_CHARGE_STATE or self.state_of_charge > \
           MAX_CHARGE_STATE:
            raise ValueError

        if self.winter == True:
            self.winter_factor = WINTER_TRUE 
        elif self.winter == False:
            self.winter_factor = WINTER_FALSE 
        
        return self.battery * self.state_of_charge * self.winter_factor * 3

    def set_winter(self, value):
        self.winter = value
        if type(self.winter) != bool:
            raise TypeError

    def get_winter(self): # Changed to no parameter
        return self.winter

    def get_name(self):
        return self.name

    def __str__(self):
        return "This car is a " + self.name + " with a battery value of " \
               + str(self.battery) + "."
    

def main():


   

if __name__ == "__main__":
    main()



"""
Testing:

    # Questions 7:
    my_string = "I love CS5001 so very much."
    result = is_cs5001(my_string)
    print(result) 


    # Question 8:
    my_dict= {"mom": "Katie", "dad": "Steve", "kid": "Helen"}
    new_key = "pet"
    new_value = "Tutu"

    my_dict_2 = append(my_dict, new_key, new_value)


    # Question 6:
    my_dict= {"mom": "Katie", "dad": "Steve", "kid": "Helen"}
    new_key = "kid"
    new_value = "Tutu"

    sample_tuple = (my_dict, new_key, new_value)
    print(sample_tuple[0:2])  


    # Question 9:
    my_string = "Katie Davenport"
    reverse_string = recursive_reverse(my_string)
    print(reverse_string)     


    # Question 10: 
    my_list = [[1, 2], [3, 4], [5, 6]]
    reversed_pairs = reverse_list_of_pairs(my_list)
    print(reversed_pairs)
    print(my_list) 


    # Question 11: 
    integer_list = [1, 2, 3, 4, 5, 6]
    even_list = evens(integer_list) 
    print(even_list)
    print(integer_list) 


    # Question 12: 
    my_int = 520212025
    check = is_ambigram(my_int)
    print(check)


    class TestElectricCar(unittest.TestCase):
    '''
    __init__, set_winter, calculate_range
    '''
    def test_init(self):
        tesla = ElectricCar("Tesla Y", 78)
        self.assertEqual(tesla.get_name(), "Tesla Y")
        self.assertFalse(tesla.get_winter())
 
        machE = ElectricCar("Ford Mach-E", 80)
        self.assertEqual(machE.get_name(), "Ford Mach-E")
        self.assertFalse(machE.get_winter())

    def test_set_winter(self):
        tesla = ElectricCar("Tesla Y", 78)
        self.assertFalse(tesla.get_winter())
        tesla.set_winter(True)
        self.assertTrue(tesla.get_winter())
 
        tesla.set_winter(False)
        self.assertFalse(tesla.get_winter())
 
    def test_bad_init_low(self):
        with self.assertRaises(ValueError):
            car = ElectricCar("eYugo", 49.9)

    def test_bad_init_high(self):
        with self.assertRaises(ValueError):
            car = ElectricCar("eYugo", 200.1)
        
    def test_bad_range_low(self):
        with self.assertRaises(ValueError):
            car = ElectricCar("eYugo", 80)
            car.calculate_range(-1)

    def test_bad_range_high(self):
        with self.assertRaises(ValueError):
            car = ElectricCar("eYugo", 80)
            car.calculate_range(1.2)
 
    def test_range(self):
        tesla = ElectricCar("Tesla Y", 78) 
        machE = ElectricCar("Ford Mach-E", 80)

        self.assertEqual(tesla.calculate_range(1), 234)
        self.assertEqual(tesla.calculate_range(0.5), 117)

        machE.set_winter(True)
        self.assertAlmostEqual(machE.calculate_range(0.9), 151.2)

        machE.set_winter(False)
        self.assertEqual(machE.calculate_range(0.9), 216)

def main():
    unittest.main(verbosity = 3)


if __name__ == "__main__":
    main()


"""
