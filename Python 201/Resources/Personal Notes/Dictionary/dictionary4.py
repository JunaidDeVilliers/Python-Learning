# You can also iterate over only the keys or only the values in a dictionary. In fact, if you 
# directly iterate over a dictionary without calling a method, such as .items() on it, Python will 
# iterate over the dictionary's keys:

users = {'mary': 22, 'caroline': 99, 'harry': 20}

for k in users:
    print(k)

# OUTPUT:
# mary
# caroline
# harry

# Alternatively, you can use the the distinct dictionary method .keys() to iterate over just the keys:

users = {'mary': 22, 'caroline': 99, 'harry': 20}

for k in users.keys():
    print(k)

# OUTPUT:
# mary
# caroline
# harry

# And if you need to access all values in a dictionary, you'll need to use .values():

users = {'mary': 22, 'caroline': 99, 'harry': 20}

for v in users.values():
    print(v)

# OUTPUT:
# 22
# 99
# 20

# As you can see, dict.keys() allows you to iterate over only the keys of your dictionary, while dict.
# values() allows you to access all the values.