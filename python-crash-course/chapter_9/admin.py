# 9-12
"""一系列模拟管理员的类。"""

from user import User

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