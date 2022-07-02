# args stands for arguments
# kwargs stands for keyword arguments

# The syntax that actually provides the functionality of this feature are the asterisks (* and **).

# When you define a function, you can prefix a parameter name, e.g. args and kwargs, with the 
# asterisks. By doing this, you implement a language feature that allows your function to now take 
# arbitrary amounts of arguments.

# If you add *args as a parameter to your function definition, it will package all passed arguments 
# into a collection. You can then access each item like you would in a normal list. More commonly, 
# however, you'll just iterate over all items in args:

def print_args(*args):
    for a in args:
        print(a)

print_args("barcelona", "tahoe", "ubud", "koh tao")
