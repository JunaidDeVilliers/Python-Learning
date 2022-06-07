# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)

# Write your code below here


my_new_list = []
temp = []
randlist.sort()

if len(randlist) % 2 != 0:
    randlist.append(0)


for i in range(len(randlist)):
    if i % 2 != 0 and i > 0:
        temp.append(randlist[i])
        temp = tuple(temp)
        my_new_list.append(temp)
        temp = list(temp)
        temp = []
    else:
        temp.append(randlist[i])
        temp = tuple(temp)
        temp = list(temp)

print(my_new_list)