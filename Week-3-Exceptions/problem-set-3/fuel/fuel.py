import math


def main():

    # Call convert function and get value of percentage
    percentage = convert()

    # Check value of percentage
    if percentage <= 10:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

# Function to get input from user, reprompt if user inputed incorectly


def get_int():

    while True:
        fraction = input("Fraction: ").split("/")  # Prompt user for input

        try:
            x = int(fraction[0])
            y = int(fraction[1])

        except ValueError:  # If anything goes wrong print text and ask user for input again
            print("Please provide integers!")

        else:   # If nothing goes wrong just break
            return x, y

# Function to convert user's input to percentage number


def convert():
    # Assigning variables
    x, y = get_int()

    # Numbers must be positive
    if x < 0 or y < 0:
        print("Provided number must be positive!")
        x, y = get_int()

    # Try dividing and look for zerodivision error
    try:
        x / y
    except ZeroDivisionError:
        print("Can not divide number by zero")
        x, y = get_int()

    if x > y:
        print("First nubmer can not be greater than second")
        x, y = get_int()

    return round((x/y) * 100)


main()
