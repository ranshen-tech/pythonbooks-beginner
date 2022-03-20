name = "Bob Smith"
print(name.split())
print(name)
print(name.split()[-1])
print("\n")

pay = 100000
pay *= 1.10
print("%.2f" % pay)
print("\n")


class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


if __name__ == "__main__":
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(0.10)
    print(sue.pay)
    print(sue)
    print("\n")