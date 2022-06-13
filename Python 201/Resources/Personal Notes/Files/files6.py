import csv

# You're operating your file object in read mode ("r")
with open("filecounts.csv", "r") as csvfile:

    # You're using the csv.DictReader() to read in the data.
    # Since you didn't add a header row to your CSV data, you need to define what each piece of data 
    # refers to by passing a sequence to the argument fieldnames. These values will become the keys 
    # for the dictionary that'll get created from each row of your data.
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG"])

    # Finally, you need to convert the reader object to a list() in order to use it as expected.
    counts = list(reader)

# print(counts)
# print(counts[1]["Folder"])

for i in counts:
    for j in i:
        print(j.ljust(10) + i[j])

# Some of this code is similar to when you were using the csv module to write the data to your file. 
# However, you can see a few differences that you'll look at in more detail:

