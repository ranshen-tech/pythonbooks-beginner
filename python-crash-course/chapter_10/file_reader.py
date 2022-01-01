pi_digits = 'pythonbooks-beginner/python-crash-course/chapter_10/pi_digits.txt'
with open(pi_digits) as file_object:
    contents = file_object.read()
print(contents)