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

G = (sum(row) for row in M)
print(next(G))
print(next(G))
print(next(G))

print(list(map(sum, M)))

print({sum(row) for row in M})
print({i : sum(M[i]) for i in range(3)})

print([ord(x) for x in 'spaam'])
print({ord(x) for x in 'spamm'})
print({x : ord(x) for x in 'spamm'})
print((ord(x) for x in 'spamm'))


# 字典
# 映射操作
D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D['food'])
D['quantity'] += 1
print(D)

D = {}
D['name'] = 'Bob'
D['job'] = 'dev'
D['age'] = 40
print(D)
print(D['name'])

bob1 = dict(name = 'Bob', job = 'dev', age = 40)
print(bob1)
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print(bob2)

# 重访嵌套
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'job': ['dev', 'mgr'],
       'age': 40.5}
print(rec['name'])
print(rec['name']['last'])
print(rec['job'])
print(rec['job'][-1])
rec['job'].append('janitor')
print(rec)

rec = 0
print(rec)

# 不存在的键: if测试
D = {'a': 1, 'b': 2, 'c': 3}
print(D)
D = dict(a = 1, b = 2, c = 3)
print(D)
D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(D)
D['e'] = 99
print(D)