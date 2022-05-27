import pathlib


import pathlib

num = 1
path = pathlib.Path('/home/junaid/Desktop/screenshots')

for filepath in path.iterdir():
    extension = filepath.suffix

    new_name = f"screenshot {str(num) + extension}"
    num += 1
    filepath.rename(pathlib.Path(path, new_name))
