# 9-11
"""一系列模拟用户的类。"""

class User():
    """一个表示用户的简单类。"""
    
    def __init__(self, first_name, last_name, username, email, location):
        """初始化用户。"""

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """显示用户信息摘要。"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")

    def greet_user(self):
        """向用户发出个性化问候。"""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """将属性 login_attempts 的值加 1。"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将 login_attempts 重置为 0。"""
        self.login_attempts = 0


class Admin(User):
    """有管理权限的用户。"""
 
    def __init__(self, first_name, last_name, username, email, location):
        """初始化管理员。"""
        super().__init__(first_name, last_name, username, email, location)
        # 将权限集初始化为空。
        self.privileges = Privileges()


class Privileges():
    """存储管理员权限的类。"""
    
    def __init__(self, privileges=[]):
       self.privileges = privileges
    
    def show_privileges(self):
       print("\nPrivileges:")
       if self.privileges:
           for privilege in self.privileges:
               print(f"- {privilege}")
       else:
           print("- This user has no privileges.")