# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

user_input = input("Enter your string: ")
user_symbol = input("Enter the symbol: ")
letter = user_input[0]

print(user_input.replace(letter, user_symbol))