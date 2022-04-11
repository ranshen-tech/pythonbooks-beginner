# 猜拳
import random

count = 1
while count <= 10:
    person = int(input("请出拳:[0:石头，1:剪刀，2:布]: "))
    computer = random.randint(0, 2)
    if person == 0 and computer == 2:
        print("你输了")
    elif person == 1 and computer == 0:
        print("你输了")
    elif person == 2 and computer == 1:
        print("你输了")
    elif person == computer:
        print("平局")
    else:
        print("你赢了")
    count += 1


# 输出1-10之间的数据
index = 1
while index <= 10:
    print(index)
index += 1


# 打印九九乘法表
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print(f"{row}*{col}={int(row*col)}", end=" ")
        col += 1
    print()
    row += 1


# 打印直角三角形
row = 1
while row <= 7:
    col = 1
    while col <= row:
        print("*", end=" ")
        col += 1
    print()
    row += 1


# 打印倒直角三角形
row = 7
while row >= 1:
    col = 1
    while col <= row:
        print("*", end=" ")
        col += 1
    print()
    row -= 1


# 打印等腰直角三角形
