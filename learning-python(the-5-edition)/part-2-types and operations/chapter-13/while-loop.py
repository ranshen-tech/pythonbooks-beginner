# 示例
# while True:
# print("Type Ctrl-C to stop me!")

x = "spam"
while x:
    print(x, end=" ")
    x = x[1:]
print("\n")

a, b = 0, 10
while a < b:
    print(a, end=" ")
    a += 1
print("\n")

# while True:
# pass
# if exitTest():
# break


# pass

# while True:
# pass


def func1():
    pass


def func2():
    pass


def func1():
    ...


def func2():
    ...


func1()


def func1():
    ...


def func2():
    ...


func1()

x = ...
print(x)
print("\n")


# continue
x = 10
while x:
    x -= 1
    if x % 2 != 0:
        continue
    print(x, end=" ")
print("\n")

x = 10
while x:
    x -= 1
    if x % 2 == 0:
        print(x, end=" ")
print("\n")


# break

# while True:
#     name = input("Enter name:")
#     if name == "stop":
#         break
#     age = input("Enter age: ")
#     print("Hello", name, "=>", int(age) ** 2)


# 循环的else
y = 4
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, "has factor", x)
        break
    x -= 1
else:
    print(y, "is prime")
print("\n")

found = False
# while x and not found:
#     if match(x[0]):
#         print("Ni")
#         found = True
#     else:
#         x = x[1:]
# if not found:
# print("not found")

# while x:
#     if match(x[0]):
#         print("Ni")
#         break
#     x = x[1:]
# else:
#     print("Not found")

x = []
while x:
    if x[0]:
        print("Ni")
        break
    x = x[1:]
else:
    print("Not found")
print("hello")
