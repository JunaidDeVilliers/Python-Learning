# Now you'll use the context manager and the csv module to save your file counter output to a .csv 
# file, so that it's in a format that'll be accessible to other developers:

# First, you're importing the csv module from Python's standard library.
import csv

count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}

# Then you're using a context manager to open up a file in append mode ("a"), and saving the file 
# object to the variable csvfile.
with open("filecounts.csv", "a") as csvfile:

    # Next, you're creating a CSV writer object with the opened csvfile as its input, and you 
    # save it to the variable csvwriter.
    countwriter = csv.writer(csvfile)

    # Now you're preparing the row of data that you want to write to the file. For this, you're 
    # accessing each piece of information through a dictionary lookup and adding them to a list.
    data = [count[""], count[".csv"], count[".md"], count[".png"]]
    # headings = list(count.keys())

    # file_inally, you're using the csvwriter to write the row of data to your file using .writerow().
    # countwriter.writerow(headings)
    countwriter.writerow(data)

