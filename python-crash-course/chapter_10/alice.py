filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")