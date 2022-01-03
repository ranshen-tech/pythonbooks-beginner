# 10-3
name = input("What's your name? ")
filename = 'pythonbooks-beginner/python-crash-course/chapter_10/guest.txt'
with open(filename, 'w') as f:
    f.write(name)