import pathlib
import csv
# import os


my_suffix = {}
csv_path = pathlib.Path("/home/junaid/Desktop/Python/Python 201/python-201-Labs/projects/File Counter")

if csv_path.joinpath("my_data.csv").is_file():
    with open(csv_path.joinpath('my_data.csv'), mode='r') as inp:
        reader = csv.reader(inp)
        my_suffix = {rows[0]:rows[1] for rows in reader}
else:
    with open(csv_path.joinpath('my_data.csv'), 'w') as f:
        for key in my_suffix.keys():
            f.write("%s, %s\n" % (key, my_suffix[key]))

print(my_suffix)

# my_dictionary = {'values': 678, 'values2': 167, 'values6': 998}


with open(csv_path.joinpath('test6.csv'), 'w') as f:
        for key in my_suffix.keys():
            f.write("%s, %s\n" % (key, my_suffix[key]))

print(my_suffix)




