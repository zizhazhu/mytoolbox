#! python3
# A program help me remember password

import sys
import pyperclip
import hashlib

# ppnn13%
token = '31c3efd94dcbaf23a7b2faa497d58a99'

Password = {'email':'*#061#', 'blog':'aabbdde', 'luggage':'dkstFeb.1st'}

if len(sys.argv) < 3:
    print('Usage: python pw.py [account] [password] - copy account password')
    sys.exit()

md5passwd = hashlib.md5(sys.argv[2].encode())
if md5passwd.hexdigest() != token:
    print('Wrong password!')
    sys.exit()

account = sys.argv[1]
if account in Password:
    pyperclip.copy(Password[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

