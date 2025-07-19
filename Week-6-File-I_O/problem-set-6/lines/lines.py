import sys
import csv

# Ensure that user inputs file name as a second argumemnt
if len(sys.argv) < 2:
    sys.exit("Please provide second argument for python file name.")
elif len(sys.argv) > 2:
    sys.exit("Too many arugments")

# Get file name
file_name = sys.argv[1]

# Check that file is python file
if not file_name.endswith(".py"):
    sys.exit("Provided file is not python file")


# Check that file exists
try:
    file = open(file_name)
except FileNotFoundError:
    sys.exit("File does not exists")

# Open file, read it and count lines
count_lines = 0
with open(file_name) as file:
    for row in file:
        row = row.strip()
        if not (row.startswith("#") or len(row) == 0):
            count_lines += 1

print(count_lines)
