message = 'It was a bright could day in April,'
message += 'and the clocks were striking thirteen.'

count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)