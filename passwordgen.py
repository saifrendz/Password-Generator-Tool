import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import random
import string

def generate_password(length = 12, include_lower = True, include_upper = True, include_digits = True, include_special = True):
    # Password legnth is at least 12 characters
    length = max(12, length)

    #define character sets
    lowercase_chars = string.ascii_lowercase if include_lower else ''
    uppercase_chars = string.ascii_uppercase if include_upper else ''
    digit_chars = string.digits if include_digits else ''
    special_chars = "!@#$%^&*()-_=+[ ]{ }|;:'\",.<>?/"  if include_special else ''

    # Ensure at least one character from each selected set
    required_chars = [
        random.choice(lowercase_chars),
        random.choice(uppercase_chars),
        random.choice(digit_chars),
        random.choice(special_chars)
    ]


    # Fill the remaining characters with a combination of all character sets
    remaining_chars = [
        random.choice(lowercase_chars + uppercase_chars + digit_chars + special_chars)
        for _ in range(length - len(required_chars))
    ]

    # Shuffle the characters
    all_chars = required_chars + remaining_chars
    random.shuffle(all_chars)

    # Generate the password
    password = ''.join(all_chars)

    return password


def generate_password_callback():
    length = int(length_entry.get())
    include_lower = lower_var.get() == 1
    include_upper = upper_var.get() == 1
    include_digits = digit_var.get() == 1
    include_special = special_var.get() == 1

    generated_password = generate_password(length, include_lower, include_upper, include_digits, include_special)
    
    result_label.config(text=f"Generated Paddword: {generated_password}")


# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Styling
# style = ttk.Style()
# style.theme_use("clam")  # Choose a theme (e.g., "clam", "alt", "default", "vista")

# ThemedStyle for better-looking themes
style = ThemedStyle(window)
style.set_theme("radiance")  # Choose a theme (e.g., "radiance", "plastik", "arc")


# Configure styles
style.configure("Tlabel", font=("Airal", 12))
style.configure("TButton", font=("Arial", 12))
style.configure("TCheckbutton", font=("Arial", 12))

# Create and Configure widgets
length_label = ttk.Label(window, text="Password Length: ")
length_entry = ttk.Entry(window)
length_entry.insert(0, "12") # Default length
lower_var = tk.IntVar(value=1)
upper_var = tk.IntVar(value=1)
digit_var = tk.IntVar(value=1)
special_var = tk.IntVar(value=1)

lower_check = ttk.Checkbutton(window, text="Include Lowercase", variable=lower_var)
upper_check = ttk.Checkbutton(window, text="Include Uppercase", variable=upper_var)
digit_check = ttk.Checkbutton(window, text="Include Digits", variable=digit_var)
special_check = ttk.Checkbutton(window, text="Incluse Special Characters", variable=special_var)

generate_button = ttk.Button(window, text="Generate Password", command=generate_password_callback)
result_label = ttk.Label(window, text="Generate Password: ")

# Place widgets in the window
length_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
length_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
lower_check.grid(row=1, column=0, padx=10, pady=5, sticky="w")
upper_check.grid(row=2, column=0, padx=10, pady=5, sticky="w")
digit_check.grid(row=3, column=0, padx=10, pady=5, sticky="w")
special_check.grid(row=4, column=0, padx=10, pady=5, sticky="w")
generate_button.grid(row=5, column=0, columnspan=2, pady=10)
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Run the application
window.mainloop()
