# Open an existing file
# Read the data from the file
# Close the file

# First, you have to open the file. This time, you'll use the default read mode ("r"):

file_in = open("filecounts.txt", "r")

# After creating a file object in read mode, you can use .read() to read the entire content of your 
# file into memory:

contents = file_in.read()
file_in.close()


# This line of code saves the content of your file in the variable contents.

print(contents)
print(type(contents))