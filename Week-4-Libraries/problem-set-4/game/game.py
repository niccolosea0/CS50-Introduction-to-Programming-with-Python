import sys
import random


def main():

    get_level()


# Function to check number validation
def check_number(str):
    while True:
        try:
            number = int(input(str))
        except ValueError:
            continue
        if number <= 0:
            continue

        return number

# Function to get guess from user


def get_guess(random_number):
    while True:
        guess = check_number("Guess: ")

        if guess < random_number:
            print("Too small!")
            continue
        elif guess > random_number:
            print("Too large!")
            continue
        else:
            print("Just right!")
            sys.exit()


def get_level():
    while True:
        n = check_number("Level: ")

        # Generate random number
        random_number = random.randint(1, n)

        # Call get_guess function

        get_guess(random_number)


main()
