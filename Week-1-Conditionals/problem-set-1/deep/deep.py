# Askins user for answer and making it to lowercase
answer = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

# Check what answet matches to
match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
