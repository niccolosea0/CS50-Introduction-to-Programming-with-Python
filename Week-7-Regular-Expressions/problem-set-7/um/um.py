import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum\b"  # with boundaries only match word um

    match = re.findall(pattern, s, re.IGNORECASE)

    return len(match)


if __name__ == "__main__":
    main()
