import math


def main():

    fraction = input("Fraction: ")

    # Call convert function and get value of percentage
    percentage = convert(fraction)

    print(gauge(percentage))

# Function to convert user's input to percentage number
def convert(str):
    # Assigning variables
    while True:
        fraction = str.split("/")
        try:
            x = int(fraction[0])
            y = int(fraction[1])
        except ValueError:
            raise ValueError("Please provide integers")
        break

    # Numbers must be positive
    if x < 0 or y < 0:
        raise ValueError("Provided number must be positive!")

    # Try dividing and look for zerodivision error
    if y == 0:
        raise ZeroDivisionError("Can not divide by zero!")

    if x > y:
        raise ValueError("First nubmer can not be greater than second")


    return round((x/y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
