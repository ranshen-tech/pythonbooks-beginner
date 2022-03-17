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
