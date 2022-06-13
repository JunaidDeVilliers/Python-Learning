# When you're working with files, you might often run into some unexpected errors. Sometimes the 
# contents of the file are not what you expect or the file doesn't even exist at all. You want to be 
# sure that the file object you opened will be closed in any case. You can achieve this by using a 
# context manager when opening the file:

with open("filecounts.txt", "r") as file_in:
    print(file_in.read())

# Using the above construct with the with keyword, which is called a context manager, you'll 
# automatically close the file object after the indented part of your code is done running.