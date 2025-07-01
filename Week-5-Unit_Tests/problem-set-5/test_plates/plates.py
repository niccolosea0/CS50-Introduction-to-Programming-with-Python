def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Check's that first two letters of text is alphabetical
def has_first_two_characters(s):
    return s[:2].isalpha()


# Check's that maximum number of characters is 6 and minimum is 2
def has_proper_size(s):
    return 2 <= len(s) <= 6

# Check's that text does not contain numbers in the middle
def ends_with_numbers(text):

    # If text contains numbers and alphabets
    if not text.isalpha():
        # Loop through entire text
        for i in range(len(text)):

            # When we will find first number
            if text[i].isdigit():

                # Check that after that number all characters are numeric too
                if not text[i:].isdigit():
                    return False

    # Return true if text does not contain numbers
    return True


# Check's that zero is not first number
def zero_is_not_first_number(text):
    for i in range(len(text)):
        if text[i].isdigit():
            return int(text[i]) != 0

    return True

# Combines 2 functions and return true if they are both true
def has_valid_numbers(text):
    if zero_is_not_first_number(text) and ends_with_numbers(text):
        return True

    return False



def is_valid(s):

    if s.isalnum() and has_first_two_characters(s) and has_proper_size(s) and ends_with_numbers(s) and zero_is_not_first_number(s) and has_valid_numbers(s):
        return True

    return False

if __name__ == "__main__":
    main()
