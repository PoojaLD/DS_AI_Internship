contacts = {
    "Pooja" : "8147841620",
    "Laxman" : "9591273624",
    "Suvarna" : "7996462761"
    }

contacts ["Supreeth"] = "9353142906"
contacts ["Pooja"] = "8197127307"

print("Look up a name that exists:", contacts.get("Pooja"))
print("Name that does not exist:", contacts.get("Ruby", "Contact not found"))

print("\n--- Contact List ---")
for name, phone in contacts.items():
    print(f"Contact: {name} | phone: {phone}")

