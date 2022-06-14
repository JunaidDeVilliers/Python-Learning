import pathlib

path = pathlib.Path("/home/junaid/Desktop/Python/Python 201/Resources")

with open(path.joinpath("output.txt"), "r") as file_in:
    print(file_in.read())

