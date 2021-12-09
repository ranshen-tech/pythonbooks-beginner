CHAR = '*'
def rectangle(height, width):
    """prints the rectangle."""
    for row in range(height):
        for col in range(width):
            print(CHAR, end='')
        print()

def square(side):
    """prints a square."""
    rectangle(side, side)

