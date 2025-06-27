# Count of products
grocery = {}


while True:
    try:
        # Prompt user to input fruit name
        fruit = input().lower().strip().title()

    except EOFError:
        break

    else:
        # If fruit is in grocery dictionarty increase it's value by 1
        if fruit in grocery:
            grocery[fruit] += 1

        # If not assign it value by 1
        else:
            grocery[fruit] = 1

# Sort grocery items and save it as a list of tuples in sorted_grocery
sorted_grocery_tuples = sorted(grocery.items())

# Transfer list of tuples in dictionary
sorted_grocery_dict = dict(sorted_grocery_tuples)

for key in sorted_grocery_dict:
    print(grocery[key], key.upper(), sep=" ")
