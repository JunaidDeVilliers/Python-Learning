# Dictionaries are iterable mappings, which means that you can iterate over them similar to how you 
# would with a collection, such as a string, a tuple, a list, or a set. However, because dictionaries 
# consist of keys and values, you'll need to tackle iteration a bit differently:

users = {'mary': 22, 'caroline': 99, 'harry': 20}

for user, age in users.items():
    print(user, age)

# The dict.items() method gives you a list of tuple objects that you can iterate over.