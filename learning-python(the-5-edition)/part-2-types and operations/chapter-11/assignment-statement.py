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
