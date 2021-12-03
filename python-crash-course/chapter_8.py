# 8-1
def display_message():
    msg = "I'm learning to store code in functions."
    print(msg)

display_message()
print()


# 8-2
def favourite_book(title):
    """显示一条消息，
    指出喜欢的一本图书。
    """
    print(f"{title} is one of my favourite books.")

favourite_book('Python Crash Course')


# 8-3
def make_shirt(size, message):
    """概述要制作的T恤什么样。"""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f"It will say, '{message}'")

make_shirt('large', 'I love Python!')
make_shirt(message="Readability counts.", size='medium')


# 8-4
def make_shirt(size='large', message='I love Python!'):
    """概述要制作的T恤什么样。"""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f"It will say, '{message}'")

make_shirt()
make_shirt('medium')
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')
print()

# 8-5
def describe_city(city, country='chile'):
    """描述城市。"""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city(('santiago'))
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')
print()

# 8-6
def city_country(city, country):
    """返回一个类似于'Santiago, Chile'的字符串"""
    return f"{city.title()}, {country.title()}"

city = city_country('santiago', 'chile')
print(city)
city = city_country('ushuaia', 'argentina')
print(city)
city = city_country('longyearbyen', 'svalbard')
print(city)
print()


# 8-7