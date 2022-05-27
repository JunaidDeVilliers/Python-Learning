import string

secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7

#ensuring the cipher remains within range
cipher %= 26

# assigning the alphabet to a string variable
alphabet = string.ascii_lowercase

# shifting the alphabet by the cipher and assigning it to a new variable
# using string slicing to start at the cipher index until the end
# Then adding from the beginning until the cypher index
shifted = alphabet[cipher:] + alphabet[:cipher]

# creating an encryption table with the alphabet on top and the shifted alphabet at the bottom
# will be using this table to encrypt the message
table = str.maketrans(alphabet, shifted)
upper_table = str.maketrans(alphabet.upper(), shifted)

# using the table to translate the normal text into encrypted text (lowercase letters)
encrypted = secret.translate(table)

# using the table to translate the normal text into encrypted text (uppercase letters)
encrypted = encrypted.translate(upper_table)

print(encrypted)