f = open("data.txt", "w")
f.write("Hello\n")
f.write("world\n")
f.close()


f = open("data.txt")
text = f.read()
print(text)
for line in open("data.txt"):
    print(line)
print("\n")

# print(dir(f))
# print(help(f.seek))
print(set([1, 2, 1, 3, 1]))
print("\n")

l = ["spam!"]
print(l * 5)
print("\n")


class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= 1.0 + percent


bob = Worker("Bob Smith", 50000)
sue = Worker("Sue Jones", 60000)

print(bob.lastName())
print(sue.lastName())
sue.giveRaise(0.10)
print(sue.pay)
print("\n")
