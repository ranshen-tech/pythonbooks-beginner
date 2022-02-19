for line in open("log.txt").readlines():
    print(line.rstrip())
print("\n")

for line in open("log.txt"):
    print(line)
print("\n--")

for line in reversed(open("log.txt")):
    print(line)
