# exercise1
print(2**16)
print(2 / 5, 2 / 5.0)
print("\n")

print("spam" + "eggs")
s = "ham"
print("eggs" + s)
print(s * 5)
print(s[:0])
print("green %s and %s" % ("eggs", s))
print("green {0} and {1}".format("eggs", s))
print(("x",)[0])
print(("x", "y")[1])
print("\n")

l = [1, 2, 3] + [4, 5, 6]
print(l, l[:], l[:0], l[-2], l[-2:])
print(([1, 2, 3] + [4, 5, 6])[2:4])
print(type(([1, 2, 3] + [4, 5, 6])))
print([l[2], l[3]])
l.reverse()
print(l)
l.sort()
print(l)
print(l.index(4))
print("\n")
