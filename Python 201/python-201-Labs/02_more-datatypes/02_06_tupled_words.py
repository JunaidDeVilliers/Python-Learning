# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]


input = input("Enter a sentence: ").split()
result_list = []

for i in input:
    result_list.append(tuple(i))

print(result_list)