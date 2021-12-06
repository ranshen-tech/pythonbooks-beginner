# 9-1
class Restaurant():
    """一个表示餐馆的类。"""

    def __init__(self, name, cuisine_type):
        """初始化餐馆。"""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """显示餐馆信息摘要。"""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """显示一条消息，指出餐馆正在营业。"""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2
class Restaurant():
    """一个表示餐馆的类。"""

    def __init__(self, name, cuisine_type):
        """初始化餐馆。"""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """显示餐馆信息摘要概述。"""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """显示一条消息，指出餐馆正在营业。"""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

mean_queen = Restaurant('the mean queen', 'pizza')
mean_queen.describe_restaurant()

ludvigs = Restaurant("ludvig's bistro", 'seafood')
ludvigs.describe_restaurant()

mango_thai = Restaurant('mango thai', 'thai food')
mango_thai.describe_restaurant()


# 9-3
class User():
    """一个表示用户的简单类。"""

    def __init__(self, first_name, last_name, username, email, location):
        """初始化用户。"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """显示用户信息摘要。"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")

    def greet_user(self):
        """向用户发出个性化的问候。"""
        print(f"\nWelcome back, {self.username}!")

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()


# 9-4
class Restaurant():
    """一个表示餐馆的类。"""

    def __init__(self, name, cuisine_type):
        """初始化餐馆。"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """显示餐馆信息摘要。"""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")
    
    def open_restaurant(self):
        """显示一条消息，指出餐馆正在营业。"""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """让用户能够设置就餐人数。"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """让用户能够增加就餐人数。"""
        self.number_served += additional_served

restaurant = Restaurant('the mean queen', 'pizza')

restaurant.describe_restaurant()
print(f"\nNumber served: {restaurant.number_served}")

restaurant.number_served = 430
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(1257)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(239)
print(f"Number served: {restaurant.number_served}")


# 9-5
class User():
    """一个表示用户的简单类。"""

    def __init__(self, first_name, last_name, username, email, location):
        """初始化用户."""
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

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print(f" Login attempts: {eric.login_attempts}")

print("Resetting login attempts...")
eric.reset_login_attempts()
print(f" Login attempts: {eric.login_attempts}")


# 9-6
class Restaurant():
    """一个表示餐馆的类。"""

    def __init__(self, name, cuisine_type):
        """初始化餐馆。"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """显示餐馆信息摘要。"""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """显示一条消息，指出餐馆正在营业。"""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """让用户能够设置就餐人数。"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """让用户能够增加就餐人数。"""
        self.number_served += additional_served
 
 
class IceCreamStand(Restaurant):
    """一个表示冰激凌小店的类。"""

    def __init__(self, name, cuisine_type='ice_cream'):
        """初始化冰激凌小店。"""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """显示出售的冰激凌品种。"""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
           print(f"- {flavor.title()}")

big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()


# 9-7
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
        self.privileges = []

    def show_privileges(self):
        """显示当前管理员的权限。"""
        print("\nPrivileges:")
        for privilege in self.privileges:
           print(f"- {privilege}")

eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')

eric.describe_user()

eric.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.show_privileges()


# 9-8
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
    """一个存储管理员权限的类。"""
    
    def __init__(self, privileges=[]):
       self.privileges = privileges
    
    def show_privileges(self):
       print("\nPrivileges:")
       if self.privileges:
           for privilege in self.privileges:
               print(f"- {privilege}")
       else:
           print("- This user has no privileges.")

eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')

eric.describe_user()
eric.privileges.show_privileges()

print("\nAdding privileges...")

eric_privileges = [
    'can reset passwords',
    'can moderate discussions', 
    'can suspend accounts',
    ]

eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()

