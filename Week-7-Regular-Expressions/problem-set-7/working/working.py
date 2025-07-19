import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(text):
    pattern = r"^(?P<first_hour>\d{1,2}):?(?P<first_minutes>\d\d)? (?P<first_meridiem>AM|PM) to (?P<second_hour>\d{1,2}):?(?P<second_minutes>\d\d)? (?P<second_meridiem>PM|AM)$"

    match = re.search(pattern, text)

    if not match:
        raise ValueError("Unsupported format")

    first_time = to_24_hours(
        match.group("first_hour"),
        match.group("first_minutes"),
        match.group("first_meridiem")
    )

    second_time = to_24_hours(
        match.group("second_hour"),
        match.group("second_minutes"),
        match.group("second_meridiem")
    )

    return f"{first_time} to {second_time}"


def to_24_hours(hour_str, minute_str, meridiem):

    hour = int(hour_str)
    minutes = int(minute_str) if minute_str else 0

    if minutes >= 60:
        raise ValueError("Minutes can not be greater than 60")

    if meridiem == "AM":
        if hour == 12:
            hour = 0

    elif meridiem == "PM":
        if hour != 12:
            hour += 12

    return f"{str(hour).zfill(2)}:{str(minutes).zfill(2)}"


if __name__ == "__main__":
    main()
