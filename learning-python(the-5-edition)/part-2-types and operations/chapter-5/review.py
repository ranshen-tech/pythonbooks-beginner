print(10 / 4)
print(10 // 4)
print("\n")


import math

print(math.floor(2.5))
print(math.floor(-2.5))
print(math.trunc(2.5))
print(math.trunc(-2.5))
print("\n")

print(math.pi, math.e)
print(math.sin(2 * math.pi / 180))
print("\n")

print(math.sqrt(144), math.sqrt(2))
print("\n")

print(pow(2, 4))
print(abs(-42.0), sum([1, 2, 3, 4]))
print("\n")

print(math.floor(2.567), math.floor(-2.567))
print(math.trunc(2.567), math.trunc(-2.567))
print(round(2.567), round(2.467), round(2.567, 2))
print("\n")


import random

print(random.random())
print(random.randint(1, 3))
suits = ["hearts", "clubs", "diamonds", "spades"]
print(suits)
random.shuffle(suits)
print(suits)
random.shuffle(suits)
print(suits)
print("\n")


from decimal import Decimal

print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))
print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3"))
print("\n")


from fractions import Fraction

x = Fraction(1, 3)
y = Fraction(4, 6)
print(x)
print(y)
print(type(x))
print(x - y)
print("\n")

x = set("abcde")
print(x)
y = set("bdxyz")
print(y)
print(x - y)
print(x ^ y)
print("\n")
