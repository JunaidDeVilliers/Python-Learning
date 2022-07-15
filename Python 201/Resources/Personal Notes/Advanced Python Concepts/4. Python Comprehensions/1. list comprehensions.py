# Python comprehensions are a concise way of writing some code logic that you could also express in a 
# for loop.

list_ = [x*2 for x in range(5)]
print(list_) 
print(type(list_))

# The list comprehension allows you to encode the logic you'd otherwise apply in a for loop into a 
# single line of code. In the example above, you're multiplying each number provided by the range() 
# object by 2, and you end up with a new list object containing the results.

