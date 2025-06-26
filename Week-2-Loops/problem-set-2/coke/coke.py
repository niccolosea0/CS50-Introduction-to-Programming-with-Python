import math

# Base value of bottle of coke
base_value = 50

# List of available coins
available_coins = [5, 10, 25]

while base_value > 0:

    coin = 0

    # Print very first text
    amount = print(f"Amount Due: {base_value - coin}")

    # Prompt user to input coin
    coin = int(input("Insert Coin: "))

    # Check that coin is valid
    if not coin in available_coins:
        print(f"Invalid coin inserted! Please enter following coins: {available_coins} ")
        continue

    # Subtract base_value of coke and user's input coin
    base_value -= coin

# Change will be whatever is left in base_value after loop
change = int(math.fabs(base_value))

# Output result
print(f"Change Owed: {change}")
