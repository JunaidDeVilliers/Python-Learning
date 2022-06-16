# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

import pathlib

words = []
path = pathlib.Path("/home/junaid/Desktop/Python/Python 201/python-201-Labs/03_file-input-output/words.txt")

with open(path, "r") as f_in:
    for word in f_in.readlines():
        word = word.rstrip()
        words.append(word)


small = [max(words, key = len)]
big = [min(words, key = len)]

for name in words:
    if len(name) > len(big[0]):
        big = [""]
        big[0] = name
    elif len(name) == len(big[0]):
        big.append(name)

    if len(name) < len(small[0]):
        small = [""]
        small[0] = name
    elif len(name) == len(small[0]):
        small.append(name)

print("Biggest word/words:")
for name in big:
    print(name)

print()

print("Smallest word/words:")
for name in small:
    print(name)

    
