import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os


class PhoneBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phone Book v1.0")
        self.root.geometry("800x600")
        self.contacts = []
        self.load_contacts()

        # Create frames
        self.input_frame = tk.Frame(self.root, padx=10, pady=10)
        self.input_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.display_frame = tk.Frame(self.root, padx=10, pady=10)
        self.display_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Input fields
        tk.Label(self.input_frame, text="Name:").grid(row=0, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.input_frame, text="Phone:").grid(row=1, column=0, sticky=tk.W)
        self.phone_entry = tk.Entry(self.input_frame)
        self.phone_entry.grid(row=1, column=1)

        tk.Label(self.input_frame, text="Location:").grid(row=2, column=0, sticky=tk.W)
        self.location_entry = tk.Entry(self.input_frame)
        self.location_entry.grid(row=2, column=1)

        tk.Label(self.input_frame, text="Email:").grid(row=3, column=0, sticky=tk.W)
        self.email_entry = tk.Entry(self.input_frame)
        self.email_entry.grid(row=3, column=1)

        # Buttons
        self.add_button = tk.Button(
            self.input_frame, text="Add Contact", command=self.add_contact
        )
        self.add_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.search_button = tk.Button(
            self.input_frame, text="Search", command=self.search_contact
        )
        self.search_button.grid(row=5, column=0, columnspan=2, pady=5)

        # Display
        tk.Label(self.display_frame, text="Contacts:").pack()
        self.contacts_listbox = tk.Listbox(self.display_frame, width=50, height=20)
        self.contacts_listbox.pack(fill=tk.BOTH, expand=True)
        self.contacts_listbox.bind("<Double-Button-1>", self.edit_contact)

        self.delete_button = tk.Button(
            self.display_frame, text="Delete Selected", command=self.delete_contact
        )
        self.delete_button.pack(pady=5)

        self.update_listbox()

    def load_contacts(self):
        if os.path.exists("contacts.json"):
            with open("contacts.json", "r") as f:
                self.contacts = json.load(f)

    def save_contacts(self):
        with open("contacts.json", "w") as f:
            json.dump(self.contacts, f, indent=4)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        location = self.location_entry.get().strip()
        email = self.email_entry.get().strip()

        if not name or not phone:
            messagebox.showerror("Error", "Name and Phone are required!")
            return

        contact = {"name": name, "phone": phone, "location": location, "email": email}
        self.contacts.append(contact)
        self.save_contacts()
        self.update_listbox()
        self.clear_entries()
        messagebox.showinfo("Success", "Contact added!")

    def search_contact(self):
        query = simpledialog.askstring("Search", "Enter name to search:")
        if query:
            results = [c for c in self.contacts if query.lower() in c["name"].lower()]
            if results:
                self.contacts_listbox.delete(0, tk.END)
                for contact in results:
                    self.contacts_listbox.insert(
                        tk.END, f"{contact['name']} - {contact['phone']}"
                    )
            else:
                messagebox.showinfo("No Results", "No contacts found.")

    def delete_contact(self):
        selected = self.contacts_listbox.curselection()
        if selected:
            index = selected[0]
            del self.contacts[index]
            self.save_contacts()
            self.update_listbox()
            messagebox.showinfo("Success", "Contact deleted!")
        else:
            messagebox.showwarning("Warning", "Select a contact to delete.")

    def edit_contact(self, event):
        selected = self.contacts_listbox.curselection()
        if selected:
            index = selected[0]
            contact = self.contacts[index]
            # Populate entries
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, contact["name"])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, contact["phone"])
            self.location_entry.delete(0, tk.END)
            self.location_entry.insert(0, contact["location"])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, contact["email"])
            # Change add button to update
            self.add_button.config(
                text="Update Contact", command=lambda: self.update_contact(index)
            )

    def update_contact(self, index):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        location = self.location_entry.get().strip()
        email = self.email_entry.get().strip()

        if not name or not phone:
            messagebox.showerror("Error", "Name and Phone are required!")
            return

        self.contacts[index] = {
            "name": name,
            "phone": phone,
            "location": location,
            "email": email,
        }
        self.save_contacts()
        self.update_listbox()
        self.clear_entries()
        self.add_button.config(text="Add Contact", command=self.add_contact)
        messagebox.showinfo("Success", "Contact updated!")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def update_listbox(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(
                tk.END, f"{contact['name']} - {contact['phone']}"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneBookApp(root)
    root.mainloop()
