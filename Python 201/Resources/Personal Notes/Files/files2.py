# You can open file objects in different modes. You've opened it in write mode ("w"), which always 
# starts with a blank slate.

# Instead, you can use the append mode ("a") to add new data to an existing file:

file_out = open("filecounts.txt", "a")  # 'append' mode

# The rest of your code stays the same. If you now run your script a second time, you'll see that 
# Python added a new dictionary at the end of the file:
ages = {"Junaid": 23, "Tauriq": 17, "Tashriq": 13, "Ishaaq": 25}

file_out.write(str(ages))
file_out.write("\n") # Include a line break
file_out.close()
