# Contact Book GUI Application using Python

import tkinter as tk
from tkinter import messagebox

contacts = []

# Add Contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    messagebox.showinfo("Success", "Contact Added Successfully!")
    clear_fields()
    view_contacts()

# View Contacts
def view_contacts():
    contact_list.delete(0, tk.END)

    for contact in contacts:
        contact_list.insert(
            tk.END,
            f"{contact['name']} - {contact['phone']}"
        )

# Search Contact
def search_contact():
    search = search_entry.get().lower()
    contact_list.delete(0, tk.END)

    found = False

    for contact in contacts:
        if search in contact['name'].lower() or search in contact['phone']:
            contact_list.insert(
                tk.END,
                f"{contact['name']} - {contact['phone']}"
            )
            found = True

    if not found:
        messagebox.showinfo("Search", "No Contact Found!")

# Update Contact
def update_contact():
    selected = contact_list.curselection()

    if not selected:
        messagebox.showerror("Error", "Select a contact to update!")
        return

    index = selected[0]

    contacts[index] = {
        "name": name_entry.get(),
        "phone": phone_entry.get(),
        "email": email_entry.get(),
        "address": address_entry.get()
    }

    messagebox.showinfo("Success", "Contact Updated Successfully!")
    view_contacts()

# Delete Contact
def delete_contact():
    selected = contact_list.curselection()

    if not selected:
        messagebox.showerror("Error", "Select a contact to delete!")
        return

    index = selected[0]
    contacts.pop(index)

    messagebox.showinfo("Success", "Contact Deleted Successfully!")
    view_contacts()

# Fill Fields when selecting contact
def select_contact(event):
    selected = contact_list.curselection()

    if selected:
        index = selected[0]
        contact = contacts[index]

        clear_fields()

        name_entry.insert(0, contact['name'])
        phone_entry.insert(0, contact['phone'])
        email_entry.insert(0, contact['email'])
        address_entry.insert(0, contact['address'])

# Clear Fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# GUI Window
root = tk.Tk()
root.title("Contact Book")
root.geometry("700x500")
root.configure(bg="#f0f0f0")

# Title
title = tk.Label(
    root,
    text="📞 Contact Book Application",
    font=("Arial", 20, "bold"),
    bg="#f0f0f0",
    fg="#333"
)
title.pack(pady=10)

# Form Frame
form_frame = tk.Frame(root, bg="#f0f0f0")
form_frame.pack(pady=10)

# Name
tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1)

# Phone
tk.Label(form_frame, text="Phone:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(form_frame, width=30)
phone_entry.grid(row=1, column=1)

# Email
tk.Label(form_frame, text="Email:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=5)
email_entry = tk.Entry(form_frame, width=30)
email_entry.grid(row=2, column=1)

# Address
tk.Label(form_frame, text="Address:", font=("Arial", 12), bg="#f0f0f0").grid(row=3, column=0, padx=5, pady=5)
address_entry = tk.Entry(form_frame, width=30)
address_entry.grid(row=3, column=1)

# Buttons Frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Contact", width=15, bg="#4CAF50", fg="white", command=add_contact).grid(row=0, column=0, padx=5)

tk.Button(button_frame, text="Update Contact", width=15, bg="#2196F3", fg="white", command=update_contact).grid(row=0, column=1, padx=5)

tk.Button(button_frame, text="Delete Contact", width=15, bg="#f44336", fg="white", command=delete_contact).grid(row=0, column=2, padx=5)

# Search Section
search_frame = tk.Frame(root, bg="#f0f0f0")
search_frame.pack(pady=10)

search_entry = tk.Entry(search_frame, width=30)
search_entry.grid(row=0, column=0, padx=5)

tk.Button(search_frame, text="Search", bg="#FF9800", fg="white", command=search_contact).grid(row=0, column=1)

# Contact List
contact_list = tk.Listbox(root, width=60, height=10, font=("Arial", 11))
contact_list.pack(pady=10)

contact_list.bind('<<ListboxSelect>>', select_contact)

# Run App
root.mainloop()