# 10-9
filenames = [
    'pythonbooks-beginner/python-crash-course/chapter_10/cats.txt',
    'pythonbooks-beginner/python-crash-course/chapter_10/dogs.txt'
    ]

for filename in filenames:

    try:
       with open(filename) as f:
           contents = f.read()
    
    except FileNotFoundError:
        pass
    
    else:
        print(f"\nReading file: {filename}")
        print(contents)