# 9-13
from random import randint

class Die():
    """一个表示骰子的类"""

    def __init__(self, sides=6):
        """初始化骰子"""
        self.sides = sides

    def roll_die(self):
        """返回一个位于 1 和骰子面数之间的随机数。"""
        return randint(1, self.sides)

# 移到my_die.py文件中

# # 创建一个 6 面的骰子，再掷 10 次并显示结果。
# d6 = Die()

# results = []
# for roll_num in range(10):
#     result = d6.roll_die()
#     results.append(result)
# print("\n10 rolls of a 6-sided die:")
# print(results)