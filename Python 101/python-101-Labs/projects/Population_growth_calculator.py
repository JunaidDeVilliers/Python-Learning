# Write the necessary code to display the total population count for the next 3 years 
# (without a leap year).

# Here are the specifications:

# In the country we want to investigate:

#     The current population is 380,123,456
#     One person is born every 6 seconds
#     One person dies every 12 seconds
#     One person immigrates every 40 seconds

current_population = 380123456

# converting the three years into seconds
time = 60 * 60 * 24 * 365 * 3

# dividing to see how much people will be born in the next 3 years
birth = time / 6

# dividing to see how much people will die in the next 3 years
death = time / 12

#dividing to see how many people will immigrate in the next 3 years
immigrate = time / 40

# subtracting the deaths and immigration and adding the births to the total
future_population = current_population + birth - death - immigrate

print("The current population is: " + str(current_population))
print("In 3 years the population will be: " + str(future_population))
