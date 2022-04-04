# 3.7
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print("\n")


# 5.5
for item in range(10):
    if item == 3:
        break
    print(item)
else:
    print("for over!")
print("\n")


i, r, s, t = 100, 0, 0, 0
while i < 1000:
    r = i // 100
    s = (i - r * 100) // 10
    t = i - r * 100 - s * 10
    if i == r**3 + s**3 + t**3:
        print("i =", str(i))
    i += 1
print("\n")


for i in range(100, 1000):
    r = i // 100
    s = (i - r * 100) // 10
    t = i - r * 100 - s * 10
    if i == r**3 + s**3 + t**3:
        print("i =", str(i))
print("\n")


# 6.1
a = "Hello"
print(max(a))
print(min(a))
print(len(a))
print(a[::-1])
print("\n")


# 6.2
print(list("hello"))
list = [20, 10, 50, 30]
t = [1, 2, 3]
list.extend(t)
print(list)
list.insert(2, 80)
print(list)
print("\n")


# 6.3
print(tuple([21, 23, 32, 43]))
print("\n")


# 6.4
a = set("hello")
print(a)
print(type(a))
b = {}
print(type(b))
print("\n")


# 6.6
d = {1: "ran", 2: "xu", 3: "zhu"}
print("---遍历键---")
for k in d.keys():
    print(f"学号: {k}")

print("\n---遍历值---")
for v in d.values():
    print(f"学生: {v}")

print("\n---遍历键:值---")
for d_id, d_name in d.items():
    print(f"学号: {d_id} - 学生: {d_name}")
print("\n")


# 7.4
s = "hello world"
print(s.find("l", 4, 10))
print("\n")


wordstring = """
    it was the best of time it was the worst of time.
    it was the wisdom of age it was the foolish of age.
    """
# 标点符号替换
wordstring = wordstring.replace(".", "")
print(wordstring)

# 分割单词
wordlist = wordstring.split()
print(wordlist)

wordreq = []
for w in wordlist:
    # 统计单词出现个数
    wordreq.append(wordlist.count(w))

d = dict(zip(wordlist, wordreq))
print(d)
print("\n")


s = "Python"
print("{}".format(s))
