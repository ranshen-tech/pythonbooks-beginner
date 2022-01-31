X = set("spam")
Y = {"h", "a", "m"}

print(X, Y)

print(X & Y)
print(X | Y)
print(X - Y)
print(X > Y)

print({n**2 for n in [1, 2, 3, 4]})

print(list(set([1, 2, 1, 3, 1])))
print(set([1, 2, 1, 3, 1]))
print(set("spam") - set("ham"))
print(set("spam") == set("asmp"))

print("p" in set("spam"), "p" in "spam", "ham" in ["eggs", "spam", "ham"])
