# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.

import sys

num = 1

while 1 == 1:
    print("Loop " + str(num))
    num += 1

    quit = input("enter quit to stop the loop: ")
    
    if quit == "quit":
        sys.exit()