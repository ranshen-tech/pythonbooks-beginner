# 2-2
msg = "I love learning to use Python."
print(msg)

msg = "It's really satisfying!"
print(msg)


# 2-5
print('Albert Einstein once said, "a person who never made a mistake')
print('never tried anything new."')


# 2-7
name = "\tRan Shen\n"
print('Unmodified:')
print(name)

# 这种删除只是暂时的
print('Using lstrip:')
print(name.lstrip())

print('Using rstrip:')
print(name.rstrip())

print('\nUsing strip:')
print(name.strip())


# 2-9
favourite_number = 9
message = f"\nMy favourite_number is {favourite_number}."

print(message)