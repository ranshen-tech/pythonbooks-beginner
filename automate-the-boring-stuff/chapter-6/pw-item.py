#! python3
# pw-item.py - An insecure password locker program.

PASSWORDS = {
    'email': 'F7min1BDDuvMjuxESSKHFhTxFtjVB6',
    'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
    'luggage': '12345'
    }

import sys
if len(sys.argv) < 2:
    print('Usage: python pw-item.py [account] - copy account password')
    sys.exit()

# first command line arg is the account name
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
