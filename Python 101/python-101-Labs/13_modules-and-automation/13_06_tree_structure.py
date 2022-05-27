# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import pathlib

path = pathlib.Path("/home/junaid/Desktop/Python/Python 101/python-101-Labs/11_conditionals-and-loops")

for filepath in path.iterdir():
    if filepath.suffix == ".py":
        print(filepath.name)