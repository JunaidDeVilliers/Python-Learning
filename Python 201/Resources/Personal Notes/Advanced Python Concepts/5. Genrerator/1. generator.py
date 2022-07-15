# In the previous lesson, you got to know the syntax of Python comprehensions. In generator objects, 
# you might encounter an extremely similar construct that behaves a bit differently:

generator = (x*2 for x in range(5))
print(generator)
print(type(generator))

# The only syntactic difference to a list comprehension is the different types of parentheses used. 
# Generators wrap the code logic in round parentheses (()).

# However, when you look at the output, you might be surprised. You don't seem to be able to look 
# into the generator object, and you can see that it created neither a set() nor a list(), but 
# something called a 'generator'.

# Python generators allow you to work with iterables in a more memory-effective way than if you 
# were using a list comprehension. When you write a list comprehension, it actually creates a new 
# list, which is an object that contains multiple other objects:

# When Python creates a list object, it needs to assign computer memory in order to be able 
# to store it somewhere. If you're working with huge lists, this can potentially become an issue.

# A generator on the other hand is only a single generator object. It doesn't hold any references 
# to other objects that take up memory themselves. Instead, the generator only yields each item of 
# the iterable once, while it's needed, and then dumps it into oblivion:

# Generators are slower in execution because when a single iterator should be addressed, the item 
# first needs to be created. However, they are much quicker to create because there's no huge list 
# object with thousands of items in it that needs to be built.

# In order to actually create and work with the items whose potential existence the generator 
# contains, you'll have to iterator over the generator object:

for i in generator:
    print(i)