# Ask user for a filename
filename = input("Enter the filename to open: ")

try:
    # Try to open and read the file
    with open(filename, "r") as file:
        print("\nFile content:\n")
        print(file.read())

# Handle error if file doesn't exist
except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")
