# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Junaid De Villiers"
test = "abababababab"

# indexing
# the first index is inclusive and the the last index is exclusive
# if you are indexing from the start of the string then you dont need to include the starting index
# if you are indexing until the end of the string then you dont need to inclue the end index
first_name = name[0:6] # first_name = name[:6]
last_name = name[7:18] # last_name = name[7:]

# step is how much we are increasing our index by during each iteration
# can be used to skip letters

print(first_name)
print(last_name)

#starts at beginning and ends at the end but only prints every second letter
print(test[::2])

# negative step starts at the back
print(test[::-2])

# reversing the string by stepping from the back
print(name[::-1])