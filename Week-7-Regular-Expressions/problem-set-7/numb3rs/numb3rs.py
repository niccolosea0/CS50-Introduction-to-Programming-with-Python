import re


def main():
    print(validate(input("IPV4 Address: ")))


def validate(ip):

    pattern = r"^(\d{1,4})\.(\d{1,4})\.(\d{1,4})\.(\d{1,4})$"

    if matches := re.search(pattern, ip):
        for i in range(1, 5):
            # Check for legit numbers
            if int(matches.group(i)) > 255:
                return False
            # Check for leading zeros
            if len(matches.group(i)) > 1:
                if int(matches.group(i)[0]) == 0:
                    return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
