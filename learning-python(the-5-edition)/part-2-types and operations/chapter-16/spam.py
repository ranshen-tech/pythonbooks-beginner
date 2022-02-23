from makeopen import makeopen

makeopen("spam")

F = open("script2.py")
F.read()

makeopen("eggs")
F = open("script2.py")
F.read()
