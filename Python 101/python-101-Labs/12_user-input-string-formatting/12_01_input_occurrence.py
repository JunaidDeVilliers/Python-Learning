# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

user_input = input("Enter your string: ")
user_letter = input("Enter the letter: ")

print(user_input.find(user_letter))