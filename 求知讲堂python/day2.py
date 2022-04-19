# # 猜拳
# import random

# count = 1
# while count <= 10:
#     person = int(input("请出拳:[0:石头，1:剪刀，2:布]: "))
#     computer = random.randint(0, 2)
#     if person == 0 and computer == 2:
#         print("你输了")
#     elif person == 1 and computer == 0:
#         print("你输了")
#     elif person == 2 and computer == 1:
#         print("你输了")
#     elif person == computer:
#         print("平局")
#     else:
#         print("你赢了")
#     count += 1


# 输出1-10之间的数据
index = 1
while index <= 10:
    print(index)
    index += 1
print("\n")


# 打印九九乘法表
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print(f"{row}*{col}={int(row*col)}", end=" ")
        col += 1
    print()
    row += 1
print("\n")


# 打印直角三角形
row = 1
while row <= 7:
    col = 1
    while col <= row:
        print("*", end=" ")
        col += 1
    print()
    row += 1
print("\n")


# 打印倒直角三角形
row = 7
while row >= 1:
    col = 1
    while col <= row:
        print("*", end=" ")
        col += 1
    print()
    row -= 1
print("\n")


# 打印等腰直角三角形
row = 1
while row <= 5:
    j = 1
    while j <= 5 - row:
        print(" ", end="")
        j += 1

    k = 1
    while k <= 2 * row - 1:
        print("*", end="")
        k += 1
    print()
    row += 1
print("\n")


sum = 0
for i in range(1, 101):
    sum += i
print(f"sum = {sum}")
print("\n")


sum = 0
for i in range(1, 51):
    if sum > 100:
        print(f"循环执行到{i}结束")
        break
    sum += i
print(sum)
print("\n")


for item in range(10):
    if item % 2 == 0:
        continue
    print(item)
print("\n")


for item in "i love python":
    if item == "e":
        break
    print(item)
print("\n")


for item in "i love python":
    if item == "o":
        continue
    print(item)
print("\n")


index = 1
while index <= 100:
    if index > 20:
        break
    print(index)
    index += 1
print("\n")


for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}*{j}={i*j}", end=" ")
    print()
print("\n")
