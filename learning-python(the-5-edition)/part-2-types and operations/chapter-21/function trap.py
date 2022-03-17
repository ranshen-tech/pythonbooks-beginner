# 局部变量是被静态检测的

X = 99


def selector():
    print(X)


selector()
print("\n")


def selector():
    print(X)
    X = 88


# selector()


def selector():
    global X
    print(X)
    X = 88


selector()
print("\n")


X = 99


def selector():
    import __main__

    print(__main__.X)
    X = 88
    print(X)


selector()
print("\n")


# default value parameter and variable object


def saver(x=[]):
    x.append(1)
    print(x)


saver([2])
saver([2])
saver()
saver()
saver()
print("\n")


def saver(x=None):
    if x is None:
        x = []
    x.append(1)
    print(x)


saver([2])
saver()
saver()
print("\n")


def saver():
    saver.x.append(1)
    print(saver.x)


saver.x = []
saver()
saver()
saver()
print("\n")
