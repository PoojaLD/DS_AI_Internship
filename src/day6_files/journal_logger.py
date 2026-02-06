# Ask user for details
name = input("Enter your name: ")
goal = input("Enter your Daily Goal: ")

# Open file in APPEND mode
with open("journal.txt", "a") as file:
    file.write(f"Name: {name} | Goal: {goal}\n")

print("Entry saved successfully!")
