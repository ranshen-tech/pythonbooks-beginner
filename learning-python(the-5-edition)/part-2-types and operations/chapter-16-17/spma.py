import thismod

thismod.test()
print(thismod.var)
print("\n")

X = 99


def f1():
    X = 88

    def f2():
        print(X)

    f2()


f1()
