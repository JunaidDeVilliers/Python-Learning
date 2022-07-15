# Lambda expressions, also called anonymous functions, allow you to define small functions in a 
# single line of code. They can make your code more concise.

def square_root(x):
    return x**2

# In the code snippet above, you defined a function, square_root() that takes an integer, x, as 
# its argument and returns that number squared.

# You can write the same logic in a one-liner lambda expression:

squared = lambda x: x**2

# In both cases, you've defined a function object, square_root and squared respectively, that you can 
# call with a number as an argument to get the same results:

print(square_root(4))
print(squared(4))
