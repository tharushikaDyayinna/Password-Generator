import string
import random
import tkinter as tk
from tkinter import messagebox

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(length_entry.get())
    
    password = []
    
    for _ in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    
    password = "".join(password)
    
    result_label.config(text="Generated Password: " + password)
    generated_password.set(password)  # Set the generated password to the variable

def copy_to_clipboard():
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(generated_password.get())  # Append the generated password
    root.update()  # Update the clipboard

# main window
root = tk.Tk()
root.title("Password Generator")

# variable to store generated password
generated_password = tk.StringVar()

# place widgets
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=1, column=1, pady=10)

result_label = tk.Label(root, text="Generated Password: ")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# main loop
root.mainloop()
