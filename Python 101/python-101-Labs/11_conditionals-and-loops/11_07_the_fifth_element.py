# Use a `for` loop to print out every fifth number counting from 1 to 1000.
# i.e. sum 5, 10, 15, 20 ...

for num in range(1000):
    if num % 5 == 0 and num != 0:
        print(num)
