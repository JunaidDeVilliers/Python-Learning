# Type hinting was introduced to improve documentation on which data types should be used when calling 
# a function.

# Primarily, type hints are a way to more concisely and unambiguously document your function.

# To add type hints to your function definition, you add the expected type of a parameter after a 
# colon (:). You can also define the expected type of your return value with an arrow (->) at the end 
# of the first line of your function definition:

def greet(greeting: str, name: str) -> str:
    """Generates a greeting."""
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

# There are external packages, such as mypy, that make it possible to enforce static typing in Python. 
# mypy uses the type hints and throws errors if you attempt to pass any data type that contradicts 
# them. By using type hints together with mypy to check your code, you can benefit from some of the 
# advantages of static typing in Python.