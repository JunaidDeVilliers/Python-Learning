# TODO: Write a prompt that asks users to "type something to win"
#       They will only win if they type "something" into the prompt
#
# Collect user input
# Compare to the string "something"
# Print a win or lose message

win = False

while win != True:
    answer = input("type something to win ")
    answer = answer.lower()
    if answer == "something":
        win = True
        print("Congradulations, you have won")