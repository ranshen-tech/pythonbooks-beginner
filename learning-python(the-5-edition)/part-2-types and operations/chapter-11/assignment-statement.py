# 赋值语句形式
spam = "Spam"
print(spam)
spam, ham = "yum", "YUM"
print(spam)
print(ham)
print("\n")

[spam, ham] = ["yum", "YUM"]
print(spam)
print(ham)
print([spam, ham])
print([spam, ham][0])
print("\n")

a, b, c, d = "spam"
print(a, b, c, d)
print(a)
print(b)
print(c)
print(d)
print("\n")

a, *b = "spam"
print(a)
print(*b)
print("\n")

spam = ham = "lunch"
print(spam)
print(ham)
spams = 0
spams += 42
print(spams)
print("\n")


# 序列赋值
nudge = 1
wink = 2
A, B = nudge, wink
print(A)
print(A, B)
print(type((A, B)))
[C, D] = [nudge, wink]
print(C, D)
print("\n")

nudge = 1
wink = 2
nudge, wink = wink, nudge
print(nudge, wink)
print("\n")

[a, b, c] = (1, 2, 3)
print(a, c)
print(b)
(a, b, c) = "ABC"
print(a, c)
print(b)
a, b, c = "ABC"
print(a, c)
print(b)
print("\n")


# 高级序列赋值语句模式
string = "SPAM"
a, b, c, d = string
print(a, d)
# a, b, c = string
a, b, c = string[0], string[1], string[2:]
print(a, b, c)

a, b, c = list(string[:2]) + [string[2:]]
print(a, b, c)

a, b = string[:2]
print(type(string[:2]))
c = string[2:]
print(a, b, c)

(a, b), c = string[:2], string[2:]
print(a, b, c)
print("\n")

((a, b), c) = ("SP", "AM")
print(a, b, c)
(a, b), c = "SP", "AM"
print(a, b, c)
print("\n")

for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:
    print(a, b, c)
for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
    print((a, b), c)
print("\n")
for a, b, c in [(1, 2, 3), (4, 5, 6)]:
    print(a, b, c)
for (a, b), c in [((1, 2), 3), ((4, 5), 6)]:
    print((a, b), c)
print("\n")

red, green, blue = range(3)
print(red, blue)
print("\n")

print(list(range(3)))
print("\n")

L = [1, 2, 3, 4]
while L:
    fnt, L = L[0], L[1:]
    print(fnt, L)
print("\n")

seq = [1, 2, 3, 4]
a, b, c, d = seq
print(a, b, c, d)
print("\n")

a, *b = seq
print(a)
print(b)
print("\n")

*a, b = seq
print(a)
print(b)
print("\n")

a, *b, c = seq
print(a)
print(b)
print(c)
print("\n")

a, b, *c = seq
print(a)
print(b)
print(c)
