# Class


class ShareData:
    spam = 42


x = ShareData()
y = ShareData()
print(x.spam, y.spam)
print("\n")

ShareData.spam = 99
print(x.spam, y.spam, ShareData.spam)

x.spam = 88
print(x.spam, y.spam, ShareData.spam)
print("\n")


class MixedNames:
    data = "spam"

    def __init__(self, value):
        self.data = value

    def display(self):
        print(self.data, MixedNames.data)


x = MixedNames(1)
y = MixedNames(2)
x.display()
y.display()
print("\n")


# Method


class NextClass:
    def printer(self, text):
        self.message = text
        print(self.message)


x = NextClass()
x.printer("instance call")
print(x.message)
print("\n")

NextClass.printer(x, "class call")
print(x.message)
# NextClass.printer("bad call")
