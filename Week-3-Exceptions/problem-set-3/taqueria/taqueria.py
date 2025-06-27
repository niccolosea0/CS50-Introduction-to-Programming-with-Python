menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Variable to count total amount of price
total = 0

while True:

    # Try to prompt user for input, make input lower, strip, title
    try:
        prompt = input("Item: ").lower().strip().title()

    # If input was "ctr^d" break
    except EOFError:
        break
    else:
        try:
            total += menu[prompt]
        # Check for invalid key and reprompt if its true
        except KeyError:
            continue

        print(f"${total:.2f}")
