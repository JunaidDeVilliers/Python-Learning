# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

my_set = set()
points = 5
win = False

while points > 0:
    user_num = int(input("Enter your number:" ))

    if len(my_set) == 9:
        win = True
        break

    if user_num in my_set:
        points -= 1
        print(f"This number is already in the set. You have have {points} points left")
    else:
        my_set.add(user_num)

if win == True:
    print("Congradulations! You have won")
else:
    print("Game Over!")