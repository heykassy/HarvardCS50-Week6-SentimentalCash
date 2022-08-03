# TODO
from cs50 import get_float

# Ask how many cents the customer is owed
dollars = get_float("Change owed: ")
while dollars < 0.00:
    dollars = get_float("Change owed: ")

dollars = int(dollars * 100)

# Calculate the number of quarters to give the customer
quarters = dollars // 25
dollars = dollars - quarters * 25

# Calculate the number of dimes to give the customer
dimes = dollars // 10
dollars = dollars - dimes * 10

# Calculate the number of nickels to give the customer
nickels = dollars // 5
dollars = dollars - nickels * 5

# Calculate the number of pennies to give the customer
pennies = dollars // 1
dollars = dollars - pennies * 1

# Sum coins
coins = quarters + dimes + nickels + pennies

print(coins)