#Game where player must guess the number.
import random
print('Hi! What is your name?')
name = input()
secretNumber = random.randint(1, 25)
print('Well, ' + name + ', I am thinking of a number between 1 and 25, can you figure it out?')

#Asks the player to guess 4 times.
for guessesTaken in range(1, 6):
    print('Take a guess.')
    guess = int(input())
    if guess > 25:
        print('You are out of the range bud!')
    elif guess < secretNumber:
        print('You are too low!')
    elif guess > secretNumber:
        print('You are too high!')
    else:
        break # This condition is the right guess

if guess == secretNumber:
    print('Hooray ' + name + '! You guessed my number in ' + str(guessesTaken) + " attempts.")
else:
    print('Too bad ' + name + ', my number was ' + str(secretNumber))
