# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

import pathlib

path = pathlib.Path("/home/junaid/Desktop/Python/Python 201/python-201-Labs/03_file-input-output/words.txt")

with open(path, "r") as f_in:
    for line in f_in.readlines():
        if len(line) > 20:
            print(line)