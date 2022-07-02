# Docstrings are special comments that describe functions, classes, and methods in Python.

# The rationale for docstrings is to help to know how to work with your functions. Docstrings should 
# describe at least three aspects of your function:
#     what it does
#     what arguments it takes
#     what it returns

# Docstrings have a specific syntax that you need to follow, and additionally there exist a couple of 
# conventions on how to write good docstrings. The two essential aspects of a docstring are:
#     Use triple-double quotes (""") to begin and end a docstring.
#     Write it starting at the first line of your function body.

def greet(greeting, name):
    """Generates a greeting.

    Args:
        greeting (str): The greeting to use, e.g. "Hello"
        name (str): The name of the person you want to greet

    Returns:
        str: A personalized greeting message
    """
    sentence = f"{greeting}, {name}! How are you?"
    return sentence
