import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("450x400")
        self.root.resizable(False, False)

        # --- Variables ---
        self.length_var = tk.IntVar(value=16)
        self.use_lowercase_var = tk.BooleanVar(value=True)
        self.use_uppercase_var = tk.BooleanVar(value=True)
        self.use_numbers_var = tk.BooleanVar(value=True)
        self.use_symbols_var = tk.BooleanVar(value=True)
        self.exclude_chars_var = tk.StringVar()
        self.password_var = tk.StringVar()

        # --- UI Layout ---
        self.create_widgets()

    def create_widgets(self):
        # Frame for options
        options_frame = tk.LabelFrame(self.root, text="Password Options", padx=10, pady=10)
        options_frame.pack(padx=10, pady=10, fill="x")

        # Length
        tk.Label(options_frame, text="Password Length:").grid(row=0, column=0, sticky="w", pady=2)
        tk.Scale(options_frame, from_=6, to_=64, orient="horizontal", variable=self.length_var).grid(row=0, column=1, columnspan=2, sticky="ew")

        # Character types
        tk.Checkbutton(options_frame, text="Include Lowercase (abc)", variable=self.use_lowercase_var).grid(row=1, column=0, sticky="w")
        tk.Checkbutton(options_frame, text="Include Uppercase (ABC)", variable=self.use_uppercase_var).grid(row=2, column=0, sticky="w")
        tk.Checkbutton(options_frame, text="Include Numbers (123)", variable=self.use_numbers_var).grid(row=3, column=0, sticky="w")
        tk.Checkbutton(options_frame, text="Include Symbols (!@#)", variable=self.use_symbols_var).grid(row=4, column=0, sticky="w")
        
        # Exclude characters
        tk.Label(options_frame, text="Exclude Characters:").grid(row=5, column=0, sticky="w", pady=5)
        tk.Entry(options_frame, textvariable=self.exclude_chars_var, width=30).grid(row=5, column=1, sticky="w")

        # Generate Button
        generate_button = tk.Button(self.root, text="🚀 Generate Password", command=self.generate_password)
        generate_button.pack(pady=10)

        # Result display
        result_frame = tk.Frame(self.root, relief="sunken", borderwidth=2)
        result_frame.pack(padx=10, pady=5, fill="x")
        password_entry = tk.Entry(result_frame, textvariable=self.password_var, font=("Courier", 12), bd=0, state="readonly")
        password_entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)
        copy_button = tk.Button(result_frame, text="📋 Copy", command=self.copy_to_clipboard)
        copy_button.pack(side="right", padx=5)

    def generate_password(self):
        length = self.length_var.get()
        exclude_chars = self.exclude_chars_var.get()
        
        char_pool = ""
        guaranteed_chars = []

        if self.use_lowercase_var.get():
            lowercase = string.ascii_lowercase
            char_pool += lowercase
            guaranteed_chars.append(random.choice(lowercase))
        if self.use_uppercase_var.get():
            uppercase = string.ascii_uppercase
            char_pool += uppercase
            guaranteed_chars.append(random.choice(uppercase))
        if self.use_numbers_var.get():
            numbers = string.digits
            char_pool += numbers
            guaranteed_chars.append(random.choice(numbers))
        if self.use_symbols_var.get():
            symbols = string.punctuation
            char_pool += symbols
            guaranteed_chars.append(random.choice(symbols))

        # Filter out excluded characters
        char_pool = ''.join([char for char in char_pool if char not in exclude_chars])

        if not char_pool or len(guaranteed_chars) > length:
            messagebox.showerror("Error", "Cannot generate password. Check your settings (e.g., ensure length is sufficient and character pool is not empty after exclusions).")
            return

        # Fill the rest of the password
        remaining_length = length - len(guaranteed_chars)
        password_list = guaranteed_chars + random.choices(char_pool, k=remaining_length)
        
        # Shuffle to ensure randomness
        random.shuffle(password_list)
        final_password = "".join(password_list)
        
        self.password_var.set(final_password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password generated to copy.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()