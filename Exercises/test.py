import random

print('Welcome to the guessing game')

secretNumber = random.randint(1, 20)

for guessing in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess > secretNumber:
        print('your guess is to high')

    elif guess < secretNumber:
        print('your guess is to low')

    else:
        break

if guess == secretNumber:
    print('your guessed the number in' + str(guess))

else:
    print('wrong the secret number is' + str(secretNumber))
