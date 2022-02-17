a = 1
b = 2
c = 3
print(a + b)

mylist = [1111, 2222, 3333]
print(mylist)

x = 1 + 2 + 3 + 4
print(type(x))
print(x)

if a == 1 and b == 2 and c == 3:
    print("spam" * 3)
print("\n")


# 简短示例：交互式循环

# while True:
#     reply = input("Enter text: ")
#     if reply == "stop":
#         break
#     print(reply.upper())


# while True:
#     reply = input("Enter text: ")
#     if reply == "stop":
#         break
#     print(int(reply) ** 2)
# print("Bye")


# S = "123"
# T = "xxx"
# print(S.isdigit(), T.isdigit())

# while True:
#     reply = input("Enter text: ")
#     if reply == "stop":
#         break
#     elif not reply.isdigit():
#         print("Bad" * 8)
#     else:
#         print(int(reply) ** 2)
# print("Bye")


# while True:
#     reply = input('Enter text: ')
#     if reply == 'stop':
#         break
#     try:
#         num = int(reply)
#     except:
#         print('Bad!' * 8)
#     else:
#         print(num ** 2)
# print('Bye')


# while True:
#     reply = input("Enter text: ")
#     if reply == "stop":
#         break
#     try:
#         print(int(reply) ** 2)
#     except:
#         print("Bad!" * 8)
# print("Bye")


# while True:
#     reply = input("Enter text: ")
#     if reply == "stop":
#         break
#     try:
#         print(float(reply) ** 2)
#     except:
#         print("Bad!" * 8)
# print("Bye")


while True:
    reply = input("Enter text: ")
    if reply == "stop":
        break
    elif not reply.isdigit():
        print("Bad!" * 8)
    else:
        num = int(reply)
        if num < 20:
            print("low")
        else:
            print(num**2)
print("Bye")
