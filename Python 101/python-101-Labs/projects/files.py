# Import pathlib
# Find the path to my Desktop
# List all the files on there
# Filter for screenshots only
# Create a new folder
# Move the screenshots in there

import pathlib

# pathlib.Path().cwd()  # Prints the path to your current working directory

path = pathlib.Path().cwd() # getting my current path and saving it to a variable

# listing the files in a directory
for filepath in path.iterdir():
    print(filepath.name) # displaying only the file names