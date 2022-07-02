# Local Function Scope

# Function-internal variables live only inside the function. You can refer to the function parameters 
# inside your function as much as you want to, but you won't be able to access them outside of it:

def greet(greeting: str, name: str) -> str:
    """Generates a greeting"""
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

# Trying to print the function-internal variable name outside of the function body will throw a 
# NameError. Python doesn't have anything assigned to the variable name in the global scope of your 
# script.

# Function-internal variables can't be re-used outside of the function's scope. To re-use any value 
# generated in the function, you need to squeeze it through the return statement and expose it to 
# your global scope. 
