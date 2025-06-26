# List of dictionary
calories = [
    {"Apple": 130},
    {"Avocado": 50},
    {"Banana": 110},
    {"Cantaloupe": 50},
    {"Grapefruit": 60},
    {"Grapes": 90},
    {"Honeydew Melon": 50},
    {"Kiwifruit": 90},
    {"Lemon": 15},
    {"Lime": 20},
    {"Nectarine": 60},
    {"Orange": 80},
    {"Peach": 60},
    {"Pear": 100},
    {"Pineapple": 50},
    {"Plums": 70},
    {"Strawberries": 50},
    {"Sweet Cherries": 100},
    {"Tangerine": 50},
    {"Watermelon": 80},
]

# Prompt user to enter name of fruit
fruit = input("Item: ").lower().title()

calory = ""

# Get dictionaries from list
for dict in calories:
    # Loop throug dictionaries keys
    for key in dict.keys():
        # Check if key equals to fruit entered by user
        if key == fruit:
            # Assign calories value to variable calory
            calory = dict[fruit]
            break

# Output value of calories
if not calory == "":
    print(f"Calories: {calory}")
