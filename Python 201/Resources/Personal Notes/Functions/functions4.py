# Adding **kwargs to your function definition has a similar effect to *args. However, Python packages 
# up your arguments in a mapping instead.

# This means that you need to pass the arguments as keyword arguments, and access them in your 
# function body as you would with a dictionary:

def print_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

print_kwargs(country='ukraine', city='odessa')