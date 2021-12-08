# 9-13
from random import randint

class Die():
    """一个表示骰子的类"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

die_6 = Die()
for i in range(10):
    die_6.roll_die()