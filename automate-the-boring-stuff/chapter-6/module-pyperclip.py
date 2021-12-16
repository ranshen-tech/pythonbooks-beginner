import pyperclip

pyperclip.copy('Hello world!')
print(pyperclip.paste())
print(pyperclip.paste())

message = 'for example, if I copied this sentence to the clipboard and then called paste(), it would look like this:'
pyperclip.copy(message)
print(pyperclip.paste())