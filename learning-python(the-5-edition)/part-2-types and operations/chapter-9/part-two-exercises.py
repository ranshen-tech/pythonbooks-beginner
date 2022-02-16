# Numbers
print(2**16)
print(2 / 5, 2 / 5.0)
print("\n")

# String
print("spam" + "eggs")
s = "ham"
print("eggs" + s)
print(s * 5)
print(s[:0])

print("green %s and %s" % ("eggs", s))
print("green {0} and {1}".format("eggs", s))
print("\n")

# Tuples
print(("x",)[0])
print(("x", "y")[1])
print("\n")

# Lists
L = [1, 2, 3] + [4, 5, 6]
print(L, L[:], L[:0], L[-2], L[-2:])
print(([1, 2, 3] + [4, 5, 6])[2:4])
print([L[2], L[3]])
L.reverse()
print(L)
L.sort()
print(L)
print(L.index(4))
print("\n")


# Dictionaries
print({"a": 1, "b": 2}["b"])
D = {"x": 1, "y": 2, "z": 3}
D["w"] = 0
print(D)
print(D["x"] + D["w"])
