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

print({"a": 1, "b": 2}["b"])
d = {"x": 1, "y": 2, "z": 3}
d["w"] = 0
print(d["x"] + d["w"])
d[(1, 2, 3)] = 4
print(list(d.keys()), list(d.values()), (1, 2, 3) in d)
print([[]], ["", [], (), {}, None])
print("\n")


# exercise2
l = [0, 1, 2, 3]
print(l[-1000:100])
l1 = l[:]
l2 = l[-1000:100]
print(l1)
print(l2)
print(l1 == l2)
print(l1 is l2)
print(l[:39])
print("\n")

print(l[3:1])
print(l[1:3])
print(l[3])
l[3:1] = [7, 6]
print(l)
print("\n")


# exercise3
l = [1, 2, 3, 4]
l[2] = []
print(l)
l[2:3] = []
print(l)
del l[0]
print(l)
print("\n")

l = [1, 2, 3, 4]
del l[1:]
print(l)
l[1:2] = [1]
print(l)
print("\n")


# exercise4
x = "spam"
y = "eggs"
x, y = y, x
print(x, y)
print("\n")


# exercise5
d = {}
d[1] = "a"
d[2] = "b"
d[(1, 2, 3)] = "c"
print(d)
print("\n")


# exercise6
