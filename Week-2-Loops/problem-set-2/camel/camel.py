# Prompt user for input
camelCase = input("camelCase: ")

# Loop throug str
for i in camelCase:
    # Find uppercase letter
    if i.isupper():
        # Replace this letter with concatinating string, (_ + letter)
        camelCase = camelCase.replace(i, f"_{i}")

# Making str lowercase and assign it to snake_case
snake_case = camelCase.lower()

# Output result
print(snake_case)
