"""
Use this as a driver for the SimpleFraction class.

"""

from SimpleFraction import SimpleFraction
from FractionTextPresenter import FractionTextPresenter
from FractionTurtlePresenter import FractionTurtlePresenter

def main():
    
    fraction = SimpleFraction(2, -4)
    print("Numerator: ", fraction.get_numerator())
    print(fraction.get_denominator())
    print(fraction.make_reciprocal())
    print(fraction.multiply(4))
    print(fraction.divide(6))
    print(SimpleFraction(2,4))
    print(SimpleFraction())

    

if __name__ == "__main__":
    main()




