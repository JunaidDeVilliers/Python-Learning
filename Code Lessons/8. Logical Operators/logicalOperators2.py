
temp = int(input("What is the tempereture outside?: "))

if not(temp >= 0 and temp <= 30): # The not changes a false statement to true or vice versa
    print("The weather is bad today")
    print("Stay inside")
elif not(temp < 0 or temp > 30):
    print("The weather is good today")
    print("Go outside")