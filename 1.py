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

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Generated Password: ")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
