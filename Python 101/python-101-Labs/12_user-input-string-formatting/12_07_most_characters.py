# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

string_1 = input("Enter your first string: ")
string_2 = input("Enter your second string: ")
string_3 = input("Enter your third string: ")
longest_string = None

if len(string_1) > len(string_2):
    if len(string_1) > len(string_3):
        print(len(string_1),string_1)
    else:
        print(len(string_3),string_3)
else:
    if len(string_2) > len(string_3):
        print(len(string_2),string_2)
    else:
        print(len(string_3),string_3)