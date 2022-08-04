foo = ['Joe', 'Black', 'Khanyi', 'Bugzy']
b = ['man', 'black', 'result', 'okay']


def CommaCode(mylist):
    empty_string = ''
    last = mylist[len(mylist) - 1]
    length = (len(mylist)) - 1
    newList = mylist[0:length]

    for words in newList:
        empty_string = empty_string + words + ' , '

    print(empty_string + ' and ' + last)


CommaCode(foo)
CommaCode(b)
