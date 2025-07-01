def main():
    # Prompt user for greeting text, remove whitespaces and make it lowercase
    greeting = input("Greeting: ").strip()

    # Output result
    print(f"${value(greeting)}")

def value(greeting):
    # We will use function startswith(value) to deteremine whether our input starts or not with specific value
    greeting = greeting.lower()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
       return 100

if __name__ == "__main__":
    main()
