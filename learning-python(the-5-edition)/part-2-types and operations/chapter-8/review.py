print(map(ord, "spam"))
print(list(map(ord, "spam")))
print("\n")

l = ["spam", "Spam", "SPAM!"]
print(l[1:3])
print(l[1:2])
print(l[1:])
print("\n")

l = [2, 3, 4, 1]
print(l[len(l) :])
l[len(l) :] = [5, 6, 7]
print(l)
print("\n")

l = ["abc", "ABD", "aBe"]
l.sort()
print(l)
l = ["abc", "ABD", "aBe"]
l.sort(key=str.lower)
print(l)

l = ["abc", "ABD", "aBe"]
l.sort(key=str.lower, reverse=True)
print(l)
print("\n")

l = ["abc", "ABD", "aBe"]
print(sorted(l, key=str.lower, reverse=True))
print(l)
l = ["abc", "ABD", "aBe"]
print(sorted([x.lower() for x in l], reverse=True))
print("\n")

l = [1, 2, 3, 4]
print(list(reversed(l)))
print("\n")

l = ["spam", "eggs", "ham"]
print(l.index("eggs"))
l.insert(1, "toast")
print(l)
l.remove("eggs")
print(l)
l.pop(1)
print(l)
print(l.count("spam"))
print("\n")
