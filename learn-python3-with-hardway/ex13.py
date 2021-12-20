from sys import argv
# read the WYSS section for how to run this
script, weight = argv
name = input("what's your name: ")
age = input("how old are you: ")
# name = input("what's your name: ")
print(f"\nThe script is called: {script}")
print(f"Your name is: {name}")
print(f"Your age is: {age}")
print("Your weight is:", weight)