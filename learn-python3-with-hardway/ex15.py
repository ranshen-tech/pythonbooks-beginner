from sys import argv

script, filename = argv
txt = open(filename)

print(f"\nHere's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input(">>> ")
txt_again = open(file_again)

print(txt_again.read())


# consolidation exercise5
# filename = input("Type the filename: ")
# txt = open(filename)

# print(txt.read())
# txt.close()