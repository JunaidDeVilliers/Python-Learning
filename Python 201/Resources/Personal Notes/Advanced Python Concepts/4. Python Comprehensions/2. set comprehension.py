# You can use set comprehensions with a slight change to the syntax you're used to, by using curly 
# braces ({}) instead of the square brackets:

set_ = {x*2 for x in range(5)}
print(set_)
print(type(set_))

# This code snippet creates a new set() that contains the results of the calculation applied to each 
# number provided by range().