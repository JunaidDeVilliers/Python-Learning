# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(bread, *toppings):
    bread_slice = bread + " slice"
    my_toppings = "\n".join(toppings)
    
    return bread_slice + "\n" + my_toppings + "\n" + bread_slice

print(make_sandwich("White bread", "chees", "turkey", "lettuce", "tomato"))