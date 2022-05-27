# Import pathlib
# Find the path to my Desktop
# List all the files on there
# Filter for screenshots only
# Create a new folder
# Move the screenshots in there

import pathlib

#creating a specific path object
path = pathlib.Path("/home/junaid/Desktop")

# making a new folder
new_path = pathlib.Path('/home/junaid/Desktop/screenshots')
new_path.mkdir(exist_ok=True) # creates the directory if it does not already exist

# getting the suffix.png
for filepath in path.iterdir():
    if filepath.suffix == ".png":
        # Create a new path for each file
        new_filepath = new_path.joinpath(filepath.name)
        # Move the screenshot there
        filepath.replace(new_filepath)