# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist

my_list = randlist
print(f"List: {my_list}")
my_list.sort()
largest = my_list[len(my_list) - 1]
product = 1

for item in my_list:
    product *= item

print("Largest Number: " + str(largest))
print("Product of all numbers: " + str(product))