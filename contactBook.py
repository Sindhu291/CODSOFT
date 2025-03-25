import csv
import os

CONTACTS_FILE = "contacts.csv"

def initialize_file():
    if not os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Store Name", "Phone Number", "Email", "Address"])

def add_contact():
    store_name = input("Enter Store Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    
    with open(CONTACTS_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([store_name, phone, email, address])
    print("Contact added successfully!\n")

def view_contacts():
    with open(CONTACTS_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            print(f"Store: {row[0]}, Phone: {row[1]}, Email: {row[2]}, Address: {row[3]}")

def search_contact():
    query = input("Enter Store Name, Phone, or Email to search: ")
    with open(CONTACTS_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        found = False
        for row in reader:
            if query in row:
                print(f"Store: {row[0]}, Phone: {row[1]}, Email: {row[2]}, Address: {row[3]}")
                found = True
        if not found:
            print("No contact found.")

def update_contact():
    contacts = []
    query = input("Enter Store Name to update: ")
    found = False
    with open(CONTACTS_FILE, mode='r') as file:
        reader = csv.reader(file)
        contacts = list(reader)
    
    for i, row in enumerate(contacts):
        if row[0] == query:
            print("Enter new details (leave blank to keep current value):")
            store_name = input(f"Store Name ({row[0]}): ") or row[0]
            phone = input(f"Phone ({row[1]}): ") or row[1]
            email = input(f"Email ({row[2]}): ") or row[2]
            address = input(f"Address ({row[3]}): ") or row[3]
            contacts[i] = [store_name, phone, email, address]
            found = True
    
    if found:
        with open(CONTACTS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    contacts = []
    query = input("Enter Store Name to delete: ")
    found = False
    with open(CONTACTS_FILE, mode='r') as file:
        reader = csv.reader(file)
        contacts = list(reader)
    
    for row in contacts:
        if row[0] == query:
            contacts.remove(row)
            found = True
    
    if found:
        with open(CONTACTS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    initialize_file()
    while True:
        print("\nCONTACT MANAGEMENT SYSTEM")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
