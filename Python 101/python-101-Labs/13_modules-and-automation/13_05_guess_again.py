# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random
import sys

num = random.randint(1, 10)
guess = None
chances = 3

while guess != num:
    guess = input("Enter a number between 1 and 10: ")
    guess = int(guess)
    chances -= 1

    if guess == num:
        print("Congradulations, you have guessed correctly!")
        sys.exit()
    elif chances == 0:
        print("Sorry game over!")
        sys.exit()
    elif guess > num:
        print("Guess lower")
        print("Chances left: " + str(chances))
    elif guess < num:
        print("Guess higher")
        print("Chances left: " + str(chances))
    else:
        print("Unkwon Error!!!")
        sys.exit()