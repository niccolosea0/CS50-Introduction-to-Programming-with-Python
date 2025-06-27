from datetime import date

monthes = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


# Function to check month
def check_month(n):
    return 0 < n < 12

# Function to check day


def check_day(n):
    return 0 < n <= 31

# Function to get date, returns false if month or day is not proper value


def get_date(list):
    month = int(list[0])
    day = int(list[1])
    year = int(list[2])

    if check_month(month) and check_day(day):
        return month, day, year

    return False


while True:

    # Prompt user for input
    prompt = input("Date: ").strip().capitalize()

    # If user input prompt like: mm/dd/yyyy
    if "/" in prompt:
        prompt = prompt.split("/")  # Split input by "/"
        if not prompt[0].isdigit():
            continue

        if get_date(prompt):
            month, day, year = get_date(prompt)  # get month, day, year from function
        else:
            continue
    else:
        # Change month day, yyyy TO month day yyyy
        if not "," in prompt:
            continue

        prompt = prompt.replace(",", "").split(" ")
        if prompt[0] in monthes:
            for i in range(len(monthes)):
                if prompt[0] == monthes[i]:
                    prompt[0] = i + 1
                    break
        else:
            continue

        if get_date(prompt):
            month, day, year = get_date(prompt)
        else:
            continue

    break

# Get date format
current_date = date(year, month, day)

# Output final date
print(current_date)
