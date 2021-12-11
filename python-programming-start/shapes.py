def codesum(s):
    """Returns the sums of the character codes of s."""
    total = 0
    for c in s:
        total = total + ord(c)
    return total

print(codesum('ranshen'))

print(ord.__doc__)