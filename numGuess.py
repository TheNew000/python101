# This is a guess the number game.
import random

guessesTaken = 0

myName = raw_input('Hello! What is your name?  ')

number = random.randint(1, 20)
print('Okay, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken <= 6:
    guess_left = 6 - guessesTaken
    guess_left = str(guess_left)
    guess = input('Take a guess. You have ' + guess_left + ' guesses left!  ')
    guess = int(guess)
    guessesTaken = guessesTaken + 1

    if guess < number:
        if guess >= number - 2:
            print("You're too low but really close!")
        else:
            print('Your guess is too low.')

    if guess > number:
        if guess <= number + 2:
            print("You're too high but really close!")

        else:
            print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    guess_num = str(number)
    print('Good job, ' + myName + '! You guessed my number: (' + guess_num + ') in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)


