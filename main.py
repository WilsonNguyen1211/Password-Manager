import hashlib
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

# Global variable to store passwords
passwords = {}

# Function to generate hash
def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# Function to store credentials
def store_credentials(username, password):
    hashed_password = hash_password(password)
    passwords[username] = hashed_password
    messagebox.showinfo("Success", "Credentials stored successfully.")

# Function to get stored password
def get_password(username):
    if username in passwords:
        return passwords[username]
    else:
        return None

# Function to delete stored password
def delete_password(username):
    if username in passwords:
        del passwords[username]
        messagebox.showinfo("Success", "Password deleted successfully.")
    else:
        messagebox.showerror("Error", "Password not found.")

class PasswordManagerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("400x250")  # Set window size to 400x250 pixels
        self.main_menu()

    def main_menu(self):
        self.clear_frame()

        title_label = ctk.CTkLabel(
            master=self.root, text="Password Manager",
            font=("Roboto Medium", 18),
            text_color="white",
            fg_color="darkgrey"
        )
        title_label.pack(pady=(20, 40))

        button_width = 15  # Adjusted width for buttons

        button_style = {
            "fg_color": "skyblue",
            "hover_color": "black",
            "text_color": "white",
            "width": button_width
        }
        add_credentials_button = ctk.CTkButton(
            master=self.root,
            text="Add Credentials",
            command=lambda: self.add_credentials(),
            **button_style
        )
        add_credentials_button.pack(pady=5)

        view_credentials_button = ctk.CTkButton(
            master=self.root,
            text="View Credentials",
            command=lambda: self.view_credentials(),
            **button_style
        )
        view_credentials_button.pack(pady=5)

        delete_credentials_button = ctk.CTkButton(
            master=self.root,
            text="Delete Credentials",
            command=lambda: self.delete_credentials(),
            **button_style
        )
        delete_credentials_button.pack(pady=5)

        exit_button = ctk.CTkButton(
            master=self.root,
            text="Exit",
            command=lambda: self.root.destroy(),
            **button_style
        )
        exit_button.pack(pady=5)

    def add_credentials(self):
        self.clear_frame()

        entry_width = 30  # Adjusted width for entry widgets
        button_width = 15  # Adjusted width for buttons

        username_label = ctk.CTkLabel(
            master=self.root,
            text="Username:",
            font=("Roboto", 14),
            fg_color="black",
            bg_color="white",
        )
        username_label.pack(pady=(10, 5))

        self.username_entry = ctk.CTkEntry(master=self.root, width=entry_width)
        self.username_entry.pack(fill="x", padx=10)

        password_label = ctk.CTkLabel(
            master=self.root,
            text="Password:",
            font=("Roboto", 14),
            fg_color="black",
            bg_color="white",
        )
        password_label.pack(pady=(10, 5))

        self.password_entry = ctk.CTkEntry(master=self.root, width=entry_width, show="*")  # Show asterisks for password
        self.password_entry.pack(fill="x", padx=10)

        submit_button = ctk.CTkButton(
            master=self.root,
            text="Submit",
            command=self.submit_credentials,
            fg_color="green",
            hover_color="darkgreen",
            text_color="white",
            width=button_width
        )
        submit_button.pack(pady=10, padx=(80, 0), side=tk.LEFT)

        return_button = ctk.CTkButton(
            master=self.root,
            text="Return to Main Menu",
            command=self.main_menu,
            fg_color="red",
            hover_color="darkred",
            text_color="white",
            width=button_width
        )
        return_button.pack(pady=10, padx=(0, 80), side=tk.RIGHT)

    def view_credentials(self):
        self.clear_frame()

        entry_width = 30  # Adjusted width for entry widgets

        username_label = ctk.CTkLabel(
            master=self.root,
            text="Username:",
            font=("Roboto", 14),
            fg_color="black",
            bg_color="white",
        )
        username_label.pack(pady=(10, 5))

        self.username_entry = ctk.CTkEntry(master=self.root, width=entry_width)
        self.username_entry.pack(fill="x", padx=10)

        view_button = ctk.CTkButton(
            master=self.root,
            text="View",
            command=self.show_password,
            fg_color="blue",
            hover_color="darkblue",
            text_color="white",
        )
        view_button.pack(pady=10)

        return_button = ctk.CTkButton(
            master=self.root,
            text="Return to Main Menu",
            command=self.main_menu,
            fg_color="red",
            hover_color="darkred",
            text_color="white",
        )
        return_button.pack(pady=10)

    def delete_credentials(self):
        self.clear_frame()

        entry_width = 30  # Adjusted width for entry widgets

        username_label = ctk.CTkLabel(
            master=self.root,
            text="Username:",
            font=("Roboto", 14),
            fg_color="black",
            bg_color="white",
        )
        username_label.pack(pady=(10, 5))

        self.username_entry = ctk.CTkEntry(master=self.root, width=entry_width)
        self.username_entry.pack(fill="x", padx=10)

        delete_button = ctk.CTkButton(
            master=self.root,
            text="Delete",
            command=self.remove_password,
            fg_color="red",
            hover_color="darkred",
            text_color="white",
        )
        delete_button.pack(pady=10)

        return_button = ctk.CTkButton(
            master=self.root,
            text="Return to Main Menu",
            command=self.main_menu,
            fg_color="red",
            hover_color="darkred",
            text_color="white",
        )
        return_button.pack(pady=10)

    def submit_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Username and password are required.")
            return

        store_credentials(username, password)
        self.main_menu()

    def show_password(self):
        username = self.username_entry.get()
        password = get_password(username)

        if password:
            messagebox.showinfo("Password", f"The password for {username} is: {password}")
        else:
            messagebox.showerror("Error", "Username not found.")

    def remove_password(self):
        username = self.username_entry.get()

        if not username:
            messagebox.showerror("Error", "Username is required.")
            return

        delete_password(username)
        self.main_menu()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = ctk.CTk()
    app = PasswordManagerUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()




