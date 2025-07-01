import sys


def main():
    # Prompt user for input
    text = input("Input: ").strip()
    result = shorten(text)
    print(f"Output: {result}")


# Loop through entire str
def shorten(text):
    # List of vowels
    vowels = ["a", "e", "i", "o", "u"]

    if not isinstance(text, str):
        raise TypeError("Input must be string")

    result = ""

    for i in text:
        # Check character is vowel character
        if i.lower() not in vowels:
            # Remove character (replace it with nothing)
            result += i

    return result


if __name__ == "__main__":
    main()
