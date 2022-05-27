# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?

num_int = 5
num_float = 5.6

print(float(num_int))
# just adds .0 to convert number to a float

print(int(num_float))
# all decimal values fall away converting number to an int

print(num_int / num_float)
# when you divide with an int and a float the answer will be a float  

print(num_int * num_float)
# when you multiply with an int and a float the answer will be a float  
