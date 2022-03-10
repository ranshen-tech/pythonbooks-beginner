# 空间与时间、简洁性、表现力

import math

print(math.factorial(10))
from permute import permute1, permute2

seq = list(range(10))
p1 = permute1(seq)
print(len(p1), p1[0], p1[1])
print("\n")


p2 = permute2(seq)
print(next(p2))
print(next(p2))

p2 = list(permute2(seq))
print(p1 == p2)
print("\n")


print(math.factorial(50))
p3 = permute2(list(range(50)))
print(next(p3))
print("\n")


import random

print(math.factorial(20))
seq = list(range(20))

random.shuffle(seq)
p = permute2(seq)
print(next(p))
print(next(p))
