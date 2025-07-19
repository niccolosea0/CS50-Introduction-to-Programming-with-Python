import sys
import csv
from PIL import Image, ImageOps
import os

if len(sys.argv) != 3:
    sys.exit("Usage: script.py <input> <output>")


# Check that files have legal expressions
for file in sys.argv[1:]:
    file_tuple = os.path.splitext(file)
    if not file_tuple[1] in [".jpeg", ".jpg", ".png"]:
        sys.exit(
            f"\tFile: '{file}' should have one of the following expressions (jpeg, jpg or png)")

# Access files
first_file = sys.argv[1]
second_file = sys.argv[2]

# Access file's extensions and root
first_file_tuple = os.path.splitext(first_file)
second_file_tuple = os.path.splitext(second_file)

# Check for file's expressions similarity
if first_file_tuple[1] != second_file_tuple[1]:
    sys.exit("\tError: Input and output have different expressions")

try:
    shirt = Image.open("shirt.png")
except FileNotFoundError:
    sys.exit("Provided file 'shirt.png' does not exists")

# get shirt size
size = shirt.size

try:
    photo = Image.open(first_file)
except FileNotFoundError:
    sys.exit(f"Provided file: '{first_file}' does not exists")

# Crop photo to same size ratio as shirt
photo = ImageOps.fit(photo, shirt.size)

# Paste shirt on photo using transperancy mask
photo.paste(shirt, (0, 0), shirt)

# Save photo
photo.save(second_file)
