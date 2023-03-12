# Testing for Square

import unittest # This is a package
from Square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        sq = Square(5)
        self.assertEqual(sq.get_width(), 5)

    def test_get_area(self):
        sq = Square(10)
        self.assertEqual(sq.get_area(), 100)

    def test_get_perimeter(self):
        sq = Square(2)
        self.assertEqual(sq.get_perimeter(), 8)

    def test_non_integer_value(self):
        sq = Square(5.5)
        self.assertAlmostEqual(sq.get_area(), 30.25)

def main():
    unittest.main(verbosity = 3)

main()    

'''
negative_test
    - expect test to be negative
    raise value error

    screen shot of final test 
'''



    
