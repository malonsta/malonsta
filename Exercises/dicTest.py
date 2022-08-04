birthdays = {'Khanyi': '26 Sep', 'Bugzy': '27 Apr', 'Small': '18 Apr', 'Tswalis': '17 Apr'}

while True:
    print('Please enter your name ')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthdate for ' + name)

    else:
        print('Birthday not found')
        print('when is their birthday')

    bday = input()
    birthdays[name] = bday

    print('database updated!')

