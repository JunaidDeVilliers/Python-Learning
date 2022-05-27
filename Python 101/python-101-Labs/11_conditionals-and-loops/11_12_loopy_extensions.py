# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"
word = ""
check = False

for letter in filename:
    if letter == ".":
        check = True
    elif check == True:
        word += letter

if word == "pdf":
    print("This is a pdf file")
else:
    print("This is not a pdf file")