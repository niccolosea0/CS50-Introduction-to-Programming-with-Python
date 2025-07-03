# Prompt user for file name
file = input("File name: ").lower().strip()

# Check on which extension file ends
if file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpg") or file.endswith(".jpeg"):
    print("image/jpeg")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".txt"):
    file = file.replace(".txt", "")
    print(f"text/{file}")
elif file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
