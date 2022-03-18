# import statement

import module1

module1.printer("Hello world!")


# from statement

from module1 import printer

print("Hello world!")
print("\n")


# from* statement

from module1 import *

printer("Hello world!")
print("\n")


import simple

print(simple.spam)
print("\n")


simple.spam = 2
import simple

print(simple.spam)
print("\n")


# 在模块中改变可变对象
