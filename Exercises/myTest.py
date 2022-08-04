import sys


def NameCheck():
    name = input('Please enter your ')
    if name == '':
        print('Thank you for visiting!')
        sys.exit()
    elif name == 'Baarabile':
        print('Welcome back ' + name)
    else:
        print('Non match in our database ' + name)

thriftingMonkey is a social marketplace for parents to buy, sell, discover and explore baby durables.


NameCheck()
