def main():
    # Prompt user for input
    time = input("What time is it? ")

    # Convert time
    realTime = convert(time)

    # Check time
    if 7.00 <= realTime <= 8.00:
        print("breakfast time")
    elif 12.00 <= realTime <= 13.00:
        print("lunch time")
    elif 18.00 <= realTime <= 19.00:
        print("dinner time")


def convert(time):
    # Split users input by : seperating
    userInput = time.split(":")
    # Value of hours
    hours = float(userInput[0])
    # Value of minutes
    minutes = float(userInput[1])

    # Convert minutes
    minutes /= 60

    # Sum hours and minutes
    time = hours + minutes

    return round(time, 2)


if __name__ == "__main__":
    main()
