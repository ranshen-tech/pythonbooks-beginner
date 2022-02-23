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
