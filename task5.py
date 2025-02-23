import json

contact_storage = "contacts.json"

def retrieve_contacts():
    try:
        with open(contact_storage, "r") as file_handler:
            return json.load(file_handler)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def store_contacts(data_bank):
    with open(contact_storage, "w") as file_handler:
        json.dump(data_bank, file_handler, indent=4)

def insert_contact():
    contact_directory = retrieve_contacts()
    contact_name = input("Enter contact name: ")
    phone_record = input("Enter phone number: ")
    email_info = input("Enter email: ")
    home_address = input("Enter address: ")

    contact_directory[contact_name] = {
        "Phone": phone_record,
        "Email": email_info,
        "Address": home_address
    }

    store_contacts(contact_directory)
    print("Contact added successfully!")

def display_contacts():
    contact_directory = retrieve_contacts()
    if not contact_directory:
        print("No contacts available.")
    else:
        for entry_name, entry_details in contact_directory.items():
            print(f"\nName: {entry_name}")
            print(f"Phone: {entry_details['Phone']}")
            print(f"Email: {entry_details['Email']}")
            print(f"Address: {entry_details['Address']}")
            print("-" * 30)


def locate_contact():
    contact_directory = retrieve_contacts()
    search_value = input("Enter name or phone number to search: ")
    
    for entry_name, entry_details in contact_directory.items():
        if search_value == entry_name or search_value == entry_details["Phone"]:
            print("\nContact Found:")
            print(f"Name: {entry_name}")
            print(f"Phone: {entry_details['Phone']}")
            print(f"Email: {entry_details['Email']}")
            print(f"Address: {entry_details['Address']}")
            return
    print("Contact not found.")


def modify_contact():
    contact_directory = retrieve_contacts()
    update_name = input("Enter the name of the contact to update: ")

    if update_name in contact_directory:
        print("Enter new details (leave blank to keep unchanged):")
        phone_update = input("New phone number: ") or contact_directory[update_name]["Phone"]
        email_update = input("New email: ") or contact_directory[update_name]["Email"]
        address_update = input("New address: ") or contact_directory[update_name]["Address"]

        contact_directory[update_name] = {
            "Phone": phone_update,
            "Email": email_update,
            "Address": address_update
        }

        store_contacts(contact_directory)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def remove_contact():
    contact_directory = retrieve_contacts()
    delete_name = input("Enter the name of the contact to delete: ")

    if delete_name in contact_directory:
        del contact_directory[delete_name]
        store_contacts(contact_directory)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def contact_manager():
    while True:
        print("\n📒 Contact Book Menu")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        user_choice = input("Enter your choice: ")

        if user_choice == "1": 
            insert_contact()
        elif user_choice == "2":
            display_contacts()
        elif user_choice == "3":
            locate_contact()
        elif user_choice == "4":
            modify_contact()
        elif user_choice == "5":
            remove_contact()
        elif user_choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

contact_manager()