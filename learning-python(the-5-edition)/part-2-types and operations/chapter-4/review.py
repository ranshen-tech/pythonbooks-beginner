s = set("123")
print(s)
s = set("abc")
print(s)
print("\n")

print(len(str(2**1000)))
print("\n")

# print(s[len(s) - 1])
# 'set' object is not subscriptable

s = "shrubbery"
l = list(s)
print(l)
l[1] = "c"
print("".join(l))
print(",".join(l))
print("\n")

s = "spam"
print(s.isalpha())
print("\n")

line = "aaa, bbb, ccccc, dd\n"
print(line)
line = line.rstrip()
print(line)
print(line.split(", "))
print(line.rstrip().split(", "))
print("\n")

print("%.2f | %05d" % (3.14159, -42))
print("\n")
