import sys
from datetime import date, datetime
import inflect

def main():

    # Get users birthday date
    user_date = get_date(input("Date: "))

    # get today's date
    today_date = date.today()

    start_date = datetime.combine(user_date, datetime.min.time())
    end_date = datetime.combine(today_date, datetime.min.time())

    # get time difference
    time_diff = end_date - start_date

    # Convert time_diff to minutes
    total_minutes = int(time_diff.total_seconds() / 60)

    minutes_in_words = minutes_to_words(total_minutes)

    print(minutes_in_words)


def get_date(user_input):
    try:
        user_date = date.fromisoformat(user_input)
    except ValueError:
        sys.exit("Invalid input")

    return user_date

def minutes_to_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    return words.capitalize() + " minutes"


if __name__ == "__main__":
    main()
