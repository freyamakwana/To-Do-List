import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []

        # GUI Components
        self.label_name = tk.Label(root, text="Name:")
        self.label_name.grid(row=0, column=0)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1)

        self.label_phone = tk.Label(root, text="Phone:")
        self.label_phone.grid(row=1, column=0)
        self.entry_phone = tk.Entry(root)
        self.entry_phone.grid(row=1, column=1)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=2, column=1)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=3, column=1)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=4, column=1)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=1)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()

        if name and phone:
            self.contacts.append({"Name": name, "Phone": phone})
            messagebox.showinfo("Success", "Contact added successfully!")
            self.entry_name.delete(0, tk.END)
            self.entry_phone.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both name and phone.")

    def search_contact(self):
        name_to_search = self.entry_name.get()
        found_contacts = [contact for contact in self.contacts if contact['Name'] == name_to_search]

        if found_contacts:
            contact_info = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in found_contacts])
            messagebox.showinfo("Search Result", contact_info)
        else:
            messagebox.showinfo("Search Result", "No contact found with that name.")

    def update_contact(self):
        name_to_update = self.entry_name.get()
        new_phone = self.entry_phone.get()

        for contact in self.contacts:
            if contact['Name'] == name_to_update:
                contact['Phone'] = new_phone
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.entry_name.delete(0, tk.END)
                self.entry_phone.delete(0, tk.END)
                return

        messagebox.showinfo("Update Error", "No contact found with that name.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts to display.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
