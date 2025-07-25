import os

CONTACT_FILE = "contacts.txt"

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    with open(CONTACT_FILE, "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("Contact added successfully.")

def display_contacts():
    if not os.path.exists(CONTACT_FILE):
        print("No contacts found.")
        return
    with open(CONTACT_FILE, "r") as file:
        contacts = file.readlines()
        print("\n--- All Contacts ---")
        for contact in contacts:
            name, phone, email = contact.strip().split(",")
            print(f"Name: {name}, Phone: {phone}, Email: {email}")

def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False
    with open(CONTACT_FILE, "r") as file:
        for line in file:
            name, phone, email = line.strip().split(",")
            if search_name in name.lower():
                print(f"Found - Name: {name}, Phone: {phone}, Email: {email}")
                found = True
    if not found:
        print("Contact not found.")

def update_contact():
    search_name = input("Enter name to update: ").lower()
    updated = False
    contacts = []
    with open(CONTACT_FILE, "r") as file:
        for line in file:
            name, phone, email = line.strip().split(",")
            if search_name in name.lower():
                print("Enter new details:")
                name = input("New Name: ")
                phone = input("New Phone: ")
                email = input("New Email: ")
                updated = True
            contacts.append(f"{name},{phone},{email}\n")
    if updated:
        with open(CONTACT_FILE, "w") as file:
            file.writelines(contacts)
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    search_name = input("Enter name to delete: ").lower()
    contacts = []
    deleted = False
    with open(CONTACT_FILE, "r") as file:
        for line in file:
            name, phone, email = line.strip().split(",")
            if search_name in name.lower():
                deleted = True
                continue
            contacts.append(f"{name},{phone},{email}\n")
    with open(CONTACT_FILE, "w") as file:
        file.writelines(contacts)
    if deleted:
        print("Contact deleted.")
    else:
        print("Contact not found.")

def menu():
    while True:
        print("\n--- CONTACT BOOK MENU ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            display_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Try again.")

menu()