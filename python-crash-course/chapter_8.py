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


# 8-7-1
def make_album(artist, title):
    """创建一个包含专辑信息的字典"""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)
album = make_album('beethoven', 'ninth symphony')
print(album)
album = make_album('willie nelson', 'red-headed stranger')
print(album)
print()

# 8-7-2
def make_album(artist, title, tracks=0):
    """创建一个包含专辑信息的字典。"""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('metalllica', 'ride the lightning')
print(album)
album = make_album('beethoven', 'ninth symphony')
print(album)
album = make_album('willie nelson', 'red-headed stranger')
print(album)
album = make_album('iron maiden', 'piece of mind', tracks=8)
print(album)


# 8-8
def make_album(artist, title, tracks=0):
    """创建一个包含专辑信息的字典。"""
    album_dict = {
       'artist': artist.title(),
       'title': title.title(),
       }
    if tracks:
       album_dict['tracks'] = tracks
    return album_dict
# 生成提示语。
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "
# 让用户知道如何退出。
print("Enter 'quit' at any time to stop.")
while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    artist = input(artist_prompt)
    if artist == 'quit':
       break
    album = make_album(artist, title)
    print(album)
print("\nThanks for responding!")
print()


# 8-9
def show_messages(messages):
    """打印列表中的所有消息"""
    for message in messages:
        print(message)

messages = ['hello there', 'how are u?', ':)']
show_messages(messages)
print()


# 8-10
def show_messages(messages):
    """打印列表中的所有消息。"""
    print("Showing all messages:")
    for message in messages:
       print(message)

def send_messages(messages, sent_messages):
    """打印每条消息，再将其移到列表 sent_messages 中。""" print("\nSending all messages:")
while messages:
       current_message = messages.pop()
       print(current_message)
       sent_messages.append(current_message)
messages = ["hello there", "how are u?", ":)"]
show_messages(messages)
sent_messages = []
send_messages(messages, sent_messages)
print("\nFinal lists:")
print(messages)
print(sent_messages)