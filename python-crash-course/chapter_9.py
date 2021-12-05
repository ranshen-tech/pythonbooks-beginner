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