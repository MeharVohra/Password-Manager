#%%
import customtkinter
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = customtkinter.CTk()
window.title("Password Manager")
window.geometry("400x600")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


#Labels
heading_label = customtkinter.CTkLabel(master=window, text="Hi, Welcome Back!", font=("algerian",20,"bold"), text_color="#F39422")
heading_label.place(x=100, y=60)

website_label = customtkinter.CTkLabel(master=window, text="Website:")
website_label.place(x=100, y=130)

email_label = customtkinter.CTkLabel(master = window, text="Email/Username:")
email_label.place(x=100, y=210)

password_label = customtkinter.CTkLabel(master = window, text="Password:")
password_label.place(x=100, y=290)

# #Entries
website_entry = customtkinter.CTkEntry(master = window, width=200)
website_entry.place(x=100,y=160)
website_entry.focus()

email_entry = customtkinter.CTkEntry(master = window, width=200, placeholder_text="meharvohra09@gmail.com")
email_entry.place(x=100, y=240)


password_entry = customtkinter.CTkEntry(master = window, width=200)
password_entry.place(x=100, y=320)

# # Buttons
generate_password_button = customtkinter.CTkButton(master = window, text="Generate Password", command=generate_password)
generate_password_button.pack(padx=20, pady=20)
generate_password_button.place(x=100, y=370)
add_button = customtkinter.CTkButton(master = window, text="Add", width=200, command=save)
add_button.place(x=100, y=430)


window.mainloop()
# %%
