# Prompt user for input
text = input("Input: ").strip()

# List of vowels
vowels = ["a", "e", "i", "o", "u"]

# Loop through entire str
for i in text:
    # Check character is vowel character
    if i.lower() in vowels:
        # Remove character (replace it with nothing)
        text = text.replace(i, "")

print(f"Output: {text}")
