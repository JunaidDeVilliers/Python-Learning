names = ["Ada", "Bertha", "Carol"]
lowercase_names = [x.lower() for x in names]
print(lowercase_names)
print(names)

# In this code snippet, you define a list called names that contains a few names as strings. 
# In the second line, you're assigning the output of a list comprehension to the variable lowercase_
# names. If you printed the result, you'd see that it consists of a list with the same names in 
# lowercase. In fact, list comprehensions are only one-liner shortcuts for for loops in Python. 
# Anything you can do with a list comprehension, you can also do with a for loop. 
# It just takes you a couple more lines of code