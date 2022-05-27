# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)

distance = 10
# convert distance from miles to kilometers
distance = distance * 1.6

time = 30.5

speed = distance / (time / 60)

print("The average speed is: " + str(speed) + " kmph")