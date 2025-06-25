c = 300000000


def main():
    # Assigning c as a global value
    global c

    # Prompt user for input
    m = int(input("m: "))

    # Calculate E=mc^2
    E = m * (c ** 2)

    # Output result
    print(E)


main()
