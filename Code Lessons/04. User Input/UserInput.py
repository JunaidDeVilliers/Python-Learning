name = input("What is your name? ")

# all text gotten from the user is string. So we type cast it to int
age = int(input("How old are you? "))

height = float(input("How tall are you? "))

print()

print(f"Hello my name is {name}. I am {age} years old")
print(f"I am {height}m tall")