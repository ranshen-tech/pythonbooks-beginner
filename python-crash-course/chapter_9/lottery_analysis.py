# 9-15
from random import choice

def get_winning_ticket(possibilities):
    """摇出中奖组合。"""
    winning_ticket = []
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    """检查彩票的每个数字或字母，只要有一个不在中奖组合中，就返回 False"""
    for element in played_ticket:
       if element not in winning_ticket:
           return False
    return True

def make_random_ticket(possibilities):
    """随机地生成彩票。"""
    ticket = []
    while len(ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in ticket:
            ticket.append(pulled_item)
    return ticket

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)
plays = 0
won = False
max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break
if won:
    print("\nWe have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")