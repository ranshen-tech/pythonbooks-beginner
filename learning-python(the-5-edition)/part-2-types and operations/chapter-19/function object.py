# indirect function call


def echo(message):
    print(message)


echo("Direct call")

x = echo
x("Indirect call!")
print("\n")


def indirect(func, arg):
    func(arg)


indirect(echo, "Argument call")
print("\n")


schedule = [(echo, "Spam!"), (echo, "Ham!")]
for func, arg in schedule:
    func(arg)
print("\n")


def make(label):
    def echo(message):
        print(label + ":" + message)

    return echo


F = make("Spam")
F("Ham")
F("Eggs")
print("\n")


# function自省


def func(a):
    b = "spam"
    return b * a


print(func(8))
print(func.__name__)
print(dir(func))
print("\n")

print(func.__code__)
print(dir(func.__code__))
print("\n")

print(func.__code__.co_varnames)
print(func.__code__.co_argcount)
print("\n")


# function attributes


print(func)
func.count = 0
func.count += 1
print(func.count)
func.handles = "Button-Press"
print(func.handles)
print(dir(func))
print("\n")


def f():
    pass


print(f())
print(len(dir(f)))
print([x for x in dir(f) if not x.startswith("__")])
print("\n")


# Python3.X 中的function annotation


def func(a, b, c):
    return a + b + c


print(func(1, 2, 3))
print("\n")


def func(a: "spam", b: (1, 10), c: float) -> int:
    return a + b + c


print(func(1, 2, 3))
print(func.__annotations__)
print("\n")


def func(a: "spam", b, c: 99):
    return a + b + c


print(func(1, 2, 3))
print(func.__annotations__)
print("\n")

for arg in func.__annotations__:
    print(arg, "=>", func.__annotations__[arg])
print("\n")


def func(a: "spam" = 4, b: (1, 10) = 5, c: float = 6) -> int:
    return a + b + c


print(func(1, 2, 3))
print(func())
print(func(1, c=10))
print(func.__annotations__)
print("\n")


def func(a: "spam" = 4, b: (1, 10) = 5, c: float = 6) -> int:
    return a + b + c


print(func(1, 2))
print(func.__annotations__)
