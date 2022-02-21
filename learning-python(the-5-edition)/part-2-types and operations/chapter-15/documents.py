import sys

print(dir(sys))
print(len(dir(sys)))
a = len([x for x in dir(sys) if not x.startswith("__")])
print(a)
print(len([x for x in dir(sys) if not x[0] == "_"]))
print("\n💖")


# dir()

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

print(dir(str) == dir(""))
print(dir(list) == dir([]))
print(dir(str()) == dir(""))
print("\n")


# Docstring: __doc__
import docstrings

print(docstrings.__doc__)
print(docstrings.square.__doc__)
print(docstrings.Employee.__doc__)
print("\n")


# built-in docstring

print(sys.__doc__)
print(sys.getrefcount.__doc__)
print("\n")
print(int.__doc__)
print(map.__doc__)
print("\n")


# help()

# print(help(sys))
# print(help(dict))
# print(help(str.replace))
# print(help("".replace))
# print(help(ord))
# print(help("re"))
# print(help(docstrings))
# print(help(docstrings.square))
# print(help(docstrings.Employee))


# HTML
