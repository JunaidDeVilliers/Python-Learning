# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

# list_ = set(list_)
# print(list_)

list_new = []

for i in list_:
    if i in list_new:
        continue
    else:
        list_new.append(i)

print(list_new)
