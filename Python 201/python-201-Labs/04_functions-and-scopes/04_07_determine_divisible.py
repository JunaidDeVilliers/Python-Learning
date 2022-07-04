# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

def divide(num): 
    if num != 0 and num % 4 == 0:
        return True
    elif num != 0 and num % 7 == 0:
        return True
    else:
        return False

def divide_2(num): 
    if num != 0 and num % 4 == 0 and num % 7 == 0:
        return True
    else:
        return False


usernum = 0

while usernum < 1 or usernum > 1000000000:
    usernum = input("Enter a number between 1 and 1 000 000 000: ")

    if usernum.isdigit():
        usernum = int(usernum)
    else:
        usernum = 0

divisible_by_4_or_7 = divide(usernum)
divisible_by_4_and_7 = divide_2(usernum)

print(f"{usernum} is divisible by either 4 or 7: " + str(divisible_by_4_or_7))
print(f"{usernum} is divisible by both 4 and 7: " + str(divisible_by_4_and_7))