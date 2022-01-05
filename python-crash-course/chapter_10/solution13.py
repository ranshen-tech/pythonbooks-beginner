import json

def get_stored_username():
    """获取存储的用户名——如果存储了。"""
    filename = 'username.json'
    try:
       with open(filename) as f_obj:
           username = json.load(f_obj)
    except FileNotFoundError:
       return None
    else:
       return username

def get_new_username():
    """提示用户输入用户名。"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
       json.dump(username, f_obj)
    return username

def check_username():
    """检查用户名是否正确"""
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        return correct

def greet_user():
    """基于用户名问候用户。"""

    if check_username() == 'y':
        print(f"Welcome back, {check_username()}!")
        return

    username = get_new_username()
    print(f"We'll remember you when you come back, {username}!")

greet_user()