#! python3
# A program help me remember password

import sys
import pyperclip

Password = {'email':'*#061#', 'blog':'aabbdde', 'luggage':'dkstFeb.1st'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]
if account in Password:
    pyperclip.copy(Password[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

