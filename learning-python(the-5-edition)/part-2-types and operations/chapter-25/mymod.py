def countLines(name):  # 21
    file = open(name)  # 17
    return len(file.readlines())  # 28


def countChars(name):  # 21
    return len(open(name).read())  # 29


def test(name):  # 15
    return countLines(name), countChars(name)  # 41


if __name__ == "__main__":
    print(test("chapter-25/mymod.py"))


if __name__ == "__main__":
    print(test(input("Enter file name:")))
