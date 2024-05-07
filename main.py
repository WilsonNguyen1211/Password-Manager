import hashlib
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

passwords = {}
# generate hash
def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password
# get password

# receive password

class PasswordManagerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PasswordManager")
        self.main_menu()

    def main_menu(self):
        self.start_frame = ctk.CTkFrame(
            master=self.root, fg_color="darkgrey"
        )
        self.start_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.title_label = ctk.CTkLabel(
            master=self.start_frame, text="Password Manager",
            font=("Roboto Medium", 18),
            text_color="white",
            fg_color="darkgrey"
        )
        self.title_label.pack(pady=12)

        button_style = {
            "fg_color": "skyblue",
            "hover_color": "black",
            "text_color": "white"
        }
        self.add_credentials_button = ctk.CTkButton(
            master=self.start_frame,
            text="Add Credentials",
            command=lambda: self.add_credentials(),
            **button_style
        )
        self.add_credentials_button.pack(pady=8)

        self.add_get_credentials_button = ctk.CTkButton(
            master=self.start_frame,
            text="Get Credentials",
            command=lambda: self.get_credentials(),
            **button_style
        )
        self.add_get_credentials_button.pack(pady=8)

        self.add_delete_credentials_button = ctk.CTkButton(
            master=self.start_frame,
            text="Delete Credentials",
            command=lambda: self.delete_credentials(),
            **button_style
        )
        self.add_delete_credentials_button.pack(pady=8)

        self.add_exit_button = ctk.CTkButton(
            master=self.start_frame,
            text="Exit",
            command=lambda: self.exit(),
            **button_style
        )
        self.add_exit_button.pack(pady=8)
    def add_credentials(self):
        pass

    def get_credentials(self):
        pass

    def delete_credentials(self):
        pass

    def exit(self):
        pass

def main():
    root = ctk.CTk()
    app = PasswordManagerUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()