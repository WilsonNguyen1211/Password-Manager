import hashlib
from customtkinter import *

passwords = {}
# generate hash
def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password
# get password

# receive password
def main():
    app = CTk()
    app.geometry("500x400")
    set_appearance_mode("dark")
    label = CTkLabel(master=app, text="Password Manager")
    label.place(relx=.5, rely=0.1, anchor='center', font=("Arial", 20, "bold"))
    app.title("Password Manager")

    app.mainloop()


if __name__ == "__main__":
    main()