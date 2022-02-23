# def func():
#     nonlocal name1, name2, ...


# nonlocal use


def tester(start):
    state = start

    def nested(label):
        print(label, state)

    return nested


F = tester(0)
F("spam")
F("ham")
print("\n")


def tester(start):
    state = start

    def nested(label):
        print(label, state)
        state += 1

    return nested


F = tester(0)
# F("spam")


def tester(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1

    return nested


F = tester(0)
F("spam")
F("ham")
F("eggs")
print("\n")

G = tester(42)
G("spam")
G("eggs")
F("bacon")
print("\n")


def tester(start):
    def nested(label):
        global state
        state = 0
        print(label, state)

    return nested


F = tester(0)
F("abc")
print(state)

C = tester(3)
C("ranshen")
print("\n")

spam = 99


def tester():
    def nested():
        global spam
        print("Current=", spam)
        spam += 1

    return nested


tester()()
tester()()
tester()()
print("\n")
