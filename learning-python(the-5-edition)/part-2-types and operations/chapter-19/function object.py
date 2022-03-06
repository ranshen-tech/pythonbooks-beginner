# indirect function call


def echo(message):
    print(message)


echo("Direct call")

x = echo
x("Indirect call!")
print("\n")


def indirect(func, arg):
    func(arg)


indirect(echo, "Argument call")
print("\n")


schedule = [(echo, "Spam!"), (echo, "Ham!")]
for func, arg in schedule:
    func(arg)
print("\n")


def make(label):
    def echo(message):
        print(label + ":" + message)

    return echo


F = make("Spam")
F("Ham")
F("Eggs")
print("\n")
