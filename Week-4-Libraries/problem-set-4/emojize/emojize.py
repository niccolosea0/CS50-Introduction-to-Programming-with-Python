import emoji

def main():

    # Prompt user for input
    user_input = input("Input: ")
    # Convert user's input to emoji
    my_emoji = emoji.emojize(user_input, language="alias")
    print(f"Output: {my_emoji}")


if __name__ == "__main__":
    main()
