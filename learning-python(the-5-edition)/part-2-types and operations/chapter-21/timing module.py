# 自己编写的计时模块

from timer0 import timer

print(timer(pow, 2, 1000))
print(timer(str.upper, "spam"))
print("\n")


import timer

print(timer.total(1000, pow, 2, 1000)[0])
print(timer.total(1000, str.upper, "spam"))
print("\n")

print(timer.bestof(1000, str.upper, "spam"))
print(timer.bestof(1000, pow, 2, 1000000)[0])
print("\n")

print(timer.bestof(50, str.upper, "spam"))
print(timer.bestoftotal(50, 1000, str.upper, "spam"))
print("\n")


print(min(timer.total(1000, str.upper, "spam") for i in range(50)))
print("\n")
