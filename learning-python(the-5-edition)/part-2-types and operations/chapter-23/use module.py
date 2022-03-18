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

from small import x, y

x = 42
y[0] = 42
print(x)
print(y)
print("\n")


import small

print(small.x)
print(small.y)
print("\n")


# 跨文件的名称修改

from small import x, y

x = 42
print(x)

import small

small.x = 42
print(small.x)
print("\n")


# import 和 from 的等价性

# from module import name1, name2
# import module
# name1 = module.name1
# name2 = module.name2
# del module

# 文件产生命名空间

import module2

print(module2.sys)

print(module2.name)

print(module2.func)

print(module2.klass)
print("\n")

# \命名空间字典： __dict__

print(list(module2.__dict__.keys()))
print("\n")

print(list(name for name in module2.__dict__.keys() if not name.startswith("__")))
print(list(name for name in module2.__dict__ if not name.startswith("__")))
print("\n")

print(module2.name, module2.__dict__["name"])
print("\n")


# reload basic

# import module
# ...use module.attributes...
# ...
# ...
# from imp import reload
# reload(module)
# ...use module.attributes...


# reload example

import changer

changer.printer()


# import changer

# changer.printer()
# from imp import reload

# reload(changer)
# changer.printer()
