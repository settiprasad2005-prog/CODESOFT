# Password Generator GUI using Python

import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Please enter a positive number!")
            return

        # Character combinations
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate password
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display password
        password_output.config(state='normal')
        password_output.delete(0, tk.END)
        password_output.insert(0, password)
        password_output.config(state='readonly')

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Heading
title_label = tk.Label(
    root,
    text="🔐 Password Generator",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0",
    fg="#333"
)
title_label.pack(pady=15)

# Length input
length_label = tk.Label(
    root,
    text="Enter Password Length:",
    font=("Arial", 12),
    bg="#f0f0f0"
)
length_label.pack()

length_entry = tk.Entry(root, font=("Arial", 12), width=20)
length_entry.pack(pady=5)

# Generate button
generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=generate_password
)
generate_btn.pack(pady=15)

# Password output
password_output = tk.Entry(
    root,
    font=("Arial", 12),
    width=30,
    justify="center",
    state='readonly'
)
password_output.pack(pady=10)

# Run application
root.mainloop()