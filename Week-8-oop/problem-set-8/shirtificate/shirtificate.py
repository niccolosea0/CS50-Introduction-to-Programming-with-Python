from fpdf import FPDF

name = input("Name: ")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()


pdf.set_font("Helvetica", "B", 24)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 20, "CS50 Shirtificate", align="C", ln=True)
pdf.ln(10)

shirt_image_path = "shirtificate.png"
image_width = 180
image_height = 120
x = (210 - image_width) / 2
y = 50

pdf.image(shirt_image_path, x=x, y=y, w=image_width, h=image_height)

# Insert shirt image
pdf.image(shirt_image_path, x=x, y=y, w=image_width, h=image_height)

# Overlay name in white text on the shirt
pdf.set_xy(0, y + 45)  # Adjust Y to position text over chest area of shirt
pdf.set_font("Helvetica", "B", 28)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 20, f"{name} took CS50", align="C")

# Save to PDF
pdf.output("shirtificate.pdf")

print("Shirtificate created as shirtificate.pdf!")
