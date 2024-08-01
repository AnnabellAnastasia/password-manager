from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, f'{password}]')
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title='Oops', message='Please dont leave any fields empty!')
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(),
                                       message=f"There are details you have entered: \nEmail: {username_entry.get()} \nPassword: {password_entry.get()} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", 'a') as f:
                f.write(f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()} \n")
                website_entry.delete(0, 'end')
                username_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize()
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0, )
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website field
website_label = Label(text='Website')
website_label.grid(row=1, column=0)
# Website entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky='w')
website_entry.focus()

# Email/Username field
username_label = Label(text='Email/Username')
username_label.grid(row=2, column=0)
# Username entry
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, sticky='w', columnspan=2)
username_entry.focus()
username_entry.insert(0, 'annabella@gmail.com')

# Password and entry field
password_label = Label(text="Password")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='w')
password_entry.focus()
# Generate Password Button
generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2)

# Add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
