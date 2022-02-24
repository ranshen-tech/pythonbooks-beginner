def keywordonly(a, *b, c):
    print(a, b, c)


keywordonly(1, 2, c=3)
keywordonly(a=1, c=3)
# keywordonly(1, 2, 3)
print("\n")


def keywordonly(a, *, b, c):
    print(a, b, c)


keywordonly(1, c=3, b=2)
keywordonly(c=3, b=2, a=1)
# keywordonly(1, 2, 3)
# keywordonly(1)
print("\n")


def keywordonly(a, *, b="spam", c="ham"):
    print(a, b, c)


keywordonly(1)
keywordonly(1, c=3)
keywordonly(a=1)
keywordonly(c=3, b=2, a=1)
keywordonly(1, 2)
print("\n")
