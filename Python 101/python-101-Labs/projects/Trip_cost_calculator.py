distance = int(input("How many kilometers will you be driving:? "))
fuel = int(input("How many litres of fuel does your car use per km? "))
price = int(input("What is the price per litre of fuel? "))

print(f"A {distance}km trip will cost you ${distance * fuel * price}")