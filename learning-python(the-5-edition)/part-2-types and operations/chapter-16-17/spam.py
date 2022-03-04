from makeopen import makeopen

makeopen("spam")

F = open("script2.py")
F.read()

makeopen("eggs")
F = open("script2.py")
F.read()


import builtins


class makeopen:
    def __init__(self, id):
        self.id = id
        self.original = builtins.open
        builtins.open = self

    def __call__(self, *kargs, **pargs):
        print("Custom open call %r" % self.id, kargs, pargs)
        return self.original(*kargs, **pargs)


print("\n")


# exercise
X = "Spam"


def func():
    print(X)


func()
print("\n")


x = "Spam"


def func():
    x = "NI"


func()
print(X)
print("\n")


x = "Spam"


def func():
    x = "NI"
    print(x)


func()
print(x)
print("\n")


def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i**x)
    return acts


acts = makeActions()
print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))
print("\n")


X = "Spam"


def func():
    global X
    X = "NI"


func()
print(X)
print("\n")


X = "Spam"


def func():
    X = "NI"

    def nested():
        print(X)

    nested()


func()
print(X)
print("\n")


def func():
    X = "NI"

    def nested():
        nonlocal X
        X = "Spam"

    nested()
    print(X)


func()
