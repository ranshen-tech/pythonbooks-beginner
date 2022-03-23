import manynames

X = 66
print(X)
print(manynames.X)
print("\n")

manynames.f()
manynames.g()
print("\n")

print(manynames.C.X)
I = manynames.C()
print(I.X)
print("\n")

I.m()
print(I.X)
print("\n")


X = 11


def g1():
    print(X)


def g2():
    global X
    X = 22
    print(X)


def h1():
    X = 33

    def nested():
        print(X)


def h2():
    X = 33

    def nested():
        nonlocal X
        X = 44


if __name__ == "__main__":
    print(X)
    g1()
    g2()
    print(X)
