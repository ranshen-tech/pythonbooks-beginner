# 简单的逻辑: remember you can go back
from sys import exit

def dead(why):
    print(why, 'Good job!')
    exit(0)

def start():
    print("""
    A forest is in front of you.
    What are you going to do ?
    """)
    
    choice = input(">>> ")
    a = choice.find('straight')
    b = choice.find('back')

    if a != -1:
        dead('You dead in the forest due to the fear.')
    elif b != -1:
        print("Oh yeah! You're smart, fools don't look back.")
        exit(0)
    else:
        dead("You stumble around the room until you starve.")

start()