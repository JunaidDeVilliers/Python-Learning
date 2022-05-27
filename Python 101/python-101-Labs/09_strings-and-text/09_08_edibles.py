# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."
flour = s[-9:-4]
egg = s[26:29]
butter = s[-20:-14]
fish = s[-9] + s[-4:-1]
print(flour + " " + egg + " " + butter + " " + fish + ": can make fried fish")
