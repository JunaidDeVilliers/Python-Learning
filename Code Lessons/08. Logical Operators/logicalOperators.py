# logical operators (and, or) are used to check if two or more conditional statements are true

temp = int(input("What is the tempereture outside?: "))

if temp >= 0 and temp <= 30:
    print("The weather is good today")
    print("Go outside")
elif temp < 0 or temp > 30:
    print("The weather is bad today")
    print("Stay inside")