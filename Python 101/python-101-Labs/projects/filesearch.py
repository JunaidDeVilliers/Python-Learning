# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.

import pathlib
import os

path = pathlib.Path('/home/junaid/Desktop')

for filepath in path.iterdir():
    if os.path.isdir(filepath) == True:
        new_path = path.joinpath(filepath.name)

        for new_filepath in new_path.iterdir():
            if new_filepath.suffix == ".png": # making png because i have no jpg
                print(f"{new_filepath.name} from the {new_filepath.parent.name} folder")
    elif os.path.isfile(filepath) == True:
        print(f"{filepath.name} from the {filepath.parent.name} folder")