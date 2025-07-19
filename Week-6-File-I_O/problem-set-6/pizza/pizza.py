import sys
import csv
from tabulate import tabulate


if len(sys.argv) != 2:
    sys.exit("Usage: python script.py <filename.csv>")

file_name = sys.argv[1]

if not file_name.endswith(".csv"):
    sys.exit("Provided file is not csv format")


try:
    with open(file_name) as file:
        reader = csv.reader(file)
        header = next(reader)
        menu = list(reader)

except FileNotFoundError:
    sys.exit("Provided file does not exists!")

# Print table representation of csv
print(tabulate(menu, header, tablefmt="grid"))
