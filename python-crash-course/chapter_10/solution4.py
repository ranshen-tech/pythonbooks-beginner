# 10-4
filename = 'pythonbooks-beginner/python-crash-course/chapter_10/guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
       with open(filename, 'a') as f:
           f.write(f"{name}\n")
       print(f"Hi {name}, you've been added to the guest book.")