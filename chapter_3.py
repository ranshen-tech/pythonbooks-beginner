# 3-1
names = ['ran shen', 'xu peng', 'zhu yucheng']

print(names[0])
print(names[1])
print(names[2])


# 3-2
msg = f"\nHello, {names[0].title()}!"
print(msg)

msg = f"Hello, {names[1].title()}!"
print(msg)

msg = f"Hello, {names[2].title()}!"
print(msg)


# 3-4
guests = ['ran shen', 'xu peng', 'zhu yucheng']

name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")


# 3-5
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# Xu Peng无法赴约，转而邀请Chen Yuanyuan
del guests[1]
guests.insert(1, 'chen yuanyuan')

# 重新打印邀请函
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")


# 3-6
# 找到一张更大的餐桌，再邀请一些嘉宾
print("\nWe got a bigger table!")
guests.insert(0, 'chen weibo')
guests.insert(2, 'meng hao')
guests.append('long yue')

name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.")


# 3-7
# 糟糕，餐桌无法及时送达
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

# 应该只剩下两位嘉宾了，向他们发出邀请
name = guests[0]
print(f"{name.title()}, please come to dinner.")

name = guests[1]
print(f"{name.title()}, please come to dinner.")

# 清空名单
del guests[0]
del guests[0]

# 核实名单是空的
print(guests)


# 3-8
locations = ['new york', 'hefei', 'london', 'shanghai', 'hangzhou']
print("\nOriginal order:")
print(locations)

print("\nAlphabetical:")
print(sorted(locations))

print("\nOriginal order:")
print(locations)

print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

print("\nOriginal order:")
print(locations)

print("\nReversed:")
# 永久改变列表顺序
locations.reverse()
print(locations)

print("\nOriginal order:")
locations.reverse()
print(locations)

print("\nAlphabetical:")
locations.sort()
print(locations)

print("\nReverse alphabetical:")
locations.sort(reverse=True)
print(locations)