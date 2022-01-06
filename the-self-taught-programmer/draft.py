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


list = [1, 2, 3, 4, 5]

while True:
    print("Type 'q' to quit.")
    answer = int(input('猜数字 '))
    if answer == 'q':
        break
    else:
        if answer in list:
            print('right')
        else:
            print('wrong')
