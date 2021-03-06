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

z = x.intersection(y)
print(z)
z.add("spam")
print(z)
z.update(set("XY"))
print(z)
z.remove("b")
print(z)
print("\n")

s = set([1, 2, 3])
print(s)
s | set([3, 4])
print(s)
s.union([3, 4])
print(s)
print(s.intersection((1, 3, 5)))
print(s.intersection([1, 3, 5]))
print("\n")

s = {1.23}
s.add((1, 2, 3))
print(s)
print(s | {(4, 5, 6), (1, 2, 3)})
print(s)
s.update({(4, 5, 6), (1, 2, 3)})
print(s)
print("\n")

l = [1, 2, 1, 3, 2, 4, 5]
print(l)
print(set(l))
l = list(set(l))
print(l)
print("\n")

print(set((1, 2, 3)))
print("\n")

l1, l2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
print(l1, l2)
print(l1 == l2)
print(set(l1) == set(l2))
print(sorted(l1) == sorted(l2))
print("spam" == "asmp", set("spam") == set("asmp"), sorted("spam") == sorted("asmp"))
print("\n")

print(True + 4)
