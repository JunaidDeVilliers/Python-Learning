# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

import pathlib

words = []
path = pathlib.Path("/home/junaid/Desktop/Python/Python 201/python-201-Labs/03_file-input-output")
file_out = open(path.joinpath("words_reverse.txt"), "w")

with open(path.joinpath("words.txt"), "r") as f_in:
    for word in f_in.readlines():
        word = word.rstrip()
        words.append(word)

i = len(words) - 1 
# Iterate till 1st element and keep on decrementing i
while i >= 0 :
    file_out.write(words[i] + '\n')
    i -= 1