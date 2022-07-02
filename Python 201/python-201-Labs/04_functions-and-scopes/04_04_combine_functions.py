# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(greeting: str, name: str) -> str:
    """Generates a greeting"""
    sentence = f"{greeting}, {name}! How are you? "
    return sentence

def write_letter(name, text):
    goodbye = f" Goodbye {name}!"

    return greet("Hello", name) + text + goodbye

print(write_letter("Junaid", "I am pleased to inform you that you have been accepted for the job"))
