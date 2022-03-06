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
