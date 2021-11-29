# challenge1
def squared(x):
    """ Takes an int and returns it multiplied by 2.
    :param x: int.
    :return: x multiplied by 2.
    """
    return x ** 2

print(squared(2))


# challenge2
def print_string(string):
    """ Prints the string passed in.
    :param string: str.
    """
    print(string)

print_string("Testing: 1, 2, 3.")


# challenge3
def add_mult(a, b, c, x=100, z=1000):
    """ Returns the result of two optional params
    multiplied by the addition of 3 required params.
    :param a: int.
    :param b: int.
    :param c: int.
    :param x: int.
    :param z: int.
    :return: int.
    """
    return (a + b + c) * x * z

result = add_mult(10, 15, 25)
print(result)


# challenge4
def divide(x):
    return x / 2


def multiply(x):
    return x * 4

y = divide(4)
z = multiply(y)

print(z)


# challenge5
def convert(string):
    """ Converts passed in str to int.
    :param string: str.
    :return: string converted to int.
    """
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")

c = convert("55.0")
print(c)

