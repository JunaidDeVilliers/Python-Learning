import pathlib
import os
import csv

my_suffix = {}

path = pathlib.Path("/home/junaid/Desktop")
csv_path = pathlib.Path("/home/junaid/Desktop/Python/Python 201/python-201-Labs/projects/File Counter")

if csv_path.joinpath("my_data.csv").is_file():
    with open(csv_path.joinpath('my_data.csv'), mode='r') as inp:
        reader = csv.reader(inp)
        my_suffix = {rows[0]:int(rows[1]) for rows in reader}
else:
    with open(csv_path.joinpath('my_data.csv'), 'w') as f:
        for key in my_suffix.keys():
            f.write("%s, %s\n" % (key, my_suffix[key]))

new_path = pathlib.Path('/home/junaid/Desktop/images')
new_path.mkdir(exist_ok=True)

for filepath in path.iterdir():
    if os.path.isdir(filepath):
        continue
    else:
        if filepath.suffix in my_suffix:
            new_path = pathlib.Path(f'/home/junaid/Desktop/images/({filepath.suffix})')
            new_path.mkdir(exist_ok=True)
            new_filepath = new_path.joinpath(filepath.name)
            filepath.replace(new_filepath)
            my_suffix[filepath.suffix] += 1
        else:
            new_path = pathlib.Path(f'/home/junaid/Desktop/images/({filepath.suffix})')
            new_path.mkdir(exist_ok=True)
            new_filepath = new_path.joinpath(filepath.name)
            filepath.replace(new_filepath)
            my_suffix[filepath.suffix] = 1

with open(csv_path.joinpath('my_data.csv'), 'w') as f:
        for key in my_suffix.keys():
            f.write("%s, %s\n" % (key, my_suffix[key]))

print(my_suffix)