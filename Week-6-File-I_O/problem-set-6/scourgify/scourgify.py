import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Usage: python source.py <before.csv> <after.csv>")


first_file = sys.argv[1]
second_file = sys.argv[2]


students = []
try:
    with open(first_file) as prev_file:
        reader = csv.DictReader(prev_file)
        for row in reader:
            name_parts = row["name"].strip().split(",")
            last, first = name_parts[0], name_parts[1]
            students.append({"first": first.strip(), "last": last.strip(), "house": row["house"]})

except FileNotFoundError:
    sys.exit("Provided file does not exists.")

# Open file where we write stuff
try:
    with open(second_file, "w") as sec_file:
        writer = csv.DictWriter(sec_file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)

except FileNotFoundError:
    sys.exit("Provided file does not exists")
