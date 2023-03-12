from Square import Square

def main():
    square = Square(2)
    print(square.get_area())
    print(square.get_perimeter())
    print(square.get_width())

    square.set_width(4)
    print(square.get_area())
    print(square.get_perimeter())
    print(square.get_width())
    
if __name__ == "__main__":
    main()
