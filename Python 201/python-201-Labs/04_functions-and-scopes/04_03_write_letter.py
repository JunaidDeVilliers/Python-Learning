# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.


def write_letter(name, text):
    greeting = f"Hello {name}! "
    goodbye = f" Goodbye {name}!"

    return greeting + text + goodbye

print(write_letter("Junaid", "I am pleased to inform you that you have been accepted for the job"))