print("""
Welcome to the Jimmy's World!
In there, you will have an unforgettable adventure.
There have two doors(1/2) in front of you.
So, let's choose the door.
""")
 
prompt = ">>> input the door number :"
door = input(prompt)
 
if door == "1":
    print("You lose.")
    
elif door == "2":
    print("You lose.")
   
else:
    print("You win.")
    print("It's very unforgettable!n isn't it ???")