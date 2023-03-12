"""
    CS5001
    Spring 2022
    Homework 7: Test suite for the SimpleFractionTest class
    Katie Davenport

    Imports from SimpleFraction.py and tests the SimpleFraction class by
    creating objects, calling methods on those objects, and making sure that
    the values of the attributes are what we expect.

    Negative tests are included with test names ending in "_negative".
    The output for most of these is 'ERROR' except for one using assertFalse. 
"""

import unittest 
from SimpleFraction import SimpleFraction

class TestSquare(unittest.TestCase):
    
    # Testing for __init__:
    def test_init_1(self):
        fraction = SimpleFraction(2, 5)
        self.assertEqual(fraction.numerator, 2)
        self.assertEqual(fraction.denominator, 5)

    def test_init_2(self):
        fraction = SimpleFraction()
        self.assertEqual(fraction.numerator, 1)
        self.assertEqual(fraction.denominator, 1)

        # This is a negative test. We expect an ERROR.
    def test_init_negative(self):
        fraction = SimpleFraction(-3.5, 0)
        self.assertEqual(fraction.numerator, -3.5)
        self.assertEqual(fraction.denominator, 0)         

    # Testing for get_numerator:    
    def test_get_numerator_1(self):   
        fraction = SimpleFraction()
        self.assertEqual(fraction.get_numerator(), 1)

        # This is a negative test. We expect an ERROR.
    def test_get_numerator_negative(self):   
        fraction = SimpleFraction(2.5, 7)
        self.assertEqual(fraction.get_numerator(), 2)    

    # Testing for get_denominator:
    def test_get_denominator(self):
        fraction = SimpleFraction(0, -3)
        self.assertEqual(fraction.get_denominator(), -3)

        # This is a negative test. We expect an ERROR.
    def test_get_denominator_negative(self):
        fraction = SimpleFraction(2, 0)
        self.assertEqual(fraction.get_denominator(), 0)

    # Testing for make_reciprocal:
    def test_make_reciprocal(self):
        fraction = SimpleFraction(2, 4)
        self.assertEqual(fraction.make_reciprocal(), 2)
        
        # This is a negative test. We expect an ERROR.
    def test_make_reciprocal_negative(self):
        fraction_1 = SimpleFraction(0, -3)
        self.assertEqual(fraction.make_reciprocal(), 0)

    # Testing for validate:
    def test_validate(self):
        fraction = SimpleFraction()  
        self.assertEqual(fraction.validate(), True)

        # This is a negative test. We expect an ERROR. 
    def test_validate_negative(self):
        fraction = SimpleFraction(1.5, -3.5)  
        self.assertEqual(fraction.validate(), True)

    # Testing for multiply:
    def test_multiply_1(self):
        fraction = SimpleFraction(2, 4)
        self.assertEqual(fraction.multiply(16), 8)

    def test_multiply_2(self):
        fraction_1 = SimpleFraction(1, -3)
        fraction_2 = SimpleFraction(3, 1)
        self.assertEqual(fraction_1.multiply(fraction_2), -1)    

    # Testing for divide: 
    def test_divide_1(self):
        fraction = SimpleFraction(2, 4)
        self.assertAlmostEqual(fraction.divide(2), 0.25)

    def test_divide_2(self):
        fraction_1 = SimpleFraction(4, 1)
        fraction_2 = SimpleFraction(16, 1)
        self.assertAlmostEqual(fraction_1.divide(fraction_2), 0.25)     

    # Testing for __str__:
    def test_str_1(self):
        fraction = SimpleFraction(2, -4)
        expected_output = "2/-4"
        self.assertEqual(fraction.__str__(), expected_output)

    def test_str_2(self):
        fraction = SimpleFraction()
        expected_output = "1/1"
        self.assertEqual(fraction.__str__(), expected_output)

        # This is a negative test. We expect an ERROR. 
    def test_str_negative(self):
        fraction = SimpleFraction(4, 0)
        expected_output = "4/0"
        self.assertEqual(fraction.__str__(), expected_output)

    # Testing for __eq__:
    def test_eq_1(self):
        fraction_1 = SimpleFraction()
        fraction_2 = SimpleFraction(6, 6) 
        self.assertTrue(fraction_1.__eq__(1))
        self.assertTrue(fraction_1.__eq__(fraction_2))

    # Negative test using assertFalse (output is 'ok'). 
    def test_eq_2(self):
        fraction_1 = SimpleFraction(1, 5)
        fraction_2 = SimpleFraction(-3, -6) 
        self.assertFalse(fraction_1.__eq__(fraction_2))
       
def main():
    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()
