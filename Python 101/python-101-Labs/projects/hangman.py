# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script

# Print an explanation to the user

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it

word = "hello"
attempts = len(word) * 2
masked_word = ""
user_guess = ""
pointer = 0
won = False

for letter in word:
    masked_word += "_"

while attempts > 0:
    if masked_word == word:
        won = True
        break

    while len(user_guess) != 1:
        user_guess = input("Please enter a single character guess: ")

    for letter in word:
        if user_guess == letter:
            masked_word = masked_word[:pointer] + letter + masked_word[pointer + 1:]
        pointer += 1

    pointer = 0
    print(masked_word)
    attempts -= 1
    user_guess = ""
    print(f"Tries left: {attempts}")

if won == True:
    print(f"Congradulations, you have won. The word was {word}")
else:
    print(f"Game Over! The correct word was {word}")
