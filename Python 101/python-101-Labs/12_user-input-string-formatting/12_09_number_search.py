# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

num = 0
check = 1
while num < 1 or num > 1000000000:
    num = int(input("Enter a number between 1 and 1 000 000 000: "))

while check != num:
    check += 1

print(check)

