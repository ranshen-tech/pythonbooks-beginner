# challenge1
shows = ["The Walking Dead", "Entourage", "The Sopranos","TheVampire Diaries"]

for show in shows:
    print(show)


# challenge2
for i in range(25, 51):
    print(i)


# challenge3
for i, show in enumerate(shows):
    print(i, show)


# challenge4
numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Guess a number or type 'q' to quit. ")
    if answer == 'q':
        break
    try:
        answer = int(answer)
    except ValueError:
        print("Please type a number or 'q' to quit.")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")


# challenge5
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
multiply = []

for i in list1:
    for j in list2:
        multiply.append(i * j)

print(multiply)


# challenge6