# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

string = input("Enter text: ")
word = ""
check = True

for letter in string:
    if check == True:
        word += letter.lower()
        check = False
    else:
        word += letter.upper()
        check = True

print(word)