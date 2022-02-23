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


# nonlocal state of variable(变量的状态)


def tester(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1

    return nested


F = tester(78)
F("spam")
# print(F.state)
print("\n")


def tester(start):
    global state
    state = start

    def nested(label):
        global state
        print(label, state)
        state += 1

    return nested


F = tester(9)
F("spam")
F("eggs")

G = tester(42)
G("toast")
G("bacon")
F("ham")
print("\n")


class tester:
    def __init__(self, start):
        self.state = start

    def nested(self, label):
        print(label, self.state)
        self.state += 1


F = tester(0)
F.nested("spam")
F.nested("ham")
print("\n")

G = tester(42)
G.nested("toast")
G.nested("bacon")
F.nested("eggs")
print(F.state)
print("\n")


class tester:
    def __init__(self, start):
        self.state = start

    def __call__(self, label):
        print(label, self.state)
        self.state += 1


H = tester(99)
H("juice")
H("pancakes")
print("\n")
