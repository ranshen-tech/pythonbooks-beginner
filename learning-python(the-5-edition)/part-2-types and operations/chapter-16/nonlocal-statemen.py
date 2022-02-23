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

G = tester(42)
G("spam")
