def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

question = int(input('input a integer: '))
a = collatz(question)
a = collatz(a)
a = collatz(a)
a = collatz(a)
a = collatz(a)
a = collatz(a)
a = collatz(a)