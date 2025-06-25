def main():
    text = input("Enter text: ").strip()

    # Call convert function
    updatedText = convert(text)

    # Output updated result
    print(updatedText)


def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")

    return text


main()
