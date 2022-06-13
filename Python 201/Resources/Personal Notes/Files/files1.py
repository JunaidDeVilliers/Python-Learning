# Create or open a file
# Write your data to the file
# Close the file

# First, you need to open a file in write mode:

file_out = open("output.txt", "w")
ages = {"Junaid": 23, "Tauriq": 17, "Tashriq": 13, "Ishaaq": 25}

# In the code snippet above, you're opening a file called output.txt in write mode ("w") and assign 
# that to the variable file_out.

# If there's no file called output.txt in the directory you're running your script from, 
# then it will be created.

# Note: If a file called output.txt already exists, all of its content will be 
# deleted instantly if you open it up in write mode as shown above. 


# After opening the file, you can write data to it using the .write() method on your file_out 
# variable:

file_out.write(str(ages))

# Finally, you should always close the file after you're done working with it, or you might run 
# into unexpected effects.

file_out.close()
