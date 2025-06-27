from pyfiglet import Figlet
import sys

# Create a figlet object
figlet = Figlet()

# Check that user has included 2 arguments
try:
    first_argument = sys.argv[1]
    font_style = sys.argv[2]
except IndexError:
    sys.exit("Provide 2 arguments: (-f or --font) and 'font-style'")

# Check that first argument is -f or --font
if first_argument not in ['-f', '--font']:
    sys.exit("First argument is not (-f or --font)")

if font_style not in figlet.getFonts():
    sys.exit("Provided font style is not valid.")

# Create a figlet object from pyfiglet with specific font
figlet = Figlet(font=font_style)

# Prompt user for input
text = input("Input: ")

# Convert text to ascii art
ascii_art = figlet.renderText(text)

# Output style
print(ascii_art)
