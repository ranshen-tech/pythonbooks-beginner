questions = ["What's your name? ",
             "What's your favourite color? ",
             "What's your quest? "]

n = 0
while True:
    print("type 'q' to quit.")
    answer = input(questions[n])
    if answer == 'q':
        break
    n = (n + 1) % 3