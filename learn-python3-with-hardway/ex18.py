# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"\narg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothing.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First! ")
print_none()

# note
# *args是把函数所有的参数都接收进来，只写一个args代替。
# 运行函数、调用函数和使用函数是同一个意思！