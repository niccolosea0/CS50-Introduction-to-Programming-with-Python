# Prompt user for greeting text, remove whitespaces and make it lowercase
greeting = input("Greeting: ").strip().lower()

# We will use function startswith(value) to deteremine where our input starts or not with specific value
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
