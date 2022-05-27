# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

amount = float(input("Please enter an investment amount: "))
interest = float(input("Please enter the interest rate: "))
time = float(input("Please enter the amount of years for the investment: "))

print(f"""If you invest {amount}. 
The final amount after {time} years at a {interest}% interest will be: 
{amount * (interest/100 + 1)}""")