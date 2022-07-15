# You shouldn't use a lambda expression to name a function object. Lambdas are meant to be anonymous 
# functions that you use as a one-off input to another function.

# You've probably used Python's sorted() function before. This function has an optional key parameter 
# that allows you to pass a function to apply some logic to each element before performing the sort. 
# For example, if you wanted to sort the list of names by the last letter, you can do this by passing 
# an anonymous function to the key parameter:

names = ["Junaid", "Ishaaq", "Tauriq", "Tashriq", "Aaron", "Kyle"]
print(sorted(names, key=lambda x: x[-1])) 