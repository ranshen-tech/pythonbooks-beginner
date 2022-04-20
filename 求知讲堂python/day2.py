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


# for ... else ...
for item in range(1, 10):
    if item >= 5:
        break
    print(item)
else:
    print("已经执行完了吗")
print("\n")


# account = "ranshen"
# password = "ranshen0519"
# for i in range(3):
#     accounts = input("please input your account: ")
#     passwords = input("please input your password: ")
#     if accounts == account and passwords == password:
#         print("恭喜您登陆成功")
#         break
# else:
#     print("您的系统已被锁定...")
# print('\n')


index = 1
while index <= 10:
    print(index)
    index += 1
    if index == 6:
        break
else:
    print("else执行了吗？")
print("\n")


# 猜年龄
ranshen = "29"
# for i in range(3):
#     age = input("please input your age: ")
#     if age == ranshen:
#         break
# else:
#     reply = input("还要继续玩吗？")
#     if reply == "y" or "Y":


# # 猜年龄
# index = 0
# while index < 3:
#     age = input("please input your age: ")
#     if age == ranshen:
#         break
#     index += 1
#     if index == 3:
#         reply = input("还要继续玩吗？")
#         if reply == "y" or "Y":
#             index = 0
# print("\n")


# BMI
# height = 1.78
# weight = 62.5
# BMI = weight / height**2
# if BMI < 18.5:
#     print("过轻")
# elif BMI < 25:
#     print("正常")
# elif BMI < 28:
#     print("过重")
# elif BMI < 32:
#     print("肥胖")
# else:
#     print("过度肥胖")
# print("\n")


# 猜年龄
times = 0
counts = 3
while times < counts:
    age = int(input("please input your age:"))
    if age == 29:
        print("congratulation!")
        break
    elif age > 29:
        print("too old!")
    else:
        print("too young!")
    times += 1
    if times == 3:
        choose = input("还要继续吗: Y/N? ")
        if choose == "Y" or choose == "y":
            times = 0
        elif choose == "N" or choose == "n":
            break
        else:
            print("请输入正确标识")
