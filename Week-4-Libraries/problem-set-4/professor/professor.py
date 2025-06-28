import random


def main():
    score = get_result()

    print(f"Score: {score}")


# Function to  checek user input and get level
def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if not level in [1, 2, 3]:
            continue

        return level


def generate_integer(level):
    # Get digits
    digits = pow(10, level)

    # Get random numbers
    if level == 1:
        number = random.randrange(0, digits)
    elif level == 2:
        number = random.randrange(10, digits)
    else:
        number = random.randrange(100, digits)

    return number


def get_result():
    # Call level function
    level = get_level()
    score = 0  # Variable to count score
    i = 0  # to loop

    while i < 10:

        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        mistakes = 0  # Variable to count mistakes

        while mistakes < 3:

            try:
                guess = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                mistakes += 1
                continue

            if guess != answer:
                print("EEE")
                mistakes += 1
                continue

            score += 1
            break

        if mistakes == 3:
            print(f"{x} + {y} = {answer}")
            i += 1
            continue

        i += 1

    return score


if __name__ == "__main__":
    main()
