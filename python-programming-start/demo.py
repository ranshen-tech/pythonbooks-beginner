from random import choice

def get_winning_ticket(possibilities):
    winning_ticket = []
    while len(winning_ticket) < 3:
        pulled_item = choice(possibilities)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    for element in played_ticket:
       if element not in winning_ticket:
           return False
    return True

def make_random_ticket(possibilities):
    my_ticket = []
    while len(my_ticket) < 3:
        pulled_item = choice(possibilities)
        if pulled_item not in my_ticket:
            my_ticket.append(pulled_item)
    return my_ticket

possibilities = [1, 2, 3, 'a', 'b', 'c']
winning_ticket = get_winning_ticket(possibilities)
plays = 0
won = False
max_tries = 10

while not won:# True
    my_ticket = make_random_ticket(possibilities)
    won = check_ticket(my_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break
if won:
    print("\nWe have a winning ticket!")
    print(f"Your ticket: {my_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {my_ticket}")
    print(f"Winning ticket: {winning_ticket}")