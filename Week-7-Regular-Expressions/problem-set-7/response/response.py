from validator_collection import is_email


def main():
    print(check(input("EMAIL: ")))


def check(text):
    if is_email(text):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
