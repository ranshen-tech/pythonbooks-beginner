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