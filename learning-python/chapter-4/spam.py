import random
print(random.random())
print(random.choice([1, 2, 3, 4]))

line = 'aaa,bbb,ccccc,dd'
print(line.split(','))

S = 'spam'
print(S.upper())
print(S.isalpha())
print(S.isdigit())

line = 'aaa,bbb,ccccc,dd\n'
print(line)
print(line.rstrip())
print(line.rstrip().split(','))

print('%s, eggs, and %s' % ('spam', 'Spam!'))
print('{0}, eggs, and {1}'.format('spam', 'Spam!'))
print('{}, eggs, and {}'.format('spam', 'Spam!'))
print('{:,.2f}'.format(3.1415926))

# print(dir(str))
# print(help(str.replace))

S = 'A\nB\tC'
print(S)
print(len(S))
print(ord('\n'))
S = 'A\0B\0C'
print(S)
print(len(S))

msg = """
aaaaaaaaa
bbb'''bbbbbb""bbbbbbb'bbbb
cccccccccc
"""
print(msg)

M = ['bb', 'aa', 'cc']
M.sort()
print(M)
M.reverse()
print(M)

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

col = [row[1] for row in M]
print(col)
print([row[1] + 1 for row in M])
print([row[1] for row in M if row[1] % 2 == 0])

diag = [M[i][i] for i in [0, 1, 2]]
print(diag)

doubles = [c * 2 for c in 'spam']
print(doubles)

print(list(range(4)))
print(list(range(-6, 7, 2)))

print([[x ** 2, x ** 3] for x in range(4)])
print([[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0])

G = [sum(row) for row in M]
print(G)