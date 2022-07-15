# Another comprehension you might encounter is the dictionary comprehension. Its syntax is slightly 
# more involved, just like its for loops are. This is necessary because of the different structure of 
# dictionaries:

dict_1 = {"a": 1, "b": 2}
dict_2 = {k: v*2 for (k, v) in dict_1.items()}
print(dict_2)
print(type(dict_2))