#! python3
# A program help me remember password

import sys
import pyperclip
import hashlib

passwd = hashlib.md5()
passwdtxt = ''
passwdmd5 = ''
try:
    passwdfile = open('passwd.dat', 'r')
    passwdmd5 = passwdfile.read()
    if len(passwdmd5) != 32:
        raise IOError
except:
    passwdtxt = input('Please enter a new password:')
    passwd.update(passwdtxt.encode())
    passwdmd5 = passwd.hexdigest()
    passwdfile = open('passwd.dat', 'w')
    passwdfile.write(passwdmd5)
else:
    for i in range(3):
        passwdtxt = input('Please enter your password:')
        passwd.update(passwdtxt.encode())
        if passwdmd5 != passwd.hexdigest():
            print('Wrong passwd! Please try again.')
    else:
        print("You've tried three times.")
        sys.exit()

cmd = input('Please enter your command:')

'''
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
'''
