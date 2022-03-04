"Use 3.X only keyword-only args"
import sys


def print3(*args, sep=" ", end="\n", file=sys.stdout):
    output = ""
    first = True
    for arg in args:
        output += ("" if first else sep) + str(arg)
        first = False
    file.write(output + end)


# print3(99, name="Bob")


def print3(*args, **kargs):
    sep = kargs.pop("sep", " ")
    end = kargs.pop("end", "\n")
    file = kargs.pop("file", sys.stdout)
    if kargs:
        raise TypeError("extra keywords: %s" % kargs)
    output: ""
    first = True
    for arg in args:
        output += ("" if first else sep) + str(arg)
        first = False
    file.write(output + end)


print3(99, name="bob")
