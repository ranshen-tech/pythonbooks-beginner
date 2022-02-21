import sys

print(dir(sys))
print(len(dir(sys)))
a = len([x for x in dir(sys) if not x.startswith("__")])
print(a)
print(len([x for x in dir(sys) if not x[0] == "_"]))
print("\n💖")

print(dir([]))
print("\n")
print(dir(list()))
print("\n")
print(dir(str()))
print("\n")
print(dir(""))
print("\n")

print(len(dir(list)))
print(len([x for x in dir(list) if not x.startswith("__")]))
print(len(dir(str)))
print(len([x for x in dir(str) if not x.startswith("__")]))
print("\n")

print([a for a in dir(list) if not a.startswith("__")])
print([a for a in dir(dict) if not a.startswith("__")])
print("\n")


def dir1(x):
    return [a for a in dir(x) if not a.startswith("__")]


print(dir1(tuple))
print("\n")
