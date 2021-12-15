def string(lists):
    strings = ''
    for index in range(len(lists)):
        if index == len(lists) - 2:
            strings += lists[index] + ', and '
        elif index < len(lists) - 2:
            strings += lists[index] + ', '
        else:
            strings += lists[index]
    return strings
 
span = []
print('请输入字符(以end结束):')
while True:
    s = input()
    if s == 'end':
        break
    else:
        span.append(s)
print(string(span))