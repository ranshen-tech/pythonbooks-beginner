for row in range(1, 10):
    for col in range(1, 10):
        prod = row * col
        if prod < 10:
            print(' ', end='')
        print(prod, ' ', end='')
    print()

# print(0, 0, 0, 0)
# print(1, 1, 1, 1)
# print('', 2)
# print('', end='')
# print(1, 2)