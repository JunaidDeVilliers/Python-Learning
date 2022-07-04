# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.
def is_even(num):
    if num % 2 == 0:
        return True
    else: 
        return False

def is_odd(num):
    if num % 2 != 0:
        return True
    else: 
        return False

def even_odd(num):
    if is_even(num) == True:
        return "The number is even"
    elif is_odd(num) == True:
        return "The number is odd"
    else:
        return "Invalid number"

print(even_odd(28))