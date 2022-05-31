print()
# A variable is a container for a value. It behaves like the value it contains

# String variable - A string is a series of characters
first_name = "Junaid"
last_name = "De Villiers"
full_name = first_name + " " + last_name

# int variable contains and whole number and you can do math on it
age = 23

# Float stores a decimal number
height = 1.74
# If you multiply an int and a float the answer will be a float

# Boolean can only store true or falsed
is_human = True

print("Hello my name is " + full_name)
#have to typecast age to string in order to output it on the console
print("I am " + str(age) + " years old. Next year i will be " + str(age + 1) + " years old")
print("I am " + str(height) + "m tall")
print("Is human: " + str(is_human))



print()
# Getting the datatype of the variable
print(type(full_name))
print(type(age))
print(type(height))
print(type(is_human))