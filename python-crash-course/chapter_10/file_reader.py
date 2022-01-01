pi_digits = 'pythonbooks-beginner/python-crash-course/chapter_10/pi_digits.txt'
with open(pi_digits) as file_object:
    lines = file_object.readlines()
print(lines)
for line in lines:
    print(line.rstrip())