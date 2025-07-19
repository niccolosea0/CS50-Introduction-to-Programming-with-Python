import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"^<iframe( .*)? src=\"https?://(?:www\.)?youtube\.com/embed/(?P<url_name>\w+).*></iframe>$"

    if matches := re.search(pattern, s):
        name = matches.group("url_name")
        new_url = f"https://youtu.be/{name}"

        return s.replace(s, new_url)


if __name__ == "__main__":
    main()
