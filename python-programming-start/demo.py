
CHAR = '*'
def rectangle(height, width):
    """prints the rectangle."""
    for row in range(height):
        for col in range(width):
            print(CHAR, end='')
        print()

rectangle(2, 3)
