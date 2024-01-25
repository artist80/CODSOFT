#!/usr/bin/env python3

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        if name not in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print(f"Contact {name} added successfully.")
        else:
            print(f"Contact {name} already exists.")

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contact List:")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

    def search_contact(self, name):
        if name in self.contacts:
            details = self.contacts[name]
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
        else:
            print(f"Contact {name} not found.")

    def update_contact(self, name, phone=None, email=None, address=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            name = input("Enter name to search: ")
            contact_book.search_contact(name)

        elif choice == '4':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (press Enter to keep the current one): ")
            email = input("Enter new email (press Enter to keep the current one): ")
            address = input("Enter new address (press Enter to keep the current one): ")
            contact_book.update_contact(name, phone, email, address)

        elif choice == '5':
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
