import pathlib
import os

path = pathlib.Path("/home/junaid/Desktop")

my_suffix = {}

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

print(my_suffix)