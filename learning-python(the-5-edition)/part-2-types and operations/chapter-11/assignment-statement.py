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
