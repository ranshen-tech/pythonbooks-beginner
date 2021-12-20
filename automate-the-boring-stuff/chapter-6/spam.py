# 6-1-4 原始字符串
print(r'That is Carol\'s cat.')


# 6-2-2 isX 字符串方法
print('hello'.isalpha())
print('hello123'.isalnum())
print('123'.isdecimal())
print(' '.isspace())
print('This Is NOT Title Case Eigher'.istitle())


# 6-2-3 startswith()和 endswith()
print('Hello world!'.startswith('Hello'))
print('Hello world!'.endswith('world!'))
print('abc123'.startswith('abcdefg'))
print('abc123'.endswith('12'))
print('Hello world!'.startswith('Hello world!'))
print('Hello world!'.endswith('Hello world!'))


# 6-2-4 字符串方法 join()和split()
print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Ranshen']))
print('ABC'.join(['My', 'name', 'is', 'Ranshen']))

print('My name is Ranshen'.split())
print('MyABCnameABCisABCRanshen'.split('ABC'))
print('My name is Ranshen'.split('m'))
print('Remember,remember,the fifth of November.'.split())

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''
print(spam.split('\n'))


# 6-2-5 用 rjust()、ljust()和 center()方法对齐文本
print('Hello'.rjust(10, '*'))
print('Hello'.rjust(20))
print('Hello World'.rjust(20))
print('Hello'.ljust(10, '-'))
print('Hello'.center(20))
print('Hello'.center(20, '='))

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('pmSa'))