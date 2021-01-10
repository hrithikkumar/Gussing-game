'''
Number Gussing game.py
Designed by: Hrithik Kumar

'''
import random
guessTaken = 0
print('Hello! What is your name')
name = input()
number = random.randint(1, 20)
print('Well, '+name+', I am Thinking of a number between 1 and 20')
while guessTaken < 6 :
    print('Take a Guess.')
    guess = input()
    guess = int(guess)
    guessTaken = guessTaken + 1
    
    if guess < number :
        print('Your guess is too low.')
    if guess > number :
        print('Your guess is too high.')
    if guess == number :
        break
if guess == number :
    guessTaken = str(guessTaken)
    print('Good Job, ' +name+ '! You guessed my nuber in ' +guessTaken+ ' guesses')
    
    if guess != number:
        number = str(number)
        print('Nope. The number i was thinking of was' +number)

