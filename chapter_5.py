# 5-3
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")

# 不能通过测试的版本（没有输出）
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")


# 5-4
# 执行if代码块的版本:
alien_color = 'green'

if alien_color == 'green':
    print("\nYou just earned 5 points!")
else:
    print("You just earned 10 points!")

# 执行else代码块的版本:
alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")


# 5-5
# 黄色版本
alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("\nYou just earned 10 points!")
else:
    print("You just earned 15 points!")

# 红色版本
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("\nYou just earned 15 points!\n")


# 5-6
age = 17

if age < 2:
    print("You are a baby!")
elif age < 4:
    print("You are a toddler!")
elif age < 13:
    print("You are a kid!")
elif age < 20:
    print("You are a teenager!")
elif age < 65:
    print("You are an adult!")
else:
    print("You are an elder!")


# 5-7
favourite_fruits = ['blueberries', 'oranges', 'bananas']

if 'oranges' in favourite_fruits:
    print("\nYou really love oranges!")
if 'blueberries' in favourite_fruits:
    print("You really love blueberries!")
if 'apples' in favourite_fruits:
    print("You really love apples!")
if 'kiwis' in favourite_fruits:
    print("You really love kiwis!")
if 'peaches' in favourite_fruits:
    print("You really love peaches!")


# 5-8
print()
usernames = ['ran shen', 'admin', 'zhu yucheng', 'xu peng', 'chen yuanyuan']

for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")


# 5-9
print()
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")


# 5-10
print()
current_users = [
    'ran shen', 'xu peng', 'zhu yucheng', 'chen yuanyuan', 'long yue'
    ]

new_users = [
    'Ran shen', 'zhu YuchEng', 'shao nan', 'chen weibo', 'gui rong'
    ]

# 列表解析
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.")


# 5-11
print()
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(f"{number}th")