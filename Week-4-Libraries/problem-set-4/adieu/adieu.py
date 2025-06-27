import sys

lyrics = "Adieu, adieu,"

name_list = []

while True:
    try:
        name = input("Name: ").strip().capitalize()
    except EOFError:
        print()  # Print new line
        break

    # Append name's in name_list
    name_list.append(name)


# Assign lenght of name_list to variable
list_size = len(name_list)

for i in range(list_size):
    # Check if index is on first elemnt
    if list_size == 1 or i == 0:
        lyrics += f" to {name_list[i]}"  # Concat first name to lyrics

    # Check if index is on last element
    elif i == list_size - 1:
        if list_size > 2:
            lyrics += f", and {name_list[i]}"
        else:
            lyrics += f" and {name_list[i]}"

    # Else name is just between end and beginning
    else:
        lyrics += f", {name_list[i]}"


print(lyrics)
