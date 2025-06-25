 def main():
    # Prompt user to input dollars and percent
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    # Calculate tip
    tip = dollars * percent

    # Output tip value
    print(f"Leave ${tip:.2f}")


def dollars_to_float(text):
    # Remove $ sign from input
    value = text.replace("$", "")
    # Convert str to int and return value
    return float(value)


def percent_to_float(text):
    # Remove % sign from input
    value = text.replace("%", "")
    # Convert value to int and divide it to 100 (e.x 15% = 0.15)
    return float(value) / 100


main()
