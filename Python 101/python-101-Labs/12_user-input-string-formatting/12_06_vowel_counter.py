# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

user_input = input("Please enter a word or a sentence: ")

a = 0
e = 0
i = 0
o = 0
u = 0

for letter in user_input:
    if letter == "a":
        a += 1
    elif letter == "e":
        e += 1
    elif letter == "i":
        i += 1
    elif letter == "o":
        o += 1
    elif letter == "u":
        u += 1

print(f"""
A = {a}
E = {e}
I = {i}
O = {o}
U = {u}
""")