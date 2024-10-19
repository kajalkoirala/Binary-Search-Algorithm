import os

# Load contacts from a file
def load_file(filename="contact.txt"):
    contact = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                name, phonenumber, address, email = line.strip().split(",")
                contact.append({
                    "name": name,
                    "phonenumber": phonenumber,
                    "address": address,
                    "email": email
                })
    return contact

# Save contacts to a file
def save_file(contact, filename="contact.txt"):
    with open(filename, "w") as file:
        for details in contact:
            file.write(f"{details['name']},{details['phonenumber']},{details['address']},{details['email']}\n")

# Add new contact
def add_contact(details):
    name = input("Enter name: ")
    phonenumber = input("Enter phonenumber: ")
    address = input("Enter address: ")
    email = input("Enter email: ")

    details.append({
        "name": name,
        "phonenumber": phonenumber,
        "address": address,
        "email": email
    })

# Search for a contact by name or email
def search_contact(details):
    name = input("Enter name: ")
    email = input("Enter email: ")

    for contact in details:
        if (contact['name'].lower() == name.lower() or contact['email'].lower() == email.lower()):
            print(f"Name: {contact['name']}")
            print(f"Phonenumber: {contact['phonenumber']}")
            print(f"Address: {contact['address']}")
            print(f"Email: {contact['email']}")
            return
    print(f"Contact with name {name} or email {email} not found")

# Remove contact by name
def remove_contact(details):
    name = input("Enter name: ")

    for contact in details:
        if contact['name'].lower() == name.lower():
            details.remove(contact)
            print(f"Contact {name} deleted successfully.")
            return
    print(f"Contact {name} not found.")

# Main program loop
def main():
    contacts = load_file()

    while True:
        print(
            "Contact Book Menu:\n"
            "1. Add contact\n"
            "2. Search contact\n"
            "3. Remove contact\n"
            "4. View all contacts\n"
            "5. Save the details\n"
            "6. Exit"
        )
        
        choice = input("Choose from the above (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            remove_contact(contacts)
        elif choice == '4':
            for contact in contacts:
                print(contact)
        elif choice == '5':
            save_file(contacts)
            print("Contacts saved.")
        elif choice == '6':
            print("Thanks for using the contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
